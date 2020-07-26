# Untitled - By: ew - 金 7 24 2020

import sensor, image, time, lcd

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

while(True):
    img = sensor.snapshot()
    lcd.display(img)
    lcd.draw_string(10, 10, "Camera", lcd.WHITE, lcd.GREEN)
