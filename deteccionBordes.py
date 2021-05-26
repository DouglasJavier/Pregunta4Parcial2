# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image, ImageFilter
import numpy as np 

#definimos tamaño de la matriz de laplace 
tamaño = (5,5)

#definimos la matriz de laplace
coeficientes = [0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2 , 16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0]
#coeficientes = [0, -1, 0, -1, 4, -1, 0, -1, 0]
#coeficientes = [-1,- 1, -1, -1, 8, -1, -1, -1, -1]
factor = 1
#cargamos la imagen
imagen_original = Image.open('D:\Documentos\INF-324\pregunta 3 parcial 2\lago.png')
#aplicamos el fintro con la matriz de laplace 
imagen_procesada = imagen_original.filter(ImageFilter.Kernel(tamaño, coeficientes, factor))
 
#guardamos el resultado
 
imagen_procesada.save('D:\Documentos\INF-324\pregunta 3 parcial 2\lago4.png')
 
#se cierran ambos objetos creados de la clase Image
 
imagen_original.close()
 
imagen_procesada.close()
