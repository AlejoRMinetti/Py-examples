This example uses the ffmpeg command-line tool to record video and audio, specifying the input devices and codecs to use, and the duration of the recording. You'll need to have ffmpeg installed on your system and added to PATH, you can check if it's installed by running ffmpeg -version in terminal.

The resulting file will be an MP4 file, which can be played by most media players, it will contain both the audio and video stream inside it.

Note that, this example assumes the default video and audio input devices are used, if you have multiple devices connected and you need to select a specific one, you will need to specify the input device index or name instead of default and /dev/video0 respectively.