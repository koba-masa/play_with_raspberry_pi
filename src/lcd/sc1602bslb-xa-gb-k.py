import Adafruit_CharLCD as LCD
import socket

#import common.gpio

class Lcd:
  DISPLAY_ROWS = 2
  DISPLAY_COLS = 16
  PIN = {
      "VDD": Gpio.PW_5V_1
    , "VSS": Gpio.GND_2
    , "VO" : None
    , "RS" : Gpio.GPIO_7
    , "R/W": Gpio.GPIO_17
    , "E"  : Gpio.GND_5
    , "DB0": None
    , "DB1": None
    , "DB2": None
    , "DB3": None
    , "DB4": Gpio.GPIO_27
    , "DB5": Gpio.GPIO_22
    , "DB6": Gpio.GPIO_5
    , "DB7": Gpio.GPIO_6
  }

  def __init__(self):
    self.lcd = LCD.Adafruit_CharLCD(
        self.PIN["RS"]
      , self.PIN["E"]
      , self.PIN["DB4"]
      , self.PIN["DB5"]
      , self.PIN["DB6"]
      , self.PIN["DB7"]
      , self.DISPLAY_COLS
      , self.DISPLAY_ROWS
    )

  def main(self):
    self.lcd.clear()
    self.lcd.blink(False)
    self.lcd.show_cursor(False)

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    self.lcd.message(ip)

class Gpio:
  PW_3V_1 = 1
  PW_5V_1 = 2
  GPIO_2  = 3
  PW_5V_2 = 4
  GPIO_3  = 5
  GND_1   = 6
  GPIO_4  = 7
  GPIO_14 = 8
  GND_2   = 9
  GPIO_15 = 10
  GPIO_17 = 11
  GPIO_18 = 12
  GPIO_27 = 13
  GND_3   = 14
  GPIO_22 = 15
  GPIO_23 = 16
  PW_3V_2 = 17
  GPIO_24 = 18
  GPIO_10 = 19
  GND_4   = 20
  GPIO_9  = 21
  GPIO_25 = 22
  GPIO_11 = 23
  GPIO_8  = 24
  GND_5   = 15
  GPIO_7  = 26
  ID_SD   = 27
  ID_SC   = 28
  GPIO_5  = 29
  GND_6   = 30
  GPIO_6  = 31
  GPIO_12 = 32
  GPIO_13 = 33
  GND_6   = 34
  GPIO_19 = 35
  GPIO_16 = 36
  GPIO_26 = 37
  GPIO_20 = 38
  GND_7   = 39
  GPIO_21 = 40
