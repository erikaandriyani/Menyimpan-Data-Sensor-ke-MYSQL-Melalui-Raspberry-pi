import smbus
import time

DEVICE = 0X23
POWER_DOWN = 0X00
POWER_ON = 0X01
RESET = 0X07

CONTINUOUS_LOW_RES_MODE = 0X13
CONTINUOUS_HIGH_RES_MODE_1 = 0X10
CONTINUOUS_HIGH_RES_MODE_2 = 0X11
ONE_TIME_HIGH_RES_MODE_1 = 0X20
ONE_TIME_HIGH_RES_MODE_2 = 0X21
ONE_TIME_LOW_RES_MODE = 0X23

bus = smbus.SMBus (0)
bus = smbus.SMBus (1)

def convertToNumber(data):
	result = (data[1]+(256*data[0]))/1.2
	return (result)
def readLight(addr=DEVICE):
	data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
	return convertToNumber(data)
def main():
	while True:
	lightLevel=readLight()
	print("Light Level : " + format(lightLevel,'.2f') + "1x")
	time.sleep(0.5)
if __name__=="__main__":
	main()
