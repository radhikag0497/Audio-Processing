# Import packages
from pydub import AudioSegment
from pydub.playback import play
import sys

def main(arg):
    print("Listening Audio, from file:",arg)
    # Play
    playaudio = AudioSegment.from_file(arg, format="wav")
    play(playaudio)

if __name__=="__main__":
    main(sys.argv[1])