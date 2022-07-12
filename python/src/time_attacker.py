import RPi.GPIO as GPIO

import time
import math

from device.aqm0802a import AQM0802A
from device.ssd1306 import SSD1306

class TimeAttacker:
  def __init__(self):
    # 測定中のランプ
    self.processed_lamp = 19
    # 開始ボタン
    self.start_btn = 26
    # 終了ボタン
    self.finish_btn = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.processed_lamp, GPIO.OUT)
    GPIO.setup(self.start_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(self.finish_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  def execute(self):
    GPIO.add_event_detect(self.start_btn, GPIO.FALLING, callback=self.start, bouncetime=300)
    GPIO.add_event_detect(self.finish_btn, GPIO.FALLING, callback=self.finish, bouncetime=300)
    GPIO.output(self.processed_lamp, GPIO.LOW)

    self.display = SSD1306(0x3c, 128, 64)
    #self.display.light_on()

    try:
      while True:
        time.sleep(100000000)
    except Exception as e:
      print(e)
    finally:
      #self.display.light_off()
      GPIO.cleanup(self.processed_lamp)
      GPIO.remove_event_detect(self.start_btn)
      GPIO.cleanup(self.start_btn)
      GPIO.remove_event_detect(self.finish_btn)
      GPIO.cleanup(self.finish_btn)
      #self.display.turn_off_display()
      self.display.reset()

  def start(self, gpio):
    if GPIO.input(self.processed_lamp) == 0:
      print("start")
      self.display.reset()
      #self.display.display_upper('start')
      self.start = time.perf_counter()
      self.turn_on_off_led(GPIO.HIGH)

  def finish(self, gpio):
    if GPIO.input(self.processed_lamp) == 1:
      print("finish")
      self.display.reset()
      self.end = time.perf_counter()
      attack_time = self.calculate(self.start, self.end)
      print(attack_time)
      self.write(attack_time)
      self.turn_on_off_led(GPIO.LOW)
      self.reset()

  def write(self, attack_time):
    self.display.write(format(attack_time, '.1f') + '  Sec')

  def reset(self):
    self.start = 0
    self.end = 0

  def turn_on_off_led(self, up_down):
    GPIO.output(self.processed_lamp, up_down)

  def calculate(self, start_time, end_time):
    return end_time - start_time

TimeAttacker().execute()
