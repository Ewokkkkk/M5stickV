import sensor, image, lcd, time
import KPU as kpu

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))

classes = ['', 'coin', 'lipcream', 'pencil']
task = kpu.load(0x200000)
img2 = image.Image()

while(True):
    img = sensor.snapshot()
    fmap=kpu.forward(task,img)
    plist=fmap[:]
    pmax=max(plist)
    max_index = 0
    if pmax > 0.7:
        max_index=plist.index(pmax)
    img2.clear()
    img2.draw_string(2, 2, classes[max_index], scale=3)
    img2.draw_image(img.resize(112, 112), 64, 30)
    lcd.display(img2)
    time.sleep_ms(10)
kpu.deinit(task)
