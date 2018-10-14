#!/usr/bin/env python

from PIL import Image
import sys
import random

sys.setrecursionlimit(1000000)

blu = (0, 0, 255, 255)

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
    if bmap[xy] != c:
        return

    bmap[xy] = blu

    for ab in (N(xy), S(xy), E(xy), W(xy)):
        if ab != None:
            floodfill(ab)
    return

floodfill(fuzz)
img.save(sys.argv[2])

# vim: ts=4: sts=4: sw=4:
