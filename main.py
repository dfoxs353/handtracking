import handtrakcer as ht
import gesture_control as gc
import cv2


gc = gc.control()
if __name__ == "__main__":

    while True:
        gc.check_geture()

        if cv2.waitKey(1) == ord('q'):
            break

