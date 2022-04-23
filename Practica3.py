#Isaac Alejandro Gutiérrez Huerta 19110198 7E1
#Sistemas de Visión Artificial

import numpy as np
from matplotlib import pyplot as plt
import cv2 #opencv
import os

os.system("cls")

img1=cv2.imread('Guepardo.png')
img2=cv2.imread('Aguila.png')
img1RGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2RGB = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#Ecualizacion img1
img1YUV = cv2.cvtColor(img1, cv2.COLOR_BGR2YUV)
img1YUV[:,:,0] = cv2.equalizeHist(img1YUV[:,:,0])
imgec1 = cv2.cvtColor(img1YUV, cv2.COLOR_YUV2BGR)

#Ecualizacion img2
img2YUV = cv2.cvtColor(img2, cv2.COLOR_BGR2YUV)
img2YUV[:,:,0] = cv2.equalizeHist(img2YUV[:,:,0])
imgec2 = cv2.cvtColor(img2YUV, cv2.COLOR_YUV2BGR)

imgec1RGB = cv2.cvtColor(imgec1, cv2.COLOR_BGR2RGB)
imgec2RGB = cv2.cvtColor(imgec2, cv2.COLOR_BGR2RGB)


def Operaciones(img1RGB,img2RGB,img1,img2,nombre):
#Histograma
    RES, fc = plt.subplots(4, 3)
    fc[0,0].imshow(img1RGB)
    fc[0,0].set_title('Guepardo')
    fc[0,0].axis('off')

    fc[0,2].imshow(img2RGB)
    fc[0,2].set_title('Águila')
    fc[0,2].axis('off')

    color = ('b','g','r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([img1], [i], None, [256], [0, 256])
        fc[1,0].plot(hist, color = c)
    for i, c in enumerate(color):
        hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
        fc[1,2].plot(hist, color = c)

    res=cv2.imread(nombre+'1.png',1)
    resRGB = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

    fc[0,1].imshow(resRGB)
    fc[0,1].set_title(nombre)
    fc[0,1].axis('off')

    for i, c in enumerate(color):
        hist = cv2.calcHist([res], [i], None, [256], [0, 256])
        fc[1,1].plot(hist, color = c)

#Ecualizacion
    fc[3,0].imshow(imgec1RGB)
    fc[3,0].axis('off')
    fc[3,2].imshow(imgec2RGB)
    fc[3,2].axis('off')

    for i, c in enumerate(color):
        histEcua = cv2.calcHist([imgec1], [i], None, [256], [0, 256])
        fc[2,0].plot(histEcua, color = c)
    for i, c in enumerate(color):
        histEcua = cv2.calcHist([imgec2], [i], None, [256], [0, 256])
        fc[2,2].plot(histEcua, color = c)

    resYUV = cv2.cvtColor(res, cv2.COLOR_BGR2YUV)
    resYUV[:,:,0] = cv2.equalizeHist(resYUV[:,:,0])
    resec = cv2.cvtColor(resYUV, cv2.COLOR_YUV2BGR)
    resecRGB = cv2.cvtColor(resec, cv2.COLOR_BGR2RGB)
    fc[3,1].imshow(resecRGB)
    fc[3,1].axis('off')

    for i, c in enumerate(color):
        histEcua = cv2.calcHist([resec], [i], None, [256], [0, 256])
        fc[2,1].plot(histEcua, color = c)

    plt.savefig(nombre+".jpg")
    plt.show()
#-------------------------------



def Operaciones2(img1RGB,img2RGB,img1,img2,nombre):
#Histograma
    RES, fc = plt.subplots(4, 4)
    fc[0,0].imshow(img1RGB)
    fc[0,0].set_title('Guepardo')
    fc[0,0].axis('off')

    fc[0,3].imshow(img2RGB)
    fc[0,3].set_title('Águila')
    fc[0,3].axis('off')

    color = ('b','g','r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([img1], [i], None, [256], [0, 256])
        fc[1,0].plot(hist, color = c)
    for i, c in enumerate(color):
        hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
        fc[1,3].plot(hist, color = c)

    res=cv2.imread(nombre+'1.png',1)
    resRGB = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    res2=cv2.imread(nombre+'2.png',1)
    res2RGB = cv2.cvtColor(res2, cv2.COLOR_BGR2RGB)

    fc[0,1].imshow(resRGB)
    fc[0,1].set_title(nombre+' 1')
    fc[0,1].axis('off')

    fc[0,2].imshow(res2RGB)
    fc[0,2].set_title(nombre+' 2')
    fc[0,2].axis('off')

    for i, c in enumerate(color):
        hist = cv2.calcHist([res], [i], None, [256], [0, 256])
        fc[1,1].plot(hist, color = c)
    for i, c in enumerate(color):
        hist = cv2.calcHist([res2], [i], None, [256], [0, 256])
        fc[1,2].plot(hist, color = c)

#Ecualizacion
    fc[3,0].imshow(imgec1RGB)
    fc[3,0].axis('off')
    fc[3,3].imshow(imgec2RGB)
    fc[3,3].axis('off')

    for i, c in enumerate(color):
        histEcua = cv2.calcHist([imgec1], [i], None, [256], [0, 256])
        fc[2,0].plot(histEcua, color = c)
    for i, c in enumerate(color):
        histEcua = cv2.calcHist([imgec2], [i], None, [256], [0, 256])
        fc[2,3].plot(histEcua, color = c)

    resYUV = cv2.cvtColor(res, cv2.COLOR_BGR2YUV)
    resYUV[:,:,0] = cv2.equalizeHist(resYUV[:,:,0])
    resec = cv2.cvtColor(resYUV, cv2.COLOR_YUV2BGR)
    resecRGB = cv2.cvtColor(resec, cv2.COLOR_BGR2RGB)
    fc[3,1].imshow(resecRGB)
    fc[3,1].axis('off')

    res2YUV = cv2.cvtColor(res2, cv2.COLOR_BGR2YUV)
    res2YUV[:,:,0] = cv2.equalizeHist(res2YUV[:,:,0])
    resec2 = cv2.cvtColor(res2YUV, cv2.COLOR_YUV2BGR)
    resec2RGB = cv2.cvtColor(resec2, cv2.COLOR_BGR2RGB)
    fc[3,2].imshow(resec2RGB)
    fc[3,2].axis('off')

    for i, c in enumerate(color):
        histEcua = cv2.calcHist([resec], [i], None, [256], [0, 256])
        fc[2,1].plot(histEcua, color = c)

    for i, c in enumerate(color):
        histEcua2 = cv2.calcHist([resec2], [i], None, [256], [0, 256])
        fc[2,1].plot(histEcua2, color = c)

    plt.savefig(nombre+".jpg")
    plt.show()
#-------------------------------



#SUMA
nombre='Suma'
Operaciones(img1RGB,img2RGB,img1,img2,nombre)

#RESTA
nombre='Resta'
Operaciones(img1RGB,img2RGB,img1,img2,nombre)

#MULTIPLICACIÓN
nombre='Multiplicacion'
Operaciones(img1RGB,img2RGB,img1,img2,nombre)

#DIVISIÓN
nombre='Division'
Operaciones(img1RGB,img2RGB,img1,img2,nombre)

#LOGARÍTMO NATURAL
nombre='LogaritmoNatural'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#RAIZ
nombre='RaizCuadrada'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#POTENCIA
nombre='Potencia'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#DERIVADA
nombre='Derivada'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#CONJUNCION
nombre='Conjuncion'
Operaciones(img1RGB,img2RGB,img1,img2,nombre)

#DISYUNCION
nombre='Disyuncion'
Operaciones(img1RGB,img2RGB,img1,img2,nombre)

#NEGACION
nombre='Negacion'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#TRASLACION
nombre='Traslacion'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#ESCALADO
nombre='Escalado'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#ROTACION
nombre='Rotacion'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#TRASLACIÓN A FIN
nombre='TraslacionAFin'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#TRANSPUESTA
nombre='Transpuesta'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)

#PROYECCION
nombre='Proyeccion'
Operaciones2(img1RGB,img2RGB,img1,img2,nombre)


