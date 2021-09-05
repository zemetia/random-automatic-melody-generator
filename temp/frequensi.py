import numpy as np
from scipy.io.wav import write

samplerate = 44100 #Frequecy in Hz

def get_wave(freq, duration=0.5):
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)   
    return wave

def get_song_data(music_array):
	base_freq =261.63
	for ya in music_array:
            if ya == None:
                song.append(get_wave(0))
            else:
                song.append(get_wave(base_freq*(2**(ya/12))))
	song = np.concatenate(song)
	return song

lagu = [0,2,4,5,7,9,11,12]
result = get_song_data(lagu)

#untuk menyimpan lagu
write('test.wav', samplerate,result.astype(np.int16))
