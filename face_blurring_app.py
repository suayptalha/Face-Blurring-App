import cv2

cascade_path = "haarcascade_frontalface_default.xml" #That's an example path. You can change it!

faceCascade = cv2.CascadeClassifier(cascade_path)

cap = cv2.VideoCapture(0)
cv2.waitKey(0)
def blurred():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        faces = faceCascade.detectMultiScale(frame,1.1,4) #Detecting the faces
        for (x,y,w,h) in faces:
            imgBlurred = cv2.GaussianBlur(frame[y:y+h, x:x+w],(21,21),0) #Blurring the faces
            frame[y:y+h, x:x+w] = imgBlurred
        frame1 = cv2.flip(frame,1)
        cv2.imshow("Blurred",frame1)
        cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == ord('q'): #Press 'q' button to exit
            cv2.destroyAllWindows()
            break
blurred()
