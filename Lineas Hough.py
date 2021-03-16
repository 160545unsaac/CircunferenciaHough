# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:22:25 2021

@author: Usuario
"""

import numpy as np
import cv2
def video(frame):
    # Se hara la lectura de la imagen
    img = frame
    
    # Se convierte a nivel de grises
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # Después se le aplica la detección de bordes por Canny 
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    # En este punto es recomdnable en ocasiones realizar primero
    # un filtrado, después un la detección de bordes, para 
    # posteriormente hacer erosión y ensanchamiento
    
    # La función HpughLines permitirá obtener el arreglo 2D requerido
    # en la transformada de Hough
    # Parámetros (en orden):
    # imagen a la que se le aplicará la transformación
    # La resolución de la distancia para el acumulador (r)
    # La resolución en ángulo para el acumulador (theta)
    # umbral para conocer si se toma como línea o no (revisar: https://www.learnopencv.com/hough-transform-with-opencv-c-python/)
    # posterioemente se incluye un None, estuve revisando por varios lados y no comprendo por que razón se debe incluir
    # este parámetro, ya que en caso contrario, el programa falla
    lines = cv2.HoughLines(edges,1,np.pi/180,150,None)
    
    # en ocasiones (sobre todo si no se coloca None) la transformada regresa un valor None y todo falla
    if lines is not None:
        # Recorrer los resultados
        for i in range(0, len(lines)):
            # Obtener los valores de rho (distacia)
            rho = lines[i][0][0]
    		# y de theta (ángulo)
            theta = lines[i][0][1]
    		# guardar el valor del cos(theta)
            a = np.cos(theta)
    		# guardar el valor del sen(theta)
            b = np.sin(theta)
    		# guardar el valor de r cos(theta)
            x0 = a*rho
    		# guardar el valor de r sen(theta), todo se está haciendo de forma paramétrica
            y0 = b*rho
    		# Ahora todo se recorrerá de -1000 a 1000 pixeles
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            
    		# Mostrar los valores hallados
            print("({},{})  ({},{})".format(x1,y1, x2,y2))
    		# Generar las líneas para montarlas en la imagen original
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
    # Mostrar la imagen original con todas las líneas halladas
    return img
cap = cv2.VideoCapture(2)

while (True):
    ret, frame = cap.read()
    #cv2.imshow('video1',frame)
    i = video(frame)
    cv2.imshow('video2',i)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

