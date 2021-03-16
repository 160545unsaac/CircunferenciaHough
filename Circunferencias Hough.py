# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:32:02 2021

@author: Usuario
"""

import numpy as np
import cv2
def video(frame):
    # Se hara la lectura de la imagen
    img = frame
    
    src = cv2.medianBlur(img, 5)
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(src, cv2.HOUGH_GRADIENT, 1, 20,
                                param1=50, param2=30, minRadius=0, maxRadius=0)
    
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # dibujar circulo 
        cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
        # dibujar centro
        cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)
    
    # Mostrar la imagen original con todas las líneas halladas
    return img

def video2(frame):
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #imagen a escala de grises     
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] # utiliza para aplicar el umbral     
    output=frame.copy()     
    #circles=cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,2,100,param1=50,param2=30,                             
    # minRadius=50,maxRadius=100)     
    circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 2,400, param1=50, param2=30, minRadius=50,maxRadius=200) 
    #aplicamos la transformada de Hough de openCV     
    if circles is not None: 
        circles = np.round(circles[0, :]).astype("int") 
        #ponemos en un arreglo los circulos detectados         
    for (x,y,r) in circles:             
        cv2.circle(output, (x,y), r, (0,255,0), 2)#dibujamos los circulos encontrados
    return output

cap = cv2.VideoCapture(2)

while (True):
    ret, frame = cap.read()
    #cv2.imshow('video1',frame)
    i = video2(frame)
    cv2.imshow('video2',i)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
