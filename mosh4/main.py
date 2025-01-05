class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw(self):
        print(f"Point x: ({self.x}), Point y: ({self.y})")

point = Point.zero()
point.draw()