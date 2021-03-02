import cv2
import numpy as np

def funcion(img):
    contador = 0
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)

    ret, imgt = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    countours, hierarchy = cv2.findContours(imgt.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rectangles = [cv2.boundingRect(countour) for countour in countours]
    for rect in rectangles:
        cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 0), 2)

        imgn = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0] + rect[2]]
        cv2.resize(imgn,(100,100))
        # Clasificar la imagen imgn
        # Escribir el resultado de la clasificación
        cv2.putText(img, str('hola'), (rect[0], rect[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 0, 0), 3, cv2.LINE_AA)
    return img

cam = cv2.VideoCapture(0)
while True:
    val, img = cam.read()
    img = funcion(img)
    cv2.imshow("Imagen",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
