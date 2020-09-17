from PIL import Image
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
from googlesearch import search
import urllib


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #Webcam
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)

    for barcode in decodedObjects:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)
        if barcodeType == "QRCODE":
            # print the barcode type and data to the terminal
            print(f"[INFO] Found {barcodeType} barcode: {barcodeData}")

        else:
            for obj in decodedObjects:
                # print the barcode type and data to the terminal
                print(f"[INFO] Found {barcodeType} barcode {barcodeData}")

                """
                #search on google
                for j in search(barcodeData, tld="com", num=2, stop=2, pause=2):
                    print(j)
                """

    # show the output image
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
