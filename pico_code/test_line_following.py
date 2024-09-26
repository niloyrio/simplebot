from machine import Pin
import time

# black tape = high (1), brighter surface = low (0)
l, r = Pin(9, Pin.PULL_DOWN), Pin(11, Pin.PULL_DOWN)

values = [0, 0]

while True:
    _l = l.value()
    if _l != values[0]:
        print("9 (left) became", _a)
        values[0] = _l

    _r = r.value()
    if _r != values[1]:
        print("11 (right) became", _b)
        values[1] = _r
        
    time.sleep(0.1)

#line following test
m = Motor(3, 4, 6)
n = Motor(12, 7, 10)        
bot = SimpleBot(m, n)
#while True:
#     if _r and _l:
#         bot.reverse(30)
#     elif _l:
#         bot.ccw(30)
#     elif _r:
#         bot.cw(30)
#     else:
#         bot.forward(30)
#     time.sleep(0.1)