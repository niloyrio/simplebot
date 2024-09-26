from motor import Motor
from bot import SimpleBot

m = Motor(3, 4, 6)
n = Motor(12, 7, 10)        
bot = SimpleBot(m, n)

# act entertaining
import time
from random import randint, choice

def shiver():
    bot.cw(80)
    time.sleep(0.5)
    bot.ccw(80)
    time.sleep(0.5)
    bot.stop()
    
def lurch():
    bot.forward(100)
    time.sleep(1.5)
    bot.stop()
    
def spin():
    r = randint(0, 1)
    if r:
        bot.cw(100)
    else:
        bot.ccw(100)
    time.sleep(randint(15, 25) / 10)
    bot.stop()
    
def swerve():
    for i in range(randint(2, 4)):
        duration = randint(3, 6)
        bot.left.forward(randint(40, 60))
        bot.right.forward(randint(40, 60))
        time.sleep(duration)
    bot.stop()

def circle():
    bot.left.forward(randint(30, 70))
    bot.right.forward(randint(30, 70))
    time.sleep(5.0)
    
# while True:
#     time.sleep(6.0)
#     choice([shiver, lurch, spin, swerve, circle])()