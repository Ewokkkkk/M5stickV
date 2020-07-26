import image
import lcd
lcd.init()
img = image.Image("/flash/test.jpg")
lcd.display(img)
lcd.draw_string(10, 10, "STRING", lcd.RED, lcd.BLACK)
