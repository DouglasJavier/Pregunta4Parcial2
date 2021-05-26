# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:18:28 2021

@author: douglas
"""
from PIL import Image, ImageFilter

import numpy as np 

print("-----")
img = Image.open("D:\Documentos\INF-324\pregunta 3 parcial 2\lago.png")
print(img.size)
print(img.mode)
matrizImage = np.asarray(img)

#print(matrizImage[:10,:10,0])
#print(matrizImage[:10,:10,1])
#print(matrizImage[:10,:10,2])
#definimos la matriz de laplace
matrizLaplace=[0, -1, 0, -1, 4, -1, 0, -1, 0]
#extraemos un segmento 10 x 10
matrizR=matrizImage[:11,:11,0]
matrizG=matrizImage[:11,:11,1]
matrizB=matrizImage[:11,:11,2]
convulcionR=0
convulcionG=0
convulcionB=0
#imprimimos la matriz de rojos
print(matrizR)
#imprimimos la matriz de verdes
print(matrizG)
#imprimimos la matriz de azules
print(matrizB)

#imrprimimos las convulciones del segmento extraido y la matriz de laplace
print("Convulción de rojo")
for k in range(1,10):
    for l in range(1,10):
        convulcionR=0
        cont=0
        for i in range(k-1, k+2):
            for j in range(l-1, l+2):    
                convulcionR=convulcionR+matrizLaplace[cont]*matrizR[i][j]
                cont=cont+1
        print(convulcionR," ",end=(""))
    print()
print("Convulción de verde")
for k in range(1,10):
    for l in range(1,10):
        cont=0
        convulcionG=0
        for i in range(k-1, k+2):
            for j in range(l-1, l+2):    
                convulcionG=convulcionG+matrizLaplace[cont]*matrizG[i][j]
                cont=cont+1
        print(convulcionG," ",end=(""))
    print()
print("Convulción de rojo")
for k in range(1,10):
    for l in range(1,10):
        cont=0
        convulcionB=0
        for i in range(k-1, k+2):
            for j in range(l-1, l+2):    
                convulcionB=convulcionB+matrizLaplace[cont]*matrizB[i][j]
                cont=cont+1
        print(convulcionB," ",end=(""))
    print()
    
    
