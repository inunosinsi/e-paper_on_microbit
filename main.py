from microbit import *
import epd1in9
import IIC

DSPNUM_WB = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # black
DSPNUM_WW = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]  # white
DSPNUM_WB = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # All black font
DSPNUM_W0 = [0x00, 0xbf, 0x1f, 0xbf, 0x1f, 0xbf, 0x1f, 0xbf, 0x1f, 0xbf, 0x1f, 0xbf, 0x1f, 0x00, 0x00]  # 0
DSPNUM_W1 = [0xff, 0x1f, 0x00, 0x1f, 0x00, 0x1f, 0x00, 0x1f, 0x00, 0x1f, 0x00, 0x1f, 0x00, 0x00, 0x00]  # 1
DSPNUM_W2 = [0x00, 0xfd, 0x17, 0xfd, 0x17, 0xfd, 0x17, 0xfd, 0x17, 0xfd, 0x17, 0xfd, 0x37, 0x00, 0x00]  # 2
DSPNUM_W3 = [0x00, 0xf5, 0x1f, 0xf5, 0x1f, 0xf5, 0x1f, 0xf5, 0x1f, 0xf5, 0x1f, 0xf5, 0x1f, 0x00, 0x00]  # 3
DSPNUM_W4 = [0x00, 0x47, 0x1f, 0x47, 0x1f, 0x47, 0x1f, 0x47, 0x1f, 0x47, 0x1f, 0x47, 0x3f, 0x00, 0x00]  # 4
DSPNUM_W5 = [0x00, 0xf7, 0x1d, 0xf7, 0x1d, 0xf7, 0x1d, 0xf7, 0x1d, 0xf7, 0x1d, 0xf7, 0x1d, 0x00, 0x00]  # 5
DSPNUM_W6 = [0x00, 0xff, 0x1d, 0xff, 0x1d, 0xff, 0x1d, 0xff, 0x1d, 0xff, 0x1d, 0xff, 0x3d, 0x00, 0x00]  # 6
DSPNUM_W7 = [0x00, 0x21, 0x1f, 0x21, 0x1f, 0x21, 0x1f, 0x21, 0x1f, 0x21, 0x1f, 0x21, 0x1f, 0x00, 0x00]  # 7
DSPNUM_W8 = [0x00, 0xff, 0x1f, 0xff, 0x1f, 0xff, 0x1f, 0xff, 0x1f, 0xff, 0x1f, 0xff, 0x3f, 0x00, 0x00]  # 8
DSPNUM_W9 = [0x00, 0xf7, 0x1f, 0xf7, 0x1f, 0xf7, 0x1f, 0xf7, 0x1f, 0xf7, 0x1f, 0xf7, 0x1f, 0x00, 0x00]  # 9

number_0 = [0xbf, 0x1f]
number_1 = [0x1f, 0x00]
number_2 = [0xfd, 0x17]
number_3 = [0xf5, 0x1f]
number_4 = [0x47, 0x1f]
number_5 = [0xf7, 0x1d]
number_6 = [0xff, 0x1d]
number_7 = [0x21, 0x1f]
number_8 = [0xff, 0x1f]
number_9 = [0xf7, 0x1f]
number = [[0xbf, 0x1f], [0x1f, 0x00], [0xfd, 0x17], [0xf5, 0x1f], [0x47, 0x1f], [0xf7, 0x1d], [0xff, 0x1d], [0x21, 0x1f], [0xff, 0x1f], [0xf7, 0x1f]]
radix_point = 0x20
degree_centigrad = 0x05
Fahrenheit_degree = 0x06
BLE = 0x08
POW = 0x10
First_black = 0x1f
First_white = 0x00

try:
    print("epd1in9 Demo")
    
    epd = epd1in9.EPD()
    print("init and Clear")
    
    epd.init()
    
    epd.lut_5S()
    print("1111")
    epd.Write_Screen(DSPNUM_WW)
    
    sleep(500)
    
    epd.lut_GC()
    epd.Write_Screen1(DSPNUM_WB)
    sleep(500)
    epd.Write_Screen(DSPNUM_WW)
    sleep(500)

    epd.lut_DU_WB()
    sleep(500)
    epd.Write_Screen(DSPNUM_W0);
    sleep(500)
    epd.Write_Screen(DSPNUM_W1);
    sleep(500)
	epd.Write_Screen(DSPNUM_W2);
    sleep(500)
    epd.Write_Screen(DSPNUM_W3);
    sleep(500)
	epd.Write_Screen(DSPNUM_W4);
    sleep(500)
    epd.Write_Screen(DSPNUM_W5);
    sleep(500)
    epd.Write_Screen(DSPNUM_W6);
    sleep(500)
    epd.Write_Screen(DSPNUM_W7);
    sleep(500)
    epd.Write_Screen(DSPNUM_W8);
    sleep(500)
    epd.Write_Screen(DSPNUM_W9);
    sleep(500)
    epd.Write_Screen(DSPNUM_WB)
    sleep(500)
	
    epd.sleep()
    
except KeyboardInterrupt: 
    print("BBBB")
    print("ctrl + c:")
    IIC.module_exit()
    exit()