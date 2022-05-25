''' 
Adjust the Frame Rate, Channels and Sample Width in Audio
This help you to preprocess the audio file while doing Data Preparation for “Speech to Text” projects
'''
from pydub import AudioSegment
import subprocess

sound = AudioSegment.from_file("audio/audiofile1.wav")
subprocess.call(" python listen_audio.py audio/audiofile1.wav", shell=True)

print("----------Before Conversion--------")
print("Frame Rate", sound.frame_rate)
print("Channel", sound.channels)
print("Sample Width",sound.sample_width)

# Change Frame Rate #22050
sound =  sound.set_frame_rate(22050)

# Change Channel
sound = sound.set_channels(2)

# Change Sample Width
sound = sound.set_sample_width(3)

# Export the Audio to get the changed 
sound.export("convertedrate.wav", format ="wav")
subprocess.call(" python listen_audio.py convertedrate.wav", shell=True)