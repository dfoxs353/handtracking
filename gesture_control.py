import handtrakcer as ht
#from pynput.mouse import Button, Controller
import connect

class control:
    last_x = 0
    last_y = 0
    current_x = 0
    current_y = 0
    scroll_x = 0
    scroll_y = 0

    def __init__(self):
        self.h_t = ht.hand()
        self.scroll_mouse = 1
        #self.mouse = Controller()


    def check_geture(self):

        self.get_coord()
        self.h_t.hand_track_draw()
        self.calculate_coord()
        self.check_scroll()
        #self.scroll()

    def get_coord(self):
        pass



    def calculate_coord(self):
        self.diff_x = abs(self.h_t.fingers[4].x - self.h_t.fingers[8].x)
        self.diff_y = abs(self.h_t.fingers[4].y - self.h_t.fingers[8].y)

        self.scroll_x = self.current_x - self.last_x
        self.scroll_y = self.current_y - self.last_y


    def check_scroll(self):

        if self.diff_x < 0.07 and self.diff_y < 0.07:
            self.scroll_mouse = self.scroll_mouse + 1

            if self.scroll_mouse == 5:
                connect.send()
                self.last_x = self.current_x
                self.last_y = self.current_y
                print("yes")

        else:
            self.scroll_mouse = 0



    def scroll(self):
        self.current_x = self.h_t.fingers[8].x
        self.current_y = self.h_t.fingers[8].y
        if self.scroll_mouse > 1 and abs(self.current_x - self.last_x) > 0.009:



            if self.current_x - self.last_x >0:
                self.mouse.scroll(0, -1)
            else:
                self.mouse.scroll(0, 1)






