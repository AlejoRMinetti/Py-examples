import cv2
import pyaudio
import wave

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Start capturing video
cap = cv2.VideoCapture(0)

# Set the video frame width and height
cap.set(3, 640)
cap.set(4, 480)

# Define the pyaudio recording parameters
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second

# Create a pyaudio object
p = pyaudio.PyAudio()

# Open a recording stream
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

while True:
    # Capture video frame
    ret, frame = cap.read()

    if ret:
        # Write the video frame
        out.write(frame)

        # Record audio
        data = stream.read(chunk)
        frames.append(data)

        # Display the resulting frame
        cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
p.terminate()

# Save the audio recording
wf = wave.open('audio.wav', 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
