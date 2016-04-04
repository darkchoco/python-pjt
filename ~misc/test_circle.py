__author__ = 'ihchon'


class Circle1:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, new_value):
        if new_value >= 0:
            self.__radius = new_value
        else:
            raise ValueError("Value must be positive")

    def area(self):
        return 3.14159 * (self.__radius ** 2)


class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    def __set_radius(self, new_value):
        if new_value >= 0:
            self.__radius = new_value
        else:
            raise ValueError("Value must be positive")

    # read, write, delete, documentation 순서
    radius = property(None, __set_radius)

    @property
    def area(self):
        return 3.14159 * (self.__radius ** 2)
