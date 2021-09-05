from random import randint as rand
import numpy as np

def onebar():
    p_read = []
    t_read = []
    for x in range(20):
        a = rand(0,13)
        t_read.append(a)
        if a > 0:
            p_read.append(a-1)
        else:
            p_read.append(None)
    return p_read,t_read

def translate(melody):
    nada = ['x','c','c#','d','d#','e','f','f#','g','g#','a','a#','b','c']
    translated = [nada[i] for i in melody]
    return translated

