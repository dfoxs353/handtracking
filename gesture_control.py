import handtrakcer as ht
#import connect

class control:
    def __init__(self):
        self.h_t = ht.hand()
        self.click_finger = 1
        self.i = 0


    def check_geture(self):
        self.click()
        self.h_t.hand_track_draw()

    def click(self):
        self.diff_x = self.h_t.fingers[0].x - self.h_t.fingers[1].x
        self.diff_y = self.h_t.fingers[0].y - self.h_t.fingers[1].y



        if self.diff_x<0.03 and self.diff_y<0.03 and self.click_finger <= 1 and self.diff_x != 0:
            self.click_finger = 10
            self.i = self.i + 1
            print("Click ", self.i)
            #connect.send()
        else:
            self.click_finger = self.click_finger -1





