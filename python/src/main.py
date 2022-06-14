import RPi.GPIO as GPIO

import time

  def __init__(self):
    # 測定中のランプ
    self.processed_lamp = 26
    # 開始ボタン
    self.start_btn = 19
    # 終了ボタン
    self.finish_btn = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.processed_lamp, GPIO.OUT)
    GPIO.setup(self.start_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(self.finish_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  def execute(self):
    GPIO.add_event_detect(self.start_btn, GPIO.FALLING, callback=self.start, bouncetime=300)
    GPIO.add_event_detect(self.finish_btn, GPIO.FALLING, callback=self.finish, bouncetime=300)

    try:
      while True:
        time.sleep(1)
    except Exception as e:
      print(e)
    finally:
      print("end")
      GPIO.cleanup(self.processed_lamp)
      GPIO.remove_event_detect(self.start_btn)
      GPIO.cleanup(self.start_btn)
      GPIO.remove_event_detect(self.finish_btn)
      GPIO.cleanup(self.finish_btn)

  def start(self):
    GPIO.output(self.processed_lamp, GPIO.HIGH)

  def finish(self):
    GPIO.output(self.processed_lamp, GPIO.LOW)

Koyanagi().execute()
