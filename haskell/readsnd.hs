import qualified Sound.File.Sndfile as Snd
import System.IO (hGetContents, Handle, openFile, IOMode(..))
import qualified Sound.File.Sndfile.Buffer.StorableVector as BV
import qualified Data.StorableVector as V
import qualified Graphics.Gnuplot.Simple as GP
import qualified Array as A
import DSP.Basic

sndFileName = "../testSamples/5650__pushtobreak__valihaloop5-5.aif"

readWavFile :: String -> IO (V.Vector Double)
readWavFile fileName = do
   handle <- Snd.openFile fileName Snd.ReadMode Snd.defaultInfo
   (info, Just buf) <- Snd.hGetContents handle :: IO (Snd.Info, Maybe (BV.Buffer Double))
   return (BV.fromBuffer buf)

arrayFromVector :: V.Vector Double -> A.Array Int Double
arrayFromVector vect =
   let l = V.length vect - 1 in
      A.array (0, l) (zip [0..l] (V.unpack vect))

getMax :: V.Vector Double -> Double
getMax vect = V.maximum (V.map abs (vect))

getFrames :: V.Vector Double -> Int -> Int -> [V.Vector Double]
getFrames inVect frameSize hop =
   [getFrame inVect start frameSize | start <- [0, hop .. (V.length inVect)]]

getFrame :: V.Vector Double -> Int -> Int -> V.Vector Double
getFrame inVect start length =
   V.append subString padding
   where
      subString = vectSlice start length inVect
      padding = V.replicate (length - (V.length subString)) 0 :: V.Vector Double

vectSlice :: Int -> Int -> V.Vector Double -> V.Vector Double
vectSlice start len x = V.take len $ V.drop start x

main :: IO ()
main = do
   audioVect <- readWavFile sndFileName
   print $ arrayFromVector audioVect
   --GP.plotList [] (V.unpack audioVect)
