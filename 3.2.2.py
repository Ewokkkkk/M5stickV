import lcd

lcd.init()
s = "ABC"
lcd.draw_string((lcd.width()-len(s)*8)//2, lcd.height()//2-4, s, lcd.RED, lcd.BLACK)
