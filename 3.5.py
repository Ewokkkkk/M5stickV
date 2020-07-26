import lcd, time, audio
from Maix import I2S, GPIO
from fpioa_manager import *

lcd.init()
fm.register(board_info.SPK_SD, fm.fpioa.GPIO0)
spk_sd = GPIO(GPIO.GPIO0, GPIO.OUT)
spk_sd.value(1)
fm.register(board_info.SPK_DIN, fm.fpioa.I2S0_OUT_D1)
fm.register(board_info.SPK_BCLK, fm.fpioa.I2S0_SCLK)
fm.register(board_info.SPK_LRCLK, fm.fpioa.I2S0_WS)

wav_dev = I2S(I2S.DEVICE_0)

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
            lcd.draw_string(10, 10, "SOUND", lcd.RED, lcd.BLACK)
        player.finish()
    except:
        lcd.draw_string(10, 10, "ERROR", lcd.RED, lcd.BLACK)

play_sound("/flash/ding.wav")
