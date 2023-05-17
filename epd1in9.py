from microbit import *
import IIC

RST_PIN = pin0
BUSY_PIN = pin1

class EPD:
    #def __init__(self):
        #self.reset_pin = IIC.RST_PIN
        #self.busy_pin = IIC.BUSY_PIN
        #self.VAR_Temperature = 20
    
    def reset(self):
        RST_PIN.write_digital(1)
        sleep(200)
        RST_PIN.write_digital(0)
        sleep(20)
        RST_PIN.write_digital(1)
        sleep(200) 

    def send_command(self, value):
        IIC.IIC_writebyte_com(value)
        IIC.delay_ms(1)

    def send_data(self, value):
        IIC.IIC_writebyte_data(value)
        IIC.delay_ms(1)
        
    #def read_com(self, register):
        #return IIC.IIC_Readbyte_com(register)
        
    #def read_data(self, register):
        #return IIC.IIC_Readbyte_data(register)
        
    def ReadBusy(self):
        while(IIC.digital_read(self.busy_pin) == 0):      # 0: idle, 1: busy
            IIC.delay_ms(1)
            # self.send_command(0x36)
        IIC.delay_ms(10)    
            
    
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
        if ( self.VAR_Temperature < 10 ):
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
        if (self.VAR_Temperature<5):
            self.send_command(0x31) # 0x31  (49+1)*20ms=1000ms
        elif (self.VAR_Temperature<10):
            self.send_command(0x22) # 0x22  (34+1)*20ms=700ms
        elif (self.VAR_Temperature<15):
            self.send_command(0x18) # 0x18  (24+1)*20ms=500ms
        elif (self.VAR_Temperature<20):
            self.send_command(0x13) # 0x13  (19+1)*20ms=400ms
        else:
            self.send_command(0x0e) # 0x0e  (14+1)*20ms=300ms
                            
    # Note that the size and frame rate of V0 need to be set during initialization, 
    # otherwise the local brush will not be displayed
    def init(self):
        if (IIC.module_Init() != 0):
            return -1
        # EPD hardware init start
        
        self.reset()
        IIC.delay_ms(100)
        
        
        self.send_command(0x2B) # POWER_ON
        IIC.delay_ms(10)
        self.send_command(0xA7) # boost
        self.send_command(0xE0) # TSON 
        IIC.delay_ms(10)
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
        
        IIC.delay_ms(2000)
        IIC.module_exit()
