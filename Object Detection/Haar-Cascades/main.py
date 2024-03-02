import cv2

harcascade = "haarcascade_frontalface_default.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) # height

while True:
    success, img = cap.read()
    facecascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = facecascade.detectMultiScale(img_gray, 1.1, 4)


    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow("Face", img_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break