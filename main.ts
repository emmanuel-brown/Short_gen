const { FfmpegCommand } = require('js-ffmpeg');

async function createVideo(filePaths, outputPath) {
  try {
    // Create a new ffmpeg command
    const command = new FfmpegCommand();

    // Add the input files
    filePaths.forEach(filePath => {
      command.addInput(filePath);
    });

    // Set the output options
    command
      .setOutput(outputPath)
      .addOutputOption('-vcodec', 'libx264')
      .addOutputOption('-pix_fmt', 'yuv420p')
      .addOutputOption('-r', '30')
      .addOutputOption('-s', '1280x720');

    // Run the command
    await command.run();

    console.log('Video file created');
  } catch (err) {
    console.error(err);
  }
}

// Example usage:

(async () => {
  try {
    await createVideo(['./house.png', './clothing.png', './house.png'], 'output.mp4');
    console.log('Video created successfully');
  } catch (err) {
    console.error(err);
  }
})();

