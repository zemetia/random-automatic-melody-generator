from random import randint as rand
import numpy as np

def get_wave(freq, duration=0.5):
    samplerate = 44100
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)   
    return wave

def get_wave_piano(freq, duration=0.5):
    samplerate = 44100
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * ((np.sin(np.pi * freq * t))**3 + np.sin(np.pi*freq*(t+(2/3))))
    return wave

def get_song_data(music_array, tpd):
    base_freq =261.63
    song = []
    for ya in music_array:
        if ya == None:
            song.append(get_wave(0,tpd))
        else:
            song.append(get_wave(base_freq*(2**(ya/12)),tpd))
    song = np.concatenate(song)
    return song

def translate(melody):
    nada = ['x','c','c#','d','d#','e','f','f#','g','g#','a','a#','b','c']
    translated = [nada[i] for i in melody]
    return translated

def tempo_ke_detik(tempo):
    tempo /= 60
    interval = 1/tempo
    return interval

def to_chord(nada, chord):
    lc = len(chord)
    chord = np.array(chord)
    note = np.array([nada for x in range(lc)])
    hasil = chord + note
    return hasil

def to_scale(nada,scale):
    sc = [nada]
    a = nada
    for x in scale:
        a += x
        sc.append(a)
    return sc
    
def probab(chord, scale):
    ch_arr = chord
    for x in ch_arr:
        if x > 12:
            ch_arr = np.append(ch_arr,x-12)
    sub_dom = []
    tambahan = []
    all = scale
    for narr in scale:
        if narr not in ch_arr:
            sub_dom.append(narr)
    for barr in chord:
        if barr not in scale:
            all.append(barr)
    for x in range(0,12):
        if x not in all:
            tambahan.append(x)
    return ch_arr, sub_dom, tambahan

def acak(r):
    ar =[]
    sudah = []
    x =0
    while x in range(len(r)):
        ran = rand(0, len(r)-1)
        while ran in sudah:
            ran = rand(0, len(r)-1)
        ar.append(r[ran])
        sudah.append(ran)
        x +=1
    return ar

def onebar(chord, scale, ketukan):
    pr_dom = 50
    pr_sdom = 30
    pr_mdom = 1
    cmpr_prob = [None for x in range(10)]
    hasil = []
    
    dom,sdom,mdom = probab(chord,scale)
    for x in dom:
        for y in range(pr_dom):
            cmpr_prob.append(x)
    for x in sdom:
        for y in range(pr_sdom):
            cmpr_prob.append(x)
    for x in mdom:
        for y in range(pr_mdom):
            cmpr_prob.append(x)
    
    for bar in range(ketukan*2):
        cmpr_prob = acak(cmpr_prob)
        pc = len(cmpr_prob)
        hasil.append(cmpr_prob[rand(0,pc-1)])
    print(dom,sdom,mdom)
    return hasil
    
def onebait(chord_array, scale_array, ketukan):
    hasil = []
    #perlu perbaikan di chord dan scale
    #misal nada dasar c major, maka jika chord G akan menggunakan scale mixolydian
    for ya in range(len(chord_array)):
        xa = onebar(chord_array[ya],scale_array[ya],ketukan)
        for a in xa:
            hasil.append(a)
    return hasil

