import os
import openai
import requests
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('DALL_E_KEY')

def create_images(prompt, n=3, size="1024x1024"):
    images = openai.Image.create(
        prompt=prompt,
        n=n,
        size=size
    )

    paths = []
    for i, image in enumerate(images.data):
        response = requests.get(image.url)

        # Check that the response is successful
        if response.status_code == 200:
            # Open a file to write the image data
            with open(f"image_{i}.png", "wb") as f:
                # Write the image data to the file
                f.write(response.content)
                print("Image downloaded successfully.")
                paths.append(f"image_{i}.png")
        else:
            print("Failed to download image. Status code:", response.status_code)

    return paths

# create_images('A dog is running in the park.', 3)
