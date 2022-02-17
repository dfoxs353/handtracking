import cv2
import mediapipe as mp
import pyautogui
import finger

class hand:


    def __init__(self):
        self.camera = cv2.VideoCapture(0)

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.fingers = []
        for finger_v in range(0,21):
            fn = finger.finger(finger_v)

            self.fingers.append(fn)

    def hand_track_draw(self):
        self.hand_draw()



    def hand_trakc(self):
        self.results = self.hands.process(self.imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(self.img, handLms, self.mpHands.HAND_CONNECTIONS)
                for id, point in enumerate(handLms.landmark):

                    self.fingers[id].get_coord(point.x, point.y)
                    if id == 8:
                        self.width, self.height, color = self.img.shape
                        self.width, self.height = int(point.x * self.height), int(point.y * self.width)
                        cv2.circle(self.img, (self.width, self.height), 15, (255, 255, 255), cv2.FILLED)

    def hand_draw(self):

        self.good, self.img = self.camera.read()
        self.imgRGB = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        self.hand_trakc()

        self.img = cv2.flip(self.img, 1)
        cv2.imshow("Camera", self.img)



    def give_finger(self):
        return self.fingers