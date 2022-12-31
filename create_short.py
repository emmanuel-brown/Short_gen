import cv2
import os
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip
import img_gen

story = "Humans and their ridiculous obsession with their nails. Always painting them and filing them and buffing them. It's like they can't stand to have a single nail out of place. And don't even get me started on the lengths they go to in order to make their nails look perfect. Gel polish, acrylics, manicures, pedicures - it's like they have a never-ending list of ways to pamper their digits. And don't even get me started on the ridiculous names they give to different nail polish colors. 'Teal the Cows Come Home'? 'Blushing Bride'? Please. How do they even find the time and energy to devote to such frivolous pursuits? I mean, seriously, it's just nails. Get over it."

num_of_images = 10
img_gen_paths = img_gen.create_images(story, num_of_images)
print(img_gen_paths)

if len(img_gen_paths) != num_of_images:
    print("ERROR: " + "Image generation failed.")
    exit(1)


# Set the video codec and the FPS
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30

# Set the width and height of the output video
width = 640
height = 480

# Create a VideoWriter object
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# List the specific images
images = img_gen_paths

# Set the duration of each frame in the output video
duration = 3000  # in milliseconds

# Iterate over the images
for image in images:
    # Load the image
    img = cv2.imread(image)

    # Get the original size of the image
    rows, cols, _ = img.shape

    # Calculate the size of the scaled image
    scaled_rows, scaled_cols = min(rows, cols), min(rows, cols)

    # Resize the image to a 1:1 aspect ratio
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    # Write the image to the output video
    for i in range(fps * duration // 1000):
        out.write(img)

# Release the VideoWriter object
out.release()

def save_speech(text, filename):
    # Create a gTTS object
    tts = gTTS(text=text)

    # Save the speech to an audio file
    tts.save(filename)

# Test the function
save_speech(story, "hello.mp3")

def combine_video_and_audio(video_file, audio_file, output_file):
    # Load the video file and the audio file
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)

    # Add the audio to the video
    final_clip = video.set_audio(audio)

    # Save the combined video and audio
    final_clip.write_videofile(output_file)

# Test the function
combine_video_and_audio("output.mp4", "hello.mp3", "output_1.mp4")
    
