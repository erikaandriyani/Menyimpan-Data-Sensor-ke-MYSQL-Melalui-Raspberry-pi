import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

#Create an ADS1115 object
ads = ADS.ADS1115(i2c)

#DEfine the analog input channel
channel = AnalogIn(ads, ADS.P0)

#Loop to read the analog input continuosly
while True:
    temp = round((5.0 * (1-channel.voltage) * 10000.0) / 1024, 2)
    print("Suhu: ", temp, "oc")
    time.sleep(0.2)