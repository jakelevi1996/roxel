""" Module containing the Roxel class """

class Roxel:
    """ Class for a rotating picture element """
    def __init__(self, x, y, radius, phase_init, rotations_per_second):
        self._x = x
        self._y = y
        self._radius = radius
        self._phase_init = phase_init
        self._rotations_per_second = rotations_per_second

