class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    
    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item)
    

pt1 = Point(1, 2)
pt2 = Point(10, 20)

a = pt1.x