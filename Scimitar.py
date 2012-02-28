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
   slices = []
   shadow = 0
   for i in range(len(stftFrames[0])-1):
      if shadow == 0 and \
            l2norm(stftFrames[:,i+1] - stftFrames[:,i]) > diffThreshold and \
            l2norm(stftFrames[:,i+1]) > l2norm(stftFrames[:,i]):
         slices.append(bins[i+1])
         shadow = maskFrames
      elif shadow > 0:
         shadow = shadow - 1
   return slices

def main():
   audioFiles = glob.glob("testSamples/*")
   for audioFile in audioFiles:
      snd = Sndfile(audioFile, "r")
      data = snd.read_frames(snd.nframes)
      fs = snd.samplerate
      (frames, freqs, bins, ax) = mp.specgram(data, frameSize, 
            noverlap=(frameSize/2), Fs=fs)
      mp.plot(np.linspace(0,float(snd.nframes)/fs, snd.nframes),
            data * 10000+10000, alpha=0.4)
      for time in getSlices(frames, bins, 20):
         mp.axvline(time, color="red", alpha=0.5)
         print time
      mp.show()

if __name__ == "__main__":
   main()
