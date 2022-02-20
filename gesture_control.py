import handtrakcer as ht
#from pynput.mouse import Button, Controller
# connect

class control:
    last_x = 0

    def __init__(self):
        self.h_t = ht.hand()
        self.scroll_mouse = 1
        self.width, self.height = self.h_t.width, self.h_t.height

        #self.mouse = Controller()


    def check_geture(self):

        self.get_coord()
        self.h_t.hand_track_draw()
        self.calculate_coord()
        self.check_finger_coord()
        #self.scroll()

    def get_coord(self):
        pass



    def calculate_coord(self):
        self.diff_x = abs(self.h_t.fingers[4].x - self.h_t.fingers[8].x)
        self.diff_y = abs(self.h_t.fingers[4].y - self.h_t.fingers[8].y)



    def check_finger_coord(self):
        fin_x = self.h_t.fingers[8].x



        fin_x = round(fin_x * 60)
        if(self.last_x != fin_x):
            self.last_x = fin_x
            if fin_x>=0 and fin_x<60:
                mes = '#' + str(60-fin_x) + ';'
                print(mes)








