import smbus
import time
 
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
 
DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for inputs
 
# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE,IODIRA,0x80)
 
# Set output all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATA,0)

while True:
  for MyData in range(8):
    # Count from 1 to 8 which in binary will count
    # from 001 to 111
    bus.write_byte_data(DEVICE,OLATA,MyData)
#    print("{0:08b}".format(MyData))
    time.sleep(0.001)
    MySwitch = bus.read_byte_data(DEVICE,GPIOA)
    if MySwitch & MySwitch == 0b10000000:
       print "Switch was pressed!"
    time.sleep(0.01)
 
# Set all bits to zero
bus.write_byte_data(DEVICE,OLATA,0)
