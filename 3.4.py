import lcd
from fpioa_manager import *
from Maix import GPIO

lcd.init()
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)
but_a=GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
but_b=GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

while True:
    if but_a.value() == 0:
        lcd.draw_string(10, 10, "Button A", lcd.WHITE, lcd.RED)
    elif but_b.value() == 0:
        lcd.draw_string(10, 10, "Button B", lcd.WHITE, lcd.BLUE)
    else:
        lcd.clear()
