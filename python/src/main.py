import RPi.GPIO as GPIO

import time
import random

class Main:
  def __init__(self):
    self.start_btn = 18
    self.yellow_lamp = 23
    self.blue_lamp = 24
    self.green_lamp = 25
    self.red_lamp = 12

    self.lamps = [self.blue_lamp, self.green_lamp, self.red_lamp]

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.start_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(self.yellow_lamp, GPIO.OUT)
    GPIO.setup(self.red_lamp, GPIO.OUT)
    GPIO.setup(self.green_lamp, GPIO.OUT)
    GPIO.setup(self.blue_lamp, GPIO.OUT)

  def execute(self):
    GPIO.output(self.yellow_lamp, GPIO.LOW)
    GPIO.output(self.red_lamp, GPIO.LOW)
    GPIO.output(self.green_lamp, GPIO.LOW)
    GPIO.output(self.blue_lamp, GPIO.LOW)
    GPIO.add_event_detect(self.start_btn, GPIO.FALLING, callback=self.start, bouncetime=300)

    try:
      while True:
        time.sleep(1)
    except Exception as e:
      print(e)
    finally:
      GPIO.cleanup(self.red_lamp)
      GPIO.cleanup(self.green_lamp)
      GPIO.cleanup(self.blue_lamp)
      GPIO.cleanup(self.yellow_lamp)
      GPIO.remove_event_detect(self.start_btn)
      GPIO.cleanup(self.start_btn)

  def start(self, bin):
    for num in range(5):
      self.led_on_off(self.red_lamp)
      self.led_on_off(self.green_lamp)
      self.led_on_off(self.blue_lamp)

    lamp = random.choice(self.lamps)
    GPIO.output(lamp, GPIO.HIGH)
    if not lamp == self.red_lamp and random.choice([True, False]):
      GPIO.output(self.yellow_lamp, GPIO.HIGH)

    time.sleep(5)
    GPIO.output(lamp, GPIO.LOW)
    GPIO.output(self.yellow_lamp, GPIO.LOW)

  def led_on_off(self, pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)

Main().execute()
