""" Module containing classes for different shapes """

class Square:
    """ Class representing a square """
    def __init__(self, x_centre, y_centre, length):
        """ Initialise a square, given the location of its centre and length of
        its sides """
        half_length = length / 2
        self._x_left    = x_centre - half_length
        self._x_right   = x_centre + half_length
        self._y_bottom  = y_centre - half_length
        self._y_top     = y_centre + half_length

    def is_inside_square(self, x, y):
        """ Return a Boolean representing if the point (x, y) is inside the
        square represented by this instance of Square """
        in_square = all([
            x > self._x_left,
            x < self._x_right,
            y > self._y_bottom,
            y < self._y_top,
        ])
        return in_square
