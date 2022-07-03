import RPi.GPIO as GPIO
import smbus
import time
import subprocess

class AQM0802A:
  SLAVE_ADDRESS = 0x3e
  CLEAR = 0x01
  COMMAND=0x00
  DATA = 0x40
  LOWER_ADDRESS = 0x40+0x80
  DISPLAY_ON = 0x0c
  DISPLAY_OFF = 0x08

  HOME=0x02

  LIGHT = 4

  def __init__(self):
    self.i2c = smbus.SMBus(1)
    self.setup()
    self.turn_on_display()
    self.reset()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.LIGHT, GPIO.OUT)
    self.light_off()

  def setup(self):
    self.__command(0x38)
    self.__command(0x39)
    self.__command(0x14)
    self.__command(0x70)
    self.__command(0x56)
    self.__command(0x6c)
    time.sleep(0.2)
    self.__command(0x38)

  def turn_on_display(self):
    self.__command(self.DISPLAY_ON)

  def turn_off_display(self):
    self.__command(self.DISPLAY_OFF)

  def light_on(self):
    GPIO.output(self.LIGHT, GPIO.HIGH)

  def light_off(self):
    GPIO.output(self.LIGHT, GPIO.LOW)

  def reset(self):
    self.__command(self.CLEAR)

  def display_upper(self, message):
    self.__command(self.HOME)
    self.__write(message)

  def display_lower(self, message):
    self.__command(self.LOWER_ADDRESS)
    self.__write(message)

  def __write(self, message):
    chars = []
    for char in message:
      chars.append(ord(char))
    self.i2c.write_i2c_block_data(self.SLAVE_ADDRESS, self.DATA, chars)

  def __command(self, command):
    self.i2c.write_byte_data(self.SLAVE_ADDRESS, self.COMMAND, command)
