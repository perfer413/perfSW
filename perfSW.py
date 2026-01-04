#source .env/bin/activate
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)


while True:
    ret, img = cap.read()
    cv2.imshow("hand", img)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
