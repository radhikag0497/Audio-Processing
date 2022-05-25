### Code 1

# import wave

# audiofile1="audiofile1.wav"
# audiofile2="audiofile2.wav"

# concantenated_file="audiofile3.wav"
# frames=[]

# wave0=wave.open(audiofile1,'rb')
# frames.append([wave0.getparams(),wave0.readframes(wave0.getnframes())])
# wave0.close()

# wave1=wave.open(audiofile2,'rb')
# frames.append([wave1.getparams(),wave1.readframes(wave1.getnframes())])
# wave1.close()

# result=wave.open(concantenated_file,'wb')
# result.setparams(frames[0][0])
# result.writeframes(frames[0][1])
# result.writeframes(frames[1][1])

# result.close()


### Code 2

import numpy
import wave
import scipy.io.wavfile
with open('audiofile1.wav', 'rb') as fd:
   contents = fd.read()
contents1=bytearray(contents)
numpy_data = numpy.array(contents1, dtype=float)
scipy.io.wavfile.write("audiofile2.wav", 8000, numpy_data)
