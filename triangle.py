import math

class Triangle:
    def __init__(self, side1, side2, angle1, angle2):
        self.side1 = side1
        self.side2 = side2
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = 180 - angle1 - angle2
        self.side3 = math.sqrt(side1 ** 2 + side2 ** 2 + 2 * side1 * side2 * math.cos(self.angle3))

    def __str__(self):
        return 'Сторона 1' + str(self.side1)

    def type(self):
        if self.angle1 == 90 or self.angle2 == 90 or self.angle3 == 90:
            return 'Прямоугольный'
        else:
            return'Не прямоугольный'
