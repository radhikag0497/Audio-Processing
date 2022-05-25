# Loading the Libraries
from pydub import AudioSegment
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
import os


inp = input("Do you want to play your audio (Yes/No):")
if inp == 'Yes' or inp == 'y':
    import subprocess
    # import listen_audio
    subprocess.call(" python listen_audio.py input.wav", shell=True)

# Read the Audiofile
samplerate, data = read('input.wav')
# Frame rate for the Audio
print(samplerate)

# Duration of the audio in Seconds
duration = len(data)/samplerate
print("Duration of Audio in Seconds", duration)
print("Duration of Audio in Minutes", duration/60)

time = np.arange(0,duration,1/samplerate)

# Plotting the Graph using Matplotlib
plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('input.wav')
plt.show()

#### Split Audio Files
if not os.path.isdir("splitaudio"):
    os.mkdir("splitaudio")

audio = AudioSegment.from_file("input.wav")
lengthaudio = len(audio)
print("Length of Audio File", lengthaudio)

start = 0
# In Milliseconds, this will cut 10 Sec of audio
threshold = 10000
end = 0
counter = 0

while start < len(audio):
    end += threshold
    print(start , end)
    chunk = audio[start:end]
    filename = f'splitaudio/chunk{counter}.wav'
    chunk.export(filename, format="wav")
    counter +=1
    start += threshold

import subprocess
# Listening each chunk
directory = 'splitaudio'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        subprocess.call(" python listen_audio.py "+f, shell=True)