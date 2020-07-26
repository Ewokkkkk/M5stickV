import lcd
from fpioa_manager import *
from Maix import GPIO

lcd.init()
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
btn_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)


while True:
    if btn_a.value() == 0:
        if led_r.value() == 0:
            led_r.value(1)
            time.sleep(.25)
        else:
            led_r.value(0)
            time.sleep(.25)
