from math import floor, sqrt


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_leg(self, point1, point2):
        if point1 == 0 and point2 == 0:
            return 0
        elif point1 == point2:
            return point1
        elif (point1 > 0 and point2 > 0) or (point1 < 0 and point2 < 0):
            return max([abs(point1), abs(point2)]) - min([abs(point1), abs(point2)])
        elif (point1 > 0 > point2) or (point1 < 0 < point2):
            return abs(point1) + abs(point2)

    def length_line(self):
        length_a = self.get_leg(self.x1, self.x2)
        length_b = self.get_leg(self.y1, self.y2)
        length = sqrt(length_a**2 + length_b**2)
        return length

    def closer_to_center(self):
        x1y1 = sqrt(abs(self.x1)**2 + abs(self.y1)**2)
        x2y2 = sqrt(abs(self.x2)**2 + abs(self.y2)**2)
        if x1y1 <= x2y2:
            return self.x1
        else:
            return self.x2

    def formatted_line(self):
        if self.closer_to_center() == self.x1:
            return f"({floor(self.x1)}, {floor(self.y1)})({floor(self.x2)}, {floor(self.y2)})"
        else:
            return f"({floor(self.x2)}, {floor(self.y2)})({floor(self.x1)}, {floor(self.y1)})"


x1_inp = float(input())
y1_inp = float(input())
x2_inp = float(input())
y2_inp = float(input())

line1 = Line(x1_inp, y1_inp, x2_inp, y2_inp)

x1_inp = float(input())
y1_inp = float(input())
x2_inp = float(input())
y2_inp = float(input())

line2 = Line(x1_inp, y1_inp, x2_inp, y2_inp)

if line1.length_line() >= line2.length_line():
    print(line1.formatted_line())
else:
    print(line2.formatted_line())
