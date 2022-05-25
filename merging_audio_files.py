import os
from pydub import AudioSegment
import glob
import subprocess

# if "audio" folder not exists, it will create
if not os.path.isdir("audio"):
    os.mkdir("audio")

# Grab the Audio files in "audio" folder
wavfiles = glob.glob("audio/*.wav")
print(wavfiles)
for wav in wavfiles:
    subprocess.call(" python listen_audio.py "+wav, shell=True)
# Loopting each file and include in Audio Segment
wavs = [AudioSegment.from_wav(wav) for wav in wavfiles]

combined = wavs[0]

# print(combined)
# Appending all the audio file
''' 
audiofile1.wav: hello how are you
audiofile2.wav: good morning
audiofile3.wav: hello how are you good morning
'''
for wav in wavs[1:]:
    combined = combined.append(wav)

# Export Merged Audio File
combined.export("Mergedaudio.wav", format="wav")

subprocess.call(" python listen_audio.py Mergedaudio.wav", shell=True)