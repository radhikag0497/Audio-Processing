# Audio-Processing
Audio Processing Techniques like Play an Audio, Plot the Audio Signals, Merge and Split Audio, Change the Frame Rate, Sample Width and Channel, Silence Remove in Audio, Slow down and Speed up audio

### I am doing following Audio Processing Techniques :

> Play an audio / Listen audio : listen_audio.py
in order to run this file pass filename as argument


> Plot the Audio Signals  : Audio_processing_and_cleaning.py


> Merge and Split Audio Contents : merging_audio_files.py

> Slow down and Speed up the Audio — Speed Changer : speedchangeaudio.py
the frame rate will be changed based on the tweak value. Normal Speed is: 1.0

To Slow down Audio : tweek range below 1.0

To Speed Up Audio : tweek range above 1.0


> **Change the Frame Rate, Channels and Sample Width** : adjust_speech_parameters.py
Set Frame rate 8KHz as 8000, 16KHz as 16000, 44KHz as 44000

Set Channel : 1 is Mono and 2 is Stereo

Set Sample Width

1 : “8 bit Signed Integer PCM”,

2 : “16 bit Signed Integer PCM”,

3 : “32 bit Signed Integer PCM”,

4 : “64 bit Signed Integer PCM”


> **Silence Remove** : silence_removal.py
To run this script: python silenceremove.py ‘aggressiveness’ <inputfile.wav> [aggressiveness mode is an integer between 0 and 3]
(For Eg. python silenceremove.py 3 audio.wav)
Here Silence Removal is done using VAD Algorithm.
Audio file will be converted to frames and will apply Sliding Window Technique on each set of frames to check VAD. 
Voiced frames will be collected in separate list and non-voiced will be removed. 
Finally, all voiced frames in the list will be converted to "Audio file".


## Pre-requisites to be installed:
Need python 3.5 or above:

> pip install webrtcvad==2.0.10 wave pydub simpleaudio numpy matplotlib

**Note:** Two folder are missing (audio and splitaudio), containing the audio files, was unable to upload them via Github web interface.
