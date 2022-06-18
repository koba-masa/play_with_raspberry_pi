import socket
import time

import RPi.GPIO as GPIO

from device.aqm0802a import AQM0802A

class DisplayIPAddress:
  def __init__(self):
    self.is_finish = False
    # 終了スイッチ
    self.finish_switch = 27

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.finish_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  def execute(self):
    GPIO.add_event_detect(self.finish_switch, GPIO.FALLING, callback=self.to_be_finish, bouncetime=300)

    lcd = AQM0802A()

    try:
      while True:
        my_ip_address = self.ip_address()
        lcd.display_upper(my_ip_address[0] + '.' + my_ip_address[1] + '.')
        lcd.display_lower(my_ip_address[2] + '.' + my_ip_address[3])

        if self.is_finish:
          break
        time.sleep(5)
    except Exception as e:
      print(e)
    finally:
      GPIO.remove_event_detect(self.finish_switch)
      GPIO.cleanup(self.finish_switch)
      lcd.reset()
      lcd.turn_off_display()

  def to_be_finish(self, gpio_pin):
    self.is_finish = True

  def ip_address(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0].split('.')

DisplayIPAddress().execute()
