from math import sqrt


class Vec:
    """
    A 2D vector. It is immutable, so you can put it in a set or as a key in a dict.
    """
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

# Basic getters  ---------------------------------------------------------------------------------------------------
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def get(self):
        """ Returns a tuple (x, y) """
        return self.__x, self.__y

# Operators  -------------------------------------------------------------------------------------------------------
    def __add__(self, other):
        return Vec(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Vec(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec(self.__x * other, self.__y * other)
        elif isinstance(other, Vec):
            return Vec(self.__x * other.__x, self.__y * other.__y)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec(self.__x / other, self.__y / other)
        elif isinstance(other, Vec):
            return Vec(self.__x / other.__x, self.__y / other.__y)

    def __floordiv__(self, other):
        if isinstance(other, int):
            return Vec(int(self.__x // other), int(self.__y // other))
        elif isinstance(other, Vec):
            return Vec(self.__x // other.__x, self.__y // other.__y)

    def __neg__(self):
        return Vec(-self.__x, -self.__y)

    def __pos__(self):
        return Vec(*self.get())

    def __str__(self):
        return f"vec({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# standard functionalities  ---------------------------------------------------------------------------------------
    def norm(self):
        """ The euclidian norm of the vector """
        return sqrt(self.__x ** 2 + self.__y ** 2)

    def normalize(self):
        """ Same direction, but with a norm of one """
        return self.__truediv__(self.norm())

    def neg_x(self):
        """ A vector with the coordinate x inverted """
        return Vec(-self.__x, self.__y)

    def neg_y(self):
        """ A vector with the coordinate y inverted """
        return Vec(self.__x, -self.__y)

    def to_int(self):
        """ A vector with x and y values truncated """
        return Vec(int(self.__x), int(self.__y))

    def rotate90_clockwise(self):
        return Vec(-self.__y, self.__x)

    def rotate90_anticlockwise(self):
        return -self.rotate90_clockwise()

    def at_his_right(self, v):
        """
        Returns if v is pointing to his right
        For example, (1, 0)(RIGHT) is pointing to the right of (0, -1)(UP)
        and (-1, 0)(LEFT) is pointing to the right of (0, 1)(DOWN)

        If v points at the same direction or in the opposite direction, it will return False
        """
        return dot(self.rotate90_clockwise(), v) > 0

    def project(self, axe, starting_pos=None):
        """ Returns the t value in the equation `starting_pos` + t * `axe` = projected_point """
        v = self
        if starting_pos is not None:
            v = self - starting_pos
        return dot(v, axe)

    def __hash__(self):
        return hash((self.__x, self.__y))


# Helping functions between vectors ------------------------------------------------------------------------------------
def dist(v1, v2):
    dx = (v1.x - v2.x)
    dy = (v1.y - v2.y)
    return sqrt(dx*dx+dy*dy)


def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y


# Useful vectors -------------------------------------------------------------------------------------------------------
UP = Vec(0, -1)
DOWN = Vec(0, 1)
RIGHT = Vec(1, 0)
LEFT = Vec(-1, 0)
