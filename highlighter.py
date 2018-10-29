#!/usr/bin/env python

from PIL import Image
import sys
import random

from helpers.rgbcmp import rgbcmp

blu = (0, 0, 255, 255)
tolerance = 30

img = Image.open(sys.argv[1])
w, h = img.width, img.height
bmap = img.load()

fuzz = (random.choice(range(0, w)), random.choice(range(0, h)))
c = bmap[fuzz]

def N(xy):
    x, y = xy
    if y > 0:
        return (x, y - 1)

def S(xy):
    x, y = xy
    if y < h - 1:
        return (x, y + 1)

def E(xy):
    x, y = xy
    if x < w - 1:
        return (x + 1, y)

def W(xy):
    x, y = xy
    if x > 0:
        return (x - 1, y)

def floodfill(xy):
    frontier = [xy]

    while(frontier):
        xy = frontier.pop()
        bmap[xy] = blu

        for ab in (N(xy), S(xy), E(xy), W(xy)):
            # Check for image and fill area boundaries.
            if ab != None and rgbcmp(bmap[ab], c) <= tolerance:
                frontier.append(ab)

floodfill(fuzz)
img.save(sys.argv[2])

# vim: ts=4: sts=4: sw=4:
