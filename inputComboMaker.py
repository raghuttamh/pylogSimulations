def binConvert(n,t):
    binary=format(n,'b')
    while len(binary)<t:
        binary='0'+binary
    array=[]
    for i in range(len(binary)):
        array.append(int(binary[i]))
    return array

import numpy
def comboMatrixMaker(n):
    mat=[]
    for i in range(2**n):
        mat.append(binConvert(i,n))
    return numpy.array(mat).T
