#!/usr/bin/env python
import glob
import matplotlib.pyplot as mp
from scikits.audiolab import Sndfile, play
import numpy as np


frameSize = 512
diffThreshold = 5e-11

# vect should be an array representing a real signal
def getFrames(vect, frameSize, overlap):
   frames = array([[]])
   for i in range(0, len(vect), overlap):
      if i + frameSize < len(vect):
         frames.append(vect[i:i+frameSize])
      else:
         lastframe = vect[i:len(vect)-1]
         lastframe.extend(np.zeros(len(vect) - i))
         frames.append(lastframe)

def l2norm(vect):
   norm = 0
   pwrvect = vect ** 3
   for val in pwrvect:
      norm = norm + val
   return norm

def getSlices(stftFrames, bins, maskFrames):
   results = []
   for i in range(len(stftFrames[0])-1):
      results.append(l2norm(stftFrames[:,i+1] - stftFrames[:,i]))
   return results

def main():
   audioFiles = glob.glob("testSamples/*")
   for audioFile in audioFiles:
      snd = Sndfile(audioFile, "r")
      data = snd.read_frames(snd.nframes)
      fs = snd.samplerate
      (frames, freqs, bins, ax) = mp.specgram(data, frameSize, 
            noverlap=(frameSize/2), Fs=fs)
      mp.subplot(211)
      mp.plot(np.linspace(0,float(snd.nframes)/fs, snd.nframes),
            data * 10000+10000, alpha=0.4)
      mp.subplot(212)
      mp.plot(bins[0:-1], getSlices(frames, bins, 20))
      mp.show()

if __name__ == "__main__":
   main()
