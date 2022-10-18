import cv2

cap = cv2.VideoCapture(1+ cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FPS, 10)
fps = int(cap.get(5))
print(fps)
# cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        print(data)
        break
    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

