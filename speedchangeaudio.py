### Speed Changer-Slow down and Speed up
''' 
Normal Speed of Every Audio : 1.0. 
To Slow down audio, tweak the range below 1.0 and to Speed up the Audio, tweak the range above 1.0
Adjust the speed as much as you want in “speed_change” function parameter
'''

from pydub import AudioSegment
import subprocess

sound = AudioSegment.from_file("audio/audiofile1.wav")
def speed_change(sound, speed):
    # print(sound.raw_data)
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data,
        overrides={"frame_rate": int(sound.frame_rate * speed)})
    filename = 'changed_speed_audiofile1.wav'
    sound_with_altered_frame_rate.export(filename, format='wav')

    # listen audio
    s = AudioSegment.from_file(filename)
    print('Sample_rate of new file:', s.frame_rate)
    s = s.set_frame_rate(16000)
    print('Changed Sample_rate of new file:', s.frame_rate)
    conv_wave = "convertedrate.wav"
    sound.export(conv_wave, format ="wav")
    subprocess.call(" python listen_audio.py "+conv_wave, shell=True)
    # Not able to listen to new Altered audio file because of weird sample rate i.e. 12800 

# To Slow down audio
# slow_sound = speed_change(sound, 0.8)
# To Speed up the audio 
fast_sound = speed_change(sound, 1.2)
