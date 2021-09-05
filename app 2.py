from random import randint as rand
import numpy as np
from scipy.io import wavfile as wf
import function_melody_generator as fmg

samplerate = 44100 #Frequecy in Hz
tempo = fmg.tempo_ke_detik(200)
ketukan = 8
scale=[2,1,2,2,1,3,1]
nada = 0
chord = [0,3,7]

#chordx = fmg.to_chord(0,chord)
#scalex = fmg.to_scale(0,scale)
#ob = fmg.onebar(chordx,scalex,ketukan)

ch = [0,7,9,5]
chx = [[0,4,7],[0,4,7],[0,3,7],[0,4,7]]
ach = len(ch)
ch_a = []
sc = [[2,2,1,2,2,2,1],[2,2,1,2,2,1,2],[2,1,2,2,1,2,2],[2,2,2,1,2,2,1]]
sc_a= []
for c in range(ach):
    ch_a.append(fmg.to_chord(ch[c],chx[c]))
    sc_a.append(fmg.to_scale(ch[c],sc[c]))

ob = fmg.onebait(ch_a,sc_a,ketukan)
result = fmg.get_song_data(ob,tempo)
#untuk menyimpan lagu
print(ob)

wf.write('test.wav', samplerate,result.astype(np.int16))
x = input()


        
