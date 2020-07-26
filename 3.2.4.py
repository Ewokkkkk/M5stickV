import image
import lcd

lcd.init()
img = image.Image()
img.draw_string(10, 10, "hello world!", lcd.BLUE, scale = 2.5)
lcd.display(img)
