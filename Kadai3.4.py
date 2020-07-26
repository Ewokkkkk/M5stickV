import lcd
from fpioa_manager import *
from Maix import GPIO

lcd.init()
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)

btn_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

leds = [led_r, led_g, led_b]

for l in leds:
    l.value(1)

i = 0
while True:
    if btn_b.value() == 0:
        leds[i].value(1)
        i = (i + 1) % 3
        leds[i].value(0)

    time.sleep_ms(200)

    #lcd.draw_string(10, 10, str(led_r.value()) + str(led_g.value()) + str(led_b.value()), lcd.WHITE, lcd.RED)
