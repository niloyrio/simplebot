from machine import Pin

a, b = Pin(14, Pin.IN), Pin(15, Pin.IN)

values = [0, 0]
counts = [0, 0]
ticks = 0
while True:
    _a = a.value()
    if _a != values[0]:
        #print("14 became", _a)
        values[0] = _a
        counts[0] += 1

    _b = b.value()
    if _b != values[1]:
        #print("15 became", _b)
        values[1] = _b
        counts[1] += 1
    
    ticks += 1
    if ticks == 100000:
        print(counts)
        ticks = 0