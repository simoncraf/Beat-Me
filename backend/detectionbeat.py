# -*- coding: utf-8 -*-
"""DetectionBeat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10rO5dHt7wup9GAkCV9I70GcB2w9QNpPU
"""

#from google.colab import drive
#drive.mount('/content/drive')
#!pip install librosa mir_eval

#!apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
#!pip install PyAudio

import librosa, mir_eval,librosa.display
import numpy as np

scores_arrs = {
    "1": [0, 1, 2, 3],
    "2": [0, 1, 1.5, 2, 3],
    "3": [0, 1, 2, 2.5, 3, 3.5],
    "4": [0, 1, 3, 3.5],
    "5": [0, 0.25, 0.5, 0.75, 1, 1.25, 2.5, 2.75, 3, 3.25, 3.5],
    "6": [0, 0.5, 0.75, 1, 1.5, 2, 2.25, 2.5, 3],
    "7": [0, 0.5, 1.5, 2, 2.332, 2.666, 3, 3.25],
    "8": [0, 0.5, 1, 1.75, 2, 2.25, 2.5, 2.75, 3.25, 3.5, 3.75],
    "9": [0, 0.5, 1, 1.25, 1.5, 2, 2.5, 2.75, 3, 3.5],
    "10": [0, 0.25, 0.5, 0.75, 1, 1.25, 2.25, 3.25, 3.5],
    "11": [0, 0.25, 0.75, 1, 1.332, 1.666, 2.5, 2.75, 3, 3.25, 3.75],
    "12": [0, 0.25, 0.5, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.75],
    "13": [0, 0.25, 0.5, 0.75, 1, 1.332, 1.666, 2.5, 3.25, 3.5],
    "14": [0, 0.25, 0.75, 1.25, 1.5, 1.75, 2, 2.75, 3, 3.25, 3.75]
}

#file_path = '/content/drive/MyDrive/principiantes de backend+/Backend/Backend/audio/Còpia de 52_rhy1_ref156859.m4a'

import pdb;



def compareAudio(file_path,arr):
    x, sr = librosa.load(file_path)
    print("kk 0")
    onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)#Detect the Onsets
    onset_times = librosa.frames_to_time(onset_frames)
    print(0, np.array(scores_arrs[str(arr)]), onset_times )
    F, P, R = mir_eval.onset.f_measure(np.array(scores_arrs[str(arr)]), onset_times , window=0.35)
    print(1)
    score = P*10
    print(onset_frames)
    print(onset_times)
    print(score)
    return score
    
def stats(score):
    if score > 7.5 :
      return ('Muy bien lo estas haciendo genial, tu puntuacion es:', 4,'estrellas')  
    elif score > 5 and score <= 7.5:
      return('Esta bien, estas mejorando ,tu puntuacion es:', 3, 'estrellas')
    elif score >=2.5 and score <= 5:
      return('Esta bien, pero aun te queda aprender mucho pequeño aprendiz,tu puntuacion es:', 2, 'estrellas')
    elif score < 2.5:
      return('Intenta otra vez, tu puntuacion es:', 1,'estrella')

def validator(file_path,arr):

  x, sr = librosa.load(file_path)
  onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)#Detect the Onsets
  onset_times = np.array(librosa.frames_to_time(onset_frames))
  ground_truth= np.array(arr)
  print(onset_times)
  print(ground_truth)
  feedback = []
  for i in range(min(len(onset_times),len(ground_truth))):
    compare = onset_times[i]-ground_truth[i]
    print(compare)
    if compare < 0.25:
      feedback.append('Perfecto!')
      
    elif compare>=0.25 and compare < 0.5:
      feedback.append('Genial!')
      
    elif compare >=0.5 and compare <= 0.75:
      feedback.append('Bien!')
      
    elif compare < 0.75: 
      feedback.append('Mal')
      
  return feedback

'''
arr = [0, 1, 2, 3]
x, sr = librosa.load(file_path)
onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)#Detect the Onsets
onset_times = librosa.frames_to_time(onset_frames)
print(onset_times)
for i in range(np.size(arr)):
  val = abs(onset_times[i]-arr[i])
  if val < 0.2:
    print("Perfecto!")
  elif val < 0.5:
    print('Vas bien')
  else:
    print('Mal')
  '''

'''
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce el numero del audio: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Audio 1")
    print ("2. Audio 2")
    print ("3. Audio 3")
    print ("4. Audio 4")
    print ("5. Audio 5")
    print ("6. Audio 6")
    print ("7. Audio 7")
    print ("8. Audio 8")
    print ("9. Audio 9")
    print ("10. Audio 10")
    print ("11. Audio 11")
    print ("12. Audio 12")
    print ("13. Audio 13")
    print ("14. Audio 14")
    print ("13. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Audio 1")
        compareAudio(file_path,np.array(scores_arrs.get('0.1')))
    elif opcion == 2:
        print ("Audio 2")
        compareAudio(file_path,np.array(scores_arrs.get('0.2')))
    elif opcion == 3:
        print("Audio 3")
        compareAudio(file_path,np.array(scores_arrs.get('0.3')))
    elif opcion == 4:
        print("Audio 4")
        compareAudio(file_path,np.array(scores_arrs.get('0.4')))
    elif opcion == 5:
        print("Audio 5")
        compareAudio(file_path,np.array(scores_arrs.get('1.1')))
    elif opcion == 6:
        print("Audio 6")
        compareAudio(file_path,np.array(scores_arrs.get('1.2')))
    elif opcion == 7:
        print("Audio 7")
        compareAudio(file_path,np.array(scores_arrs.get('2.1')))
    elif opcion == 8:
        print("Audio 8")
        compareAudio(file_path,np.array(scores_arrs.get('2.2')))
    elif opcion == 9:
        print("Audio 9")
        compareAudio(file_path,np.array(scores_arrs.get('3.1')))
    elif opcion == 10:
        print("Audio 10")
        compareAudio(file_path,np.array(scores_arrs.get('3.2')))
    elif opcion == 11:
        print("Audio 11")
        compareAudio(file_path,np.array(scores_arrs.get('4.1')))
    elif opcion == 12:
        print("Audio 12")
        compareAudio(file_path,np.array(scores_arrs.get('4.2')))
    elif opcion == 13:
        print("Audio 13")
        compareAudio(file_path,np.array(scores_arrs.get('5.1')))
    elif opcion == 14:
        print("Audio 14")    
        compareAudio(file_path,np.array(scores_arrs.get('5.2')))
    elif opcion == 15:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
'''

'''
from essentia.standard import *
import essentia.standard as es
from tempfile import TemporaryDirectory


# Load audio file.
audio = MonoLoader(filename='/content/drive/MyDrive/principiantes de backend+/Backend/Backend/essentia-master/test/audio/recorded/techno_loop.mp3')()

# 1. Compute the onset detection function (ODF).

# The OnsetDetection algorithm provides various ODFs.
od_hfc = OnsetDetection(method='hfc')
od_complex = OnsetDetection(method='complex')

# We need the auxilary algorithms to compute magnitude and phase.
w = Windowing(type='hann')
fft = FFT() # Outputs a complex FFT vector.
c2p = CartesianToPolar() # Converts it into a pair of magnitude and phase vectors.

# Compute both ODF frame by frame. Store results to a Pool.
pool = essentia.Pool()
for frame in FrameGenerator(audio, frameSize=1024, hopSize=512):
    magnitude, phase = c2p(fft(w(frame)))
    pool.add('odf.hfc', od_hfc(magnitude, phase))
    pool.add('odf.complex', od_complex(magnitude, phase))

# 2. Detect onset locations.

onsets = Onsets()

onsets_hfc = onsets(essentia.array([pool['odf.hfc']]),[1])

# This algorithm expects a matrix, not a vector.
# You need to specify weights, but if we use only one ODF
# it doesn't actually matter which weight to give it

onsets_complex = onsets(essentia.array([pool['odf.complex']]), [1])


# Add onset markers to the audio and save it to a file.
# We use beeps instead of white noise and stereo signal as it's more distinctive.

# We want to keep beeps in a separate audio channel.
# Add them to a silent audio and use the original audio as another channel. Mux both into a stereo signal.
silence = [0.] * len(audio)

beeps_hfc = AudioOnsetsMarker(onsets=onsets_hfc, type='beep')(silence)
beeps_complex = AudioOnsetsMarker(onsets=onsets_complex, type='beep')(silence)

audio_hfc = StereoMuxer()(audio, beeps_hfc)
audio_complex = StereoMuxer()(audio,beeps_complex)
audio_beep = StereoMuxer()(beeps_complex,beeps_complex)

# Write audio to files in a temporary directory.
temp_dir = TemporaryDirectory()
AudioWriter(filename=temp_dir.name + '/techno_onsets_hfc_stereo.mp3', format='mp3')(audio_hfc)
AudioWriter(filename=temp_dir.name + '/techno_onsets_complex_stereo.mp3', format='mp3')(audio_complex)
AudioWriter(filename=temp_dir.name + '/techno_onsets_complex_stereo_beeps.mp3', format='mp3')(audio_beep)

rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)

print("BPM:", bpm)
print("Beat positions (sec.):", beats)
print("Beat estimation confidence:", beats_confidence)
'''

'''
import pyaudio
import wave


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
filename = "recording_1.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,channels=channels,rate=sr,frames_per_buffer=chunk,input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * dur)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
'''