from machine import Pin, PWM

class Motor:
    def __init__(self, pwm_pin, in1_pin, in2_pin):
        self.pwm = PWM(Pin(pwm_pin), freq=50, duty_u16=8192)
        self.pwm.duty_u16(0) # 0%
        self.dir_pins = (Pin(in1_pin, Pin.OUT), Pin(in2_pin, Pin.OUT))
        
    def forward(self, speed=None):
        self.dir_pins[0].value(0)
        self.dir_pins[1].value(1)
        if speed: self.speed(speed)
        
    def reverse(self, speed=None):
        self.dir_pins[1].value(0)
        self.dir_pins[0].value(1)
        if speed: self.speed(speed)
        
    def stop(self):
        self.dir_pins[0].value(0)
        self.dir_pins[1].value(0)
    
    def speed(self, percent):
        self.pwm.duty_u16(int((percent/100) * 65535)) # 0%