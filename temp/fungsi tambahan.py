import numpy as np
from random import randint as rand

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
	
def probab(chord, scale):
	ch_arr = to_chord(chord)
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
	pr_dom = 5
	pr_sdom = 4
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
	return hasil
	
def onebait(chord_array, scale, ketukan):
	hasil = []
	#perlu perbaikan di chord dan scale
	#misal nada dasar c major, maka jika chord G akan menggunakan scale mixolydian
	for ya in chord_array:
		hasil.append(onebar(ya,scale,ketukan))
	return hasil
	

		
	
	
	
	
	
	
	
	