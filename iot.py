import serial
from serial import Serial#Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com4',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

for i in range(2):
    incoming = str(ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)

    if 'high' in incoming:
        pyautogui.dragRel(-50, 0, duration=1)
    if 'low' in incoming:
        pyautogui.dragRel(50, 0, duration=0.1)
        pyautogui.dragRel(0, -50, duration=0.1)
        pyautogui.dragRel(-50, 0, duration=0.1)
        pyautogui.dragRel(50, 0, duration=0.1)
        pyautogui.dragRel(0, -50, duration=0.1)
        pyautogui.dragRel(-50, 0, duration=0.1)
        # 3 written
        pyautogui.moveRel(100, 0, duration=0.1)

        pyautogui.dragRel(50, 0, duration=0.1)
        pyautogui.dragRel(0, 100, duration=0.1)
        pyautogui.dragRel(-50, 0, duration=0.1)
        pyautogui.dragRel(0, -100, duration=0.1)
        # 0 written
        time.sleep(1)

    for j in range(10):
        pyautogui.hotkey('ctrl', 'z')
        
    incoming = "";
