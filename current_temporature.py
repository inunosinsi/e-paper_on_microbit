from microbit import *

RST_PIN  = pin0
BUSY_PIN = pin1

ADDS_COM        = 0x3C #60
ADDS_DATA       = 0x3D #61

# micro:bit function temperature sensor.
VAR_Temperature = temperature()

class EPD:
    def reset(self):
        RST_PIN.write_digital(1)
        sleep(200)
        RST_PIN.write_digital(0)
        sleep(20)
        RST_PIN.write_digital(1)
        sleep(200) 

    def send_command(self, i):
        i2c.write(ADDS_COM, bytes([i]))
        sleep(1)

    def send_data(self, i):
        i2c.write(ADDS_DATA, bytes([i]))
        sleep(1)
                
    def ReadBusy(self):
        while(BUSY_PIN.read_digital() == 0):      # 0: idle, 1: busy
            sleep(1)
        sleep(10)
            
    
    # DU waveform white extinction diagram + black out diagram
    # Bureau of brush waveform
    def lut_DU_WB(self):
        self.send_command(0x82)
        self.send_command(0x80)
        self.send_command(0x00)
        self.send_command(0xC0)
        self.send_command(0x80)
        self.send_command(0x80)
        self.send_command(0x62) 
       
    # GC waveform
    # The brush waveform
    def lut_GC(self):
        self.send_command(0x82)
        self.send_command(0x20)
        self.send_command(0x00)
        self.send_command(0xA0)
        self.send_command(0x80)
        self.send_command(0x40)
        self.send_command(0x63)
       
    # 5 waveform  better ghosting
    # Boot waveform
    def lut_5S(self):
        self.send_command(0x82)
        self.send_command(0x28)
        self.send_command(0x20)
        self.send_command(0xA8)
        self.send_command(0xA0)
        self.send_command(0x50)
        self.send_command(0x65) 
            
     # temperature measurement
    # You are advised to periodically measure the temperature and modify the driver parameters
    # If an external temperature sensor is available, use an external temperature sensor
    def Temperature(self):
        if ( VAR_Temperature < 10 ):
            self.send_command(0x7E)
            self.send_command(0x81)
            self.send_command(0xB4)
        else: 
            self.send_command(0x7b)
            self.send_command(0x81)
            self.send_command(0xB4) 
        
        self.ReadBusy()        
        self.send_command(0xe7)    # Set default frame time
        
        # Set default frame time
        if (VAR_Temperature<5):
            self.send_command(0x31) # 0x31  (49+1)*20ms=1000ms
        elif (VAR_Temperature<10):
            self.send_command(0x22) # 0x22  (34+1)*20ms=700ms
        elif (VAR_Temperature<15):
            self.send_command(0x18) # 0x18  (24+1)*20ms=500ms
        elif (VAR_Temperature<20):
            self.send_command(0x13) # 0x13  (19+1)*20ms=400ms
        else:
            self.send_command(0x0e) # 0x0e  (14+1)*20ms=300ms
                            
    # Note that the size and frame rate of V0 need to be set during initialization, 
    # otherwise the local brush will not be displayed
    def init(self):
        i2c.init()
        
        self.reset()
        
        self.send_command(0x2B) # POWER_ON
        sleep(10)
        self.send_command(0xA7) # boost
        self.send_command(0xE0) # TSON 
        sleep(10)
        self.Temperature()
        
    def Write_Screen(self, image):
        self.send_command(0xAC) # Close the sleep
        self.send_command(0x2B) # turn on the power
        self.send_command(0x40) # Write RAM address
        self.send_command(0xA9) # Turn on the first SRAM
        self.send_command(0xA8) # Shut down the first SRAM
        
        for j in range(0, 15):
            self.send_data(image[j])
        
        self.send_data(0x00)
        self.send_command(0xAB) # Turn on the second SRAM
        self.send_command(0xAA) # Shut down the second SRAM
        self.send_command(0xAF) # display on
        self.ReadBusy()
        # IIC.delay_ms(2000)
        self.send_command(0xAE) # display off
        self.send_command(0x28) # HV OFF
        self.send_command(0xAD) # sleep in	
        
       
    def Write_Screen1(self, image):
        self.send_command(0xAC) # Close the sleep
        self.send_command(0x2B) # turn on the power
        self.send_command(0x40) # Write RAM address
        self.send_command(0xA9) # Turn on the first SRAM
        self.send_command(0xA8) # Shut down the first SRAM
        
        for j in range(0, 15):
            self.send_data(image[j])
            
        self.send_data(0x03)
        
        self.send_command(0xAB) # Turn on the second SRAM
        self.send_command(0xAA) # Shut down the second SRAM
        self.send_command(0xAF) # display on
        self.ReadBusy()
        # IIC.delay_ms(2000)
        self.send_command(0xAE) # display off
        self.send_command(0x28) # HV OFF
        self.send_command(0xAD) # sleep in	
        
    def sleep(self):
        self.send_command(0x28) # POWER_OFF
        self.ReadBusy()
        self.send_command(0xAC) # DEEP_SLEEP
        
        sleep(2000)
        RST_PIN.write_digital(0)

DSPNUM_WB = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # black
DSPNUM_WW = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]  # white

number = [
    [0xbf, 0x1f],  # 0
    [0x1f, 0x00],  # 1
    [0xfd, 0x17],  # 2
    [0xf5, 0x1f],  # 3
    [0x47, 0x1f],  # 4
    [0xf7, 0x1d],  # 5
    [0xff, 0x1d],  # 6
    [0x21, 0x1f],  # 7
    [0xff, 0x1f],  # 8
    [0xf7, 0x1f]   # 9
]

radix_point = 0x20
degree_centigrad = 0x05
Fahrenheit_degree = 0x06
BLE = 0x08
POW = 0x10
First_black = 0x1f
First_white = 0x00

counter = 0

def divide_number(i):
    l = []
    tens = ""
    if i >= 10:
        tens = str(i)[0]
        ones = str(i)[1]
    else:
        ones = str(i)[0]
    
    if len(tens) > 0:
        l = number[int(tens)]
    else:
        l = [0x00, 0x00]
    
    n = number[int(ones)]
    l.append(n[0])
    l.append(n[1])
    return l
    
print("epd1in9 Demo")
    
epd = EPD()
print("init and Clear")
    
epd.init()

epd.lut_5S()
epd.Write_Screen(DSPNUM_WW)

sleep(500)

epd.lut_GC()
epd.Write_Screen1(DSPNUM_WB)
#sleep(500)
epd.Write_Screen(DSPNUM_WW)
sleep(500)

#epd.lut_DU_WB()
#sleep(500)
while True:
    tmpList = divide_number(VAR_Temperature)
    # current temporature 
    epd.Write_Screen([
        0x00, 
        tmpList[0], 
        tmpList[1], 
        tmpList[2], 
        tmpList[3], 
        0x00, 
        0x00, 
        0x00, 
        0x00, 
        0x00, 
        0x00, 
        0x00, 
        0x00, 
        0xff, 
        0x00
    ])
    sleep(1000*5)

#epd.sleep()
