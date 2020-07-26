import lcd
from fpioa_manager import *
from Maix import GPIO

lcd.init()
fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
btn_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
string = "off"

lcd.draw_string((lcd.width()-len(string)*8)//2, lcd.height()//2-4, string, lcd.WHITE, lcd.BLACK)


while True:
    if btn_a.value() == 0:
        if string == "off":
            string = "on"
            time.sleep(.25)
        else:
            string = "off"
            time.sleep(.25)


        lcd.clear()
        lcd.draw_string((lcd.width()-len(string)*8)//2, lcd.height()//2-4, string, lcd.WHITE, lcd.BLACK)


