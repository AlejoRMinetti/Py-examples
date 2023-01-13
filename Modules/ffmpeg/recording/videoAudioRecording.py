import subprocess as sp

def record_video_and_audio(filename, fps, framesize, duration):
    # Define the ffmpeg command
    command = (
        "ffmpeg",
        "-y",  # overwrite output file if it already exists
        "-f", "alsa",  # audio input format
        "-ac", "2",  # number of audio channels
        "-i", "default",  # audio input device
        "-f", "v4l2",  # video input format
        "-r", str(fps),  # frames per second
        "-i", "/dev/video0",  # video input device
        "-t", str(duration),  # recording duration
        "-c:v", "mpeg4",  # codec for video
        "-c:a", "aac",  # codec for audio
        "-q:v", "0",  # quality for video
        "-q:a", "0",  # quality for audio
        "-b:a", "256k",  # bitrate for audio
        filename  # output file
    )

    # Start recording
    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = pipe.communicate()
    print(out,err)

def main():
    filename = 'output.mp4'
    fps = 30
    framesize = (1920, 1080)
    duration = 10
    record_video_and_audio(filename, fps, framesize, duration)

if __name__ == "__main__":
    main()
