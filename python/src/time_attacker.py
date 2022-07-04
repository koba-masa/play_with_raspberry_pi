import RPi.GPIO as GPIO

import time
import math

from device.aqm0802a import AQM0802A

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

    self.lcd = AQM0802A()
    self.lcd.light_on()

    try:
      while True:
        time.sleep(100000000)
    except Exception as e:
      print(e)
    finally:
      self.lcd.light_off()
      GPIO.cleanup(self.processed_lamp)
      GPIO.remove_event_detect(self.start_btn)
      GPIO.cleanup(self.start_btn)
      GPIO.remove_event_detect(self.finish_btn)
      GPIO.cleanup(self.finish_btn)
      self.lcd.turn_off_display()
      self.lcd.reset()

  def start(self, gpio):
    if GPIO.input(self.processed_lamp) == 0:
      print("start")
      self.lcd.reset()
      self.lcd.display_upper('start')
      self.start = time.perf_counter()
      self.turn_on_off_led(GPIO.HIGH)

  def finish(self, gpio):
    if GPIO.input(self.processed_lamp) == 1:
      print("finish")
      self.lcd.reset()
      self.end = time.perf_counter()
      self.attack_time = self.calculate(self.start, self.end)
      self.display(self.attack_time)
      self.turn_on_off_led(GPIO.LOW)
      self.reset()

  def reset(self):
    self.start = 0
    self.end = 0

  def turn_on_off_led(self, up_down):
    GPIO.output(self.processed_lamp, up_down)

  def calculate(self, start_time, end_time):
    # TODO 1/10秒まで計測する
    return math.ceil(end_time - start_time)

  def display(self, contents):
    self.lcd.display_upper(str(contents))
    self.lcd.display_lower('     sec')

TimeAttacker().execute()
