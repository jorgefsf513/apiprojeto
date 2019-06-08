import cv2
import numpy as np
import glob
from pyzbar import pyzbar

#criar array de imagens para teste
imagens = []
files = glob.glob ("C:/Users/jumbo/Desktop/Dados/*.jpg")
for myFile in files:
   #print(myFile)
   image = cv2.imread (myFile)
   imagens.append (image)

#descodificar cada qr code encontrado em cada imagem
t=1
for im in imagens:
    print(t)
    decodedObjects = pyzbar.decode(im)
    if decodedObjects == []:
        string2 = 'C:/Users/jumbo/Desktop/failures/qr' + str(t) + '.jpg'
        cv2.imwrite(string2, im)
    else:
        for obj in decodedObjects:
            # print("Data:",obj.data)
            (x, y, w, h) = obj.rect
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
            decodedtext = obj.data.decode("utf-8")
            txt = "{}".format(decodedtext)
            cv2.putText(im, txt, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        .5, (0, 0, 125), 2)
        string2 = 'C:/Users/jumbo/Desktop/success/qr' + str(t) + '.jpg'
        cv2.imwrite(string2, im)
