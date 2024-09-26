import pyaudio
import wave
import simpleaudio


def play_audio(audio_path: str):
    print("Playing recorded audio...")
    wave_obj = simpleaudio.WaveObject.from_wave_file(audio_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()


# Configuration settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Start recording
print("Recording...")
stream = audio.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording
print("Recording finished.")
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded data as a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()


print(f"Saved recording as {WAVE_OUTPUT_FILENAME}")
play_audio(WAVE_OUTPUT_FILENAME)
