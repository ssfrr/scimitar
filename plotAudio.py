import glob
import matplotlib.pyplot as mp
from scikits.audiolab import Sndfile, play
import numpy as np


def main():
   audioFiles = glob.glob("testSamples/*")
   for audioFile in audioFiles:
      snd = Sndfile(audioFile, "r")
      data = snd.read_frames(snd.nframes)
      play(data)
      mp.plot(data)
      mp.show()

if __name__ == "__main__":
   main()
