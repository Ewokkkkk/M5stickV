import image
import lcd
lcd.init()
img = image.Image("/flash/startup.jpg")
lcd.display(img)
