#!/usr/bin/env python

from math import sqrt, pow

def rgbcmp(c1, c2):
    return sqrt(
        pow(c2[0] - c1[0], 2) +
        pow(c2[1] - c1[1], 2) +
        pow(c2[2] - c1[2], 2))

# vim: ts=4: sts=4: sw=4:
