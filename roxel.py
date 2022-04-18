""" Module containing the Roxel class """

import numpy as np

class Roxel:
    """ Class for a rotating picture element, which represents a rotating line
    in 2D space """
    def __init__(self, x, y, radius, phase_rads, rotations_per_second):
        """ Initialise a rotating picture element, given the x- and
        y-coordinates of its centre, its radius, phase, and rotational velocity
        in rotations per second """
        self._x = x
        self._y = y
        self._radius = radius
        self._phase_rads = phase_rads
        self._rads_per_second = 2 * np.pi * rotations_per_second

    def get_end_points(self, t):
        """ Return the endpoints at time t seconds of the line that this Roxel
        instance represents """
        # Calculate the current angle with the x-axis of the line that this
        # Roxel instance represents
        theta = self._phase_rads + (self._rads_per_second * t)
        # Calculate and return the end-points of the line
        r_sin_theta = self._radius * np.sin(theta)
        r_cos_theta = self._radius * np.cos(theta)
        x1 = self._x + r_cos_theta
        y1 = self._y + r_sin_theta
        x2 = self._x - r_cos_theta
        y2 = self._y - r_sin_theta
        return x1, y1, x2, y2
