# util.py Demo pogram for rendering arbitrary fonts to an SSD1306 OLED display.

# The MIT License (MIT)
#
# Copyright (c) 2016 Peter Hinch
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# https://learn.adafruit.com/monochrome-oled-breakouts/wiring-128x32-spi-oled-display
# https://www.proto-pic.co.uk/monochrome-128x32-oled-graphic-display.html

# V0.22 Dec 23rd 2017 machine.SPI now only seems to work soft SPI and I2C
# implmentations
# Now provides demo of simple graphics

import machine
import utime
from .ssd1306 import SSD1306_I2C
from .writer import Writer

# Fonts
from . import freesans20
#import freeserif19
#import inconsolata16

WIDTH = const(128)
HEIGHT = const(64)

pscl = machine.Pin(4, machine.Pin.OUT)
psda = machine.Pin(5, machine.Pin.OUT)
i2c = machine.I2C(scl=pscl, sda=psda)
ssd = SSD1306_I2C(WIDTH, HEIGHT, i2c, 0x3c)

def printLines(line1, line2):
    ssd.fill(0)
    ssd.show()
    utime.sleep(0.5)
    wri = Writer(ssd, freesans20, verbose=False)
    Writer.set_clip(True, True)
    Writer.set_textpos(0, 0)
    wri.printstring(line1)
    wri.printstring('\n')
    wri.printstring(line2)
    ssd.show()

def test():

    rhs = WIDTH -1
    ssd.line(rhs - 20, 0, rhs, 20, 1)
    square_side = 10
    ssd.fill_rect(rhs - square_side, 0, square_side, square_side, 1)

    #wri = Writer(ssd, freeserif19)
    wri2 = Writer(ssd, freesans20, verbose=False)
    Writer.set_clip(True, True)
    Writer.set_textpos(0, 0)
    wri2.printstring('Samstag\n')
    wri2.printstring('30 Dez 2017\n')
    wri2.printstring('Hallo')
    ssd.show()

