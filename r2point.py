from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    # Лежит ли точка внутри первого квадранта?
    def is_inside_quadrant(self, b):
        return [self.x >= 0, self.y >= 0, b.x >= 0, b.y >= 0]

    # "Перемещаем" точку в первый квадрант
    @staticmethod
    def to_quadrant(first, second, inside_quadrant):
        # Если точка лежит в первом квадранте возвращаем её же
        if all(inside_quadrant):
            return first
        x = first.x - second.x
        y = first.y - second.y
        # Ордината точки прямой, проходящей через две данные и x = 0
        y1 = (-second.x) * y / x + second.y if x != 0 else -1
        point1 = R2Point(0, y1)
        # Абсцисса точки прямой, проходящей через две данные и y = 0
        x2 = (-second.y) * x / y + second.x if y != 0 else -1
        point2 = R2Point(x2, 0)
        if x2 <= 0 and y1 <= 0:
            return R2Point(0, 0)
        if (x2 > 0 and y1 < 0) or (first.y < 0 and (second.y < 0 or
        first.x >= second.x)):
            return point2
        if (y1 > 0 and x2 < 0) or (first.x < 0 and (second.x < 0 or
        first.y >= second.y)):
            return point1

    # Расстояние в первом квадранте
    def new_dist(self, b, inside_quadrant):
        point1 = R2Point.to_quadrant(self, b, inside_quadrant[:2])
        point2 = R2Point.to_quadrant(b, self, inside_quadrant[2:])
        return R2Point.dist(point1, point2)

    # Расстояние в первом квадранте
    def dist_inside_quadrant(self, b):
        inside_quadrant = self.is_inside_quadrant(b)
        if all(inside_quadrant):
            return self.dist(b)
        else:
            return self.new_dist(b, inside_quadrant)


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
    print(R2Point.area(a, c, b))
