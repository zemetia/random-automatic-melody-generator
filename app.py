from random import randint as rand
import numpy as np
from scipy.io import wavfile as wf
import function_melody_generator as fmg

samplerate = 44100 #Frequecy in Hz
ch_list = [[0,4,7],[0,4,7,11],[0,3,7],[0,3,7,10],[0,4,7,10],[0,4,7,9],[0,5,7],[0,2,7,10],[0,6,9,3],[0,4,7,8]]
sc_list = [[2,2,1,2,2,2,1],[2,1,2,2,2,1,2],[1,2,2,2,1,2,2],[2,2,2,1,2,2,1],[2,1,2,2,1,2,2],[1,2,2,1,2,2,1],[2,1,2,2,1,3,1],[3,2,1,1,3,2]]

def to_list(text,list):
    listhas = []
    if list == "":
        for c in text:
            listhas.append(int(c))
    else:
        for c in text:
            listhas.append(list[int(c)])
    return listhas

tempo = fmg.tempo_ke_detik(int(input("tempo = ")))
ketukan = int(input("ketukan = "))
nama = input("disimpan dengan (*.wav) = ")
kord = input("nada Chord : ")
knci = input("kunci Chord : ")
scla = input("scale :")
if len(knci) != len(kord) or len(scla) != len(kord):
    print("Error!")
else:
    ch = to_list(kord,"")
    chx = to_list(knci,ch_list)
    sc = to_list(scla,sc_list)

ach = len(ch)
ch_a = []
sc_a= []
for c in range(ach):
    ch_a.append(fmg.to_chord(ch[c],chx[c]))
    sc_a.append(fmg.to_scale(ch[c],sc[c]))

ob = fmg.onebait(ch_a,sc_a,ketukan)
result = fmg.get_song_data(ob,tempo)
#untuk menyimpan lagu
print(ob)

wf.write(nama+'.wav', samplerate,result.astype(np.int16))
x = input()


        
