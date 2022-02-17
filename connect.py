import serial
import time
Arduino_Serial = serial.Serial('com3', 9600)
time.sleep(2)
def send():
    Arduino_Serial.write('1'.encode())

