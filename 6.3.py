import sensor, image, lcd
import KPU as kpu

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
task = kpu.load(0x280000)   #   フラッシュメモリに組み込まれた学習モデル(0x280000番地)を読み込む
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)    #   YOLO用設定値
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)   #   YOLOの初期設定
while(True):
    img = sensor.snapshot()                     #   カメラから画像を取得
    code = kpu.run_yolo2(task, img)             #   顔検出
    if code:
        for i in code:                          #   複数の顔を検出できるのでfor文で繰り返し
            img.draw_rectangle(i.rect())        #   顔のまわりに四角を書く
    lcd.display(img)
kpu.deinit(task)
