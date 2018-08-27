import time
#from pygame import mixer # Load the required library
import pygame
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
chan_list = [7,11]    # add as many channels as you want!
                       # you can tuples instead i.e.:
                       #   chan_list = (11,12)
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP) # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/



pygame.init()

pygame.mixer.init()

def playSound(path):
#    pygame.mixer.music.stop()
#    pygame.mixer.music.load(path)
    print(path)
#    pygame.mixer.music.play()

try:
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    for pin in chan_list:
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=playSound, bouncetime=200)  # add rising edge detection on a channel

        while 1:
            time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
