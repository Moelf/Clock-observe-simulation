__author__ = 'ex'
from Tkinter import *
import math


def rgb_to_web(n):
    return '#%02x%02x%02x' % tuple(n) #RGB convert to web color
#wavelengthto RGB: http://rohanhill.com/tools/WaveToRGB/index.asp?
#                  http://www.midnightkite.com/color.html


def wav2rgb(wavelength):
    w = int(wavelength)

    # colour
    if w >= 380 and w < 440:
        R = -(w - 440.) / (440. - 350.)
        G = 0.0
        B = 1.0
    elif w >= 440 and w < 490:
        R = 0.0
        G = (w - 440.) / (490. - 440.)
        B = 1.0
    elif w >= 490 and w < 510:
        R = 0.0
        G = 1.0
        B = -(w - 510.) / (510. - 490.)
    elif w >= 510 and w < 580:
        R = (w - 510.) / (580. - 510.)
        G = 1.0
        B = 0.0
    elif w >= 580 and w < 645:
        R = 1.0
        G = -(w - 645.) / (645. - 580.)
        B = 0.0
    elif w >= 645 and w <= 780:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    # intensity correction
    if w >= 380 and w < 420:
        SSS = 0.3 + 0.7*(w - 350) / (420 - 350)
    elif w >= 420 and w <= 700:
        SSS = 1.0
    elif w > 700 and w <= 780:
        SSS = 0.3 + 0.7*(780 - w) / (780 - 700)
    else:
        SSS = 0.0
    SSS *= 255
    return [int(SSS*R), int(SSS*G), int(SSS*B)]


def resize(ev=NONE):
    clocklabel1.config(font='Helvetica -%d bold' % scale.get())
    clocklabel2.config(font='Helvetica -%d bold' % scale.get())


def dopplerperiod(period,v):
    return period/(1.0-v/100.0)


def relat_dopplerperiod(period,v):
    return dopplerperiod(period,v)/math.sqrt(1.0-(v/100.0)**2)


for i in range(-99,99):
    print i,1000.0*100/(100+i)