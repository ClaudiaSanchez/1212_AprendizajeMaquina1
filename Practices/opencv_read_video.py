import cv2


def funcion(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (5, 5), 0)

  ret, imgt = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
  countours, hierarchy = cv2.findContours(imgt.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  rectangles = [cv2.boundingRect(countour) for countour in countours]
  c = 0
  for rect in rectangles:
    if rect[2] > 50 and rect[3] > 50:
      imgn = img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
      imgn = cv2.resize(imgn, (100, 100))
      # cv2.imwrite('res/img'+str(c)+".png",imgn)
      c += 1

      # Clasificar la imagen imgn
      # Escribir el resultado

      cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 0), 2)
      cv2.putText(img, str('hola'), (rect[0], rect[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 0, 0), 3, cv2.LINE_AA)
  return img

captura = cv2.VideoCapture('billetes.mp4')
while (captura.isOpened()):
  ret, img = captura.read()

  img = funcion(img)

  if ret == True:
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break
captura.release()
cv2.destroyAllWindows()