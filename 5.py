import sensor, image, time, lcd

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)

img2 = image.Image()

while(True):
    img = sensor.snapshot()
    res = img.find_qrcodes()
   #res = img.find_barcodes()
    if len(res) > 0:
        img2.clear()
        img2.draw_string(2, 2, res[0].payload())

    img2.draw_image(img, 0, 14)
    lcd.display(img2)
