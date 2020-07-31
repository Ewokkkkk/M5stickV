import sensor, image, time, lcd, audio, uos
from fpioa_manager import *
from Maix import GPIO, I2S

fm.register(board_info.BUTTON_A, fm.fpioa.GPIO1)
fm.register(board_info.BUTTON_B, fm.fpioa.GPIO2)
but_a=GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
but_b=GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

fm.register(board_info.SPK_SD, fm.fpioa.GPIO0)
spk_sd = GPIO(GPIO.GPIO0, GPIO.OUT)
spk_sd.value(1)
fm.register(board_info.SPK_DIN, fm.fpioa.I2S0_OUT_D1)
fm.register(board_info.SPK_BCLK, fm.fpioa.I2S0_SCLK)
fm.register(board_info.SPK_LRCLK, fm.fpioa.I2S0_WS)
wav_dev = I2S(I2S.DEVICE_0)

ALLOWED_EXTENSION = ('bmp', 'pgm', 'ppm', 'jpg', 'jpeg')

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)

def play_sound(filename):
    try:
        player = audio.Audio(path = filename)
        player.volume(50)
        wav_info = player.play_process(wav_dev)
        wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER, resolution = I2S.RESOLUTION_16_BIT, align_mode = I2S.STANDARD_MODE)
        wav_dev.set_sample_rate(wav_info[1])
        while True:
            ret = player.play()
            if ret == None:
                break
            elif ret == 0:
                break
        player.finish()
    except:
        lcd.draw_string(10, 10, "ERROR", lcd.RED, lcd.BLACK)

def shooting_mode():
    time.sleep(.2)
    lcd.clear()

    while(True):
        img = sensor.snapshot()
        if but_a.value() == 0:
            filename = "_".join(map(str, time.localtime()))
            img.save("/flash/" + filename + ".jpg")
            play_sound("/flash/Shutter.wav")
            lcd.display(img)
            time.sleep(3)
        else:
            lcd.display(img)
        if but_b.value() == 0:
            preview_mode()

def preview_mode():
    time.sleep(.2)
    lcd.clear()

    files = []
    for f in uos.listdir("/flash/"):
        ext = f.rsplit('.', 1)[1]
        if ext in ALLOWED_EXTENSION:
        #if ext == "jpg":
            files.append(f)


    while(True):
        for file in files:
            while(True):
                lcd.display(image.Image(file))
                lcd.draw_string(10, 10, str((files.index(file) + 1)) + "/" + str(len(files)), lcd.WHITE, lcd.BLACK)

                if but_a.value() == 0:
                    time.sleep(.2)
                    break

                if but_b.value() == 0:
                    shooting_mode()

shooting_mode()



