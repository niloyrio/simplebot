from machine import Pin
import time
from motor import Motor
from bot import SimpleBot

# black tape = high (1), brighter surface = low (0)
l, r = Pin(9, Pin.PULL_DOWN), Pin(11, Pin.PULL_DOWN)

values = [0, 0]

m = Motor(3, 4, 6)
n = Motor(12, 7, 10)        
bot = SimpleBot(m, n)
while True:
    _l = l.value()
    _r = r.value()
    if _r and _l:
        bot.reverse(30)
    elif _l:
        bot.ccw(30)
    elif _r:
        bot.cw(30)
    else:
        bot.forward(30)
    time.sleep(0.05)
