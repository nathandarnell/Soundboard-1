import time
#from pygame import mixer # Load the required library
import pygame
import os
import RPi.GPIO as GPIO

# https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
# https://raspi.tv/2014/rpi-gpio-update-and-detecting-both-rising-and-falling-edges
GPIO.setmode(GPIO.BOARD)
gpio_list = [7,11]    # Pins to poll https://pinout.xyz/pinout/pin11_gpio17
GPIO.setup(gpio_list, GPIO.IN, pull_up_down=GPIO.PUD_UP) # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

dir_path = os.path.dirname(os.path.realpath(__file__)) #https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory

pygame.init()
pygame.mixer.init()

def getPath(pin):
    pin = str(pin) # https://www.crybit.com/convert-integer-string-python/

# Check for the right extension, mp3 first https://stackoverflow.com/questions/33400682/check-if-a-directory-contains-a-file-with-a-given-extension

    pinMP3 = pin + ".mp3";
    pinWAV = pin + ".wav";

    # One of many options: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists
    if os.path.exists(pinMP3):
        print ("pinMP3 is here!")
        pin += '.mp3'
    elif:
        print ("WAV is here!")
        pin += '.wav'
    else:
        print ("MP3 or WAV is missing!")
        return

# Play the sound
    playSound(pin)

def playSound(path):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    print(path)
    pygame.mixer.music.play()

try:
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    for pin in gpio_list:
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=getPath, bouncetime=200)  # add rising edge detection on a channel

    while 1:
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
