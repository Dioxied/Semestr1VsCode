import cv2
import mediapipe as mp
import time
from sound import Sound


cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands(False)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
fingers = [(0, 0),(0, 0)]

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            for id, lm in enumerate(handLMS.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                    fingers[0] = (cx, cy)
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                    fingers[1] = (cx, cy)


            mpDraw.draw_landmarks(img, handLMS, mphands.HAND_CONNECTIONS)
            
            
    vector = int(((fingers[1][0] - fingers[0][0])**2 + (fingers[1][1]-fingers[0][1])**2)**0.5)
    if vector > 100:
        vector = 100
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    Sound.volume_set(vector)

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.putText(img, str(int(vector)), (10, 140), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()