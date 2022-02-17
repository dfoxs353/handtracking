class finger:

    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0


    def get_coord(self, x, y):
        self.x, self.y = x, y


    def give_coord(self):
        return self.x, self.y