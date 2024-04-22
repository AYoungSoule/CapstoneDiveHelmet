#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
import time
import traceback
import Adafruit_ADS1x15
import board
import busio
import adafruit_adxl34x
from waveshare_OLED import OLED_1in51
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

try:
    disp1 = OLED_1in51.OLED_1in51_1()
    disp2 = OLED_1in51.OLED_1in51_2()
    disp3 = OLED_1in51.OLED_1in51_3()
    disp4 = OLED_1in51.OLED_1in51_4()
    adc = Adafruit_ADS1x15.ADS1015()
    GAIN = 1
    i2c = busio.I2C(board.SCL, board.SDA)
    accelerometer = adafruit_adxl34x.ADXL345(i2c)
    logging.info("\r1.51inch OLED ")
    # Initialize library.
    disp1.Init()
    disp2.Init()
    disp3.Init()
    disp4.Init()
    # Clear display.
    logging.info("clear display")
    disp1.clear()
    disp2.clear()
    disp3.clear()
    disp4.clear()
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 10)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 8)
    def AscentWarning(Screen, Message):
        image = Image.new('1', (disp4.width, disp4.height), "WHITE")
        draw = ImageDraw.Draw(image)
        draw.line([(0,0),(127,0)], fill = 0)
        draw.line([(0,0),(0,63)], fill = 0)
        draw.line([(0,63),(127,63)], fill = 0)
        draw.line([(127,0),(127,63)], fill = 0)
        draw.text((20,0), Screen, font = font1, fill = 0)
        draw.text((20,24), Message, font = font2, fill = 0)
        
        for i in range(5):
            disp4.clear()
            
            disp4.ShowImage(disp4.getbuffer(image))
            time.sleep(.25)
    # Create blank image for drawing.
    loopend = 1000
    count = 1
    lastAccel = accelerometer.acceleration[2]
    lastTime = time.time()
    for i in range(loopend):
        image1 = Image.new('1', (disp1.width, disp1.height), "WHITE")
        image2 = Image.new('1', (disp2.width, disp2.height), "WHITE")
        image3 = Image.new('1', (disp3.width, disp3.height), "WHITE")
        image4 = Image.new('1', (disp4.width, disp4.height), "WHITE")
        draw1 = ImageDraw.Draw(image1)
        draw2 = ImageDraw.Draw(image2)
        draw3 = ImageDraw.Draw(image3)
        draw4 = ImageDraw.Draw(image4)
        
        logging.info ("***draw line")
        draw1.line([(0,0),(127,0)], fill = 0)
        draw1.line([(0,0),(0,63)], fill = 0)
        draw1.line([(0,63),(127,63)], fill = 0)
        draw1.line([(127,0),(127,63)], fill = 0)
        
        draw2.line([(0,0),(127,0)], fill = 0)
        draw2.line([(0,0),(0,63)], fill = 0)
        draw2.line([(0,63),(127,63)], fill = 0)
        draw2.line([(127,0),(127,63)], fill = 0)
        
        draw3.line([(0,0),(127,0)], fill = 0)
        draw3.line([(0,0),(0,63)], fill = 0)
        draw3.line([(0,63),(127,63)], fill = 0)
        draw3.line([(127,0),(127,63)], fill = 0)
        
        draw4.line([(0,0),(127,0)], fill = 0)
        draw4.line([(0,0),(0,63)], fill = 0)
        draw4.line([(0,63),(127,63)], fill = 0)
        draw4.line([(127,0),(127,63)], fill = 0)
        
        Waterpress = adc.read_adc(0, gain=GAIN) *0.001-0.248
        
        Waterpress = Waterpress * (4.096/231)
        
        Accel = accelerometer.acceleration[2]
        
        DeltaTime = time.time()-lastTime
        DeltaA = (Accel-lastAccel)/DeltaTime
        
        logging.info ("***draw text")
        draw1.text((20,0), 'WaterPressure', font = font1, fill = 0)
        draw1.text((20,24), str(Waterpress), font = font2, fill = 0)
        
        draw2.text((20,0), 'Accelerometer ', font = font1, fill = 0)
        draw2.text((20,24), str(DeltaA), font = font2, fill = 0)
        
        draw3.text((20,0), 'Oxygen Level ', font = font1, fill = 0)
        draw3.text((20,24), str(100*(loopend-count)/loopend) + '%', font = font2, fill = 0)
        
        if DeltaA > 0.1:
             AscentWarning('Warning:', 'Ascending too Quickly')
        else:
            draw4.text((20,0), 'Screen 4 ', font = font1, fill = 0)
            draw4.text((20,24), '<3 <3 <3 ', font = font2, fill = 0)
            disp4.ShowImage(disp4.getbuffer(image4))
        #image1 = image1.rotate(180) 
        
        
        disp1.ShowImage(disp1.getbuffer(image1))
        disp2.ShowImage(disp2.getbuffer(image2))
        disp3.ShowImage(disp3.getbuffer(image3))
        
        time.sleep(1)
        lastAccel = Accel
        count +=1
    
    logging.info ("***draw image")
    Himage1 = Image.new('1', (disp1.width, disp1.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '1in51.bmp'))
    Himage1.paste(bmp, (0,0))
    
    Himage2 = Image.new('1', (disp2.width, disp2.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '1in5b.bmp'))
    Himage2.paste(bmp, (0,0))
    
    Himage3 = Image.new('1', (disp3.width, disp3.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '1in5_rgb.bmp'))
    Himage3.paste(bmp, (0,0))
    
    Himage4 = Image.new('1', (disp4.width, disp4.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '1in5_rgb1.bmp'))
    Himage4.paste(bmp, (0,0))
    #Himage1=Himage1.rotate(180) 	
    disp1.ShowImage(disp1.getbuffer(Himage1)) 
    disp2.ShowImage(disp2.getbuffer(Himage2)) 
    disp3.ShowImage(disp3.getbuffer(Himage3)) 
    disp4.ShowImage(disp4.getbuffer(Himage4)) 
    
    time.sleep(10)    
    disp1.clear()
    disp2.clear()
    disp3.clear()
    disp4.clear()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
