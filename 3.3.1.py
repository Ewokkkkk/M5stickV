import lcd
import time
from Maix import GPIO
from fpioa_manager import *

fm.register(board_info.LED_W, fm.fpioa.GPIO3)
fm.register(board_info.LED_R, fm.fpioa.GPIO4)
fm.register(board_info.LED_G, fm.fpioa.GPIO5)
fm.register(board_info.LED_B, fm.fpioa.GPIO6)

led_w = GPIO(GPIO.GPIO3, GPIO.OUT)
led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)
led_b = GPIO(GPIO.GPIO6, GPIO.OUT)

lcd.init()
lcd.draw_string(10, 10, "led", lcd.RED, lcd.BLACK)

while True:
    led_b.value(0)
    time.sleep_ms(400)
    led_b.value(1)
    time.sleep_ms(400)
    led_g.value(0)
    time.sleep_ms(400)
    led_g.value(1)
    time.sleep_ms(400)
    led_r.value(0)
    time.sleep_ms(400)
    led_r.value(1)
    time.sleep_ms(400)
    led_w.value(0)
    time.sleep_ms(400)
    led_w.value(1)
    time.sleep_ms(400)
