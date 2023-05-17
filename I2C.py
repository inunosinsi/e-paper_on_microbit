from microbit import *
#import time
#import smbus
##import RPi.GPIO as GPIO
#import os

# Pin definition
RST_PIN         = pin0
BUSY_PIN        = pin1

# address com:60 data:61
adds_com        = 0x3C
adds_data       = 0x3D

# adds_com        = 0x3E
# adds_data       = 0x3F

#iic = smbus.SMBus(1)

def digital_write(pin, value):
    pin.write_digital(pin, value)

def digital_read(pin):
    return pin.read_digital(pin)

def delay_ms(delaytime):
    sleep(delaytime)

def IIC_writebyte_com(value):
    i2c.write(adds_com, value)

def IIC_writeblock_com(register, values):
	# 文字列をまとめて書き込む
    #iic.write_block_data(adds_com, register, values)

def IIC_writebyte_data(value):
    iic.write_byte(adds_data, value)

def IIC_writeblock_data(register, values):
	# 文字列をまとめて書き込む
    #iic.write_block_data(adds_data, register, values)
    
#def IIC_Readbyte_com(register):
#    while(1):
#        try:
#            iic.write_byte(adds_com, register)
#            x = iic.read_byte(adds_com)
#            if(x != None):
#                return x
#        except :
#            pass
    
#def IIC_Readbyte_data(register):
#    while(1):
#        try:
#            iic.write_byte(adds_data, register)
#            x = iic.read_byte(adds_data)
#            if(x != None):
#                return x
#        except :
#            pass

def module_Init():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(RST_PIN, GPIO.OUT)
    #GPIO.setup(BUSY_PIN, GPIO.IN) 
    #GPIO.output(RST_PIN, 0)
	i2c.init()
    return 0
    
def module_exit():
    #iic.close()
	RST_PIN.write_digital(o)
    #GPIO.output(RST_PIN, 0)


