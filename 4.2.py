# Untitled - By: ew - 金 7 24 2020

import sensor, image, time, lcd
from fpioa_manager import *
from Maix import GPIO

fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)
but_a=GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
but_b=GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)

while(True):
    img = sensor.snapshot()
    if but_a.value() == 0:
        filename = "_".join(map(str, time.localtime()))
        img.save("/flash/" + filename + ".jpg")
        img2 = image.Image()
        img2.draw_string((lcd.width()-4*16)//2, lcd.height()//2-8, "Save", scale=2)
        lcd.display(img2)
        #time.sleep(2)
        time.sleep(.1)
    else:
        lcd.display(img)
