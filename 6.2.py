import sensor, image, lcd
import KPU as kpu

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.run(1)

task = kpu.load(0x200000)   #   フラッシュメモリに組み込まれた学習モデル(0x200000番地)を読み込む
img2 = image.Image()

while(True):
    img = sensor.snapshot()             #   カメラから画像取得
    tmp_img=img.to_grayscale(1)         #   グレースケールに変換
    tmp_img=tmp_img.resize(28, 28)      #   サイズを28x28に
    tmp_img.invert()                    #   白黒反転
    tmp_img.strech_char(1)              #   データの前処理
    tmp_img.pix_to_ai()                 #   AIデータに変換
    fmap=kpu.forward(task, tmp_img)     #   数字の認識
    plist=fmap[:]                       #   結果（確率）を取り出す
    pmax=max(plist)                     #   最も確率が高いものを答えとする
    max_index=plist.index(pmax)         #   答えの数字
    x = img.width() // 2
    tmp_img=tmp_img.resize(x, x)
    img2.clear()
    img2.draw_image(tmp_img, 0, 22)
    img2.draw_string(2, 2, str(max_index), scale=2)
    img2.draw_image(img.resize(x, img.height()//2), x, 22)
    lcd.display(img2)
kpu.deinit(task)
