#!/usr/bin/python3
# -*- coding:UTF-8 -*-
# Code at github.com/llvllch/doomed 
# Oct' 21

#--------------Driver Library-----------------#
import RPi.GPIO as GPIO
import OLED_Driver as OLED
#--------------Image Library---------------#
from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
#--------------Data Grabber and other---------------#
import urllib, json
import requests
import random
import os
import glob
import time
#-------------Display Functions---------------#

dirname = os.path.dirname(__file__)
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
fontdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts')

def Display_Picture(File_Name, score):
    image = Image.open(File_Name)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(os.path.join(fontdir,'RobotoCondensed-Bold.ttf'),22)
    draw.text((102, 106), str(score), fill = "WHITE", font = font)
    angle = 180
    image = image.rotate(angle, expand=True)
    OLED.Display_Image(image)


def getindex(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        fearjson=requests.get(url, headers=headers).json()
        print(fearjson)
        data= fearjson['data']
        score=data[0]['value']
        time_until_update= data[0]['time_until_update']
# Derive the level from the score... a simple division into 5 levels
        level = int(score) // 20 + 1
    except:
        score=""
        level=5
        time_until_update='69'
    return score, level, time_until_update
    
#----------------------MAIN-------------------------#
try:

    def main():
    
        #-------------OLED Init------------#
        OLED.Device_Init()
        Display_Picture(os.path.join(picdir, "wake1.jpg"),"")
        OLED.Delay(2000)
        Display_Picture(os.path.join(picdir, "wake2.jpg"),"")
        OLED.Delay(2000)
        lastfetch = time.time()
        url='https://api.alternative.me/fng/'
        score, level, tui =getindex(url)
        while (True):
            numberchoices=len(glob.glob(os.path.join(picdir, "picture"+str(level)+"-*.jpg")))
            print(numberchoices)
            randompic = random.randint(1,numberchoices)
            filename = os.path.join(picdir, "picture"+str(level)+"-"+str(randompic)+".jpg")
            Display_Picture(filename,score)
            OLED.Delay(random.randint(10000,100000))
            if (time.time() - lastfetch > int(tui)):
                score, level, tui =getindex(url)
                lastfetch=time.time()


    if __name__ == '__main__':
        main()

except:
    print("\r\nInterrupted, End")
    OLED.Clear_Screen()
    GPIO.cleanup()


