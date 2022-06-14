import RPi.GPIO
from gpio import GPIO

import time

class Koyanagi:
    def __init__(self):
        # 測定中のランプ
        self.processed_lamp = GPIO.GPIO_26
        # 開始ボタン
        self.start_btn = GPIO.GPIO_19

        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(self.processed_lamp, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.start_btn, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

    def execute(self):
        while true:
            RPi.GPIO.output(self.processed_lamp, 1)
            time.sleep(1)
            RPi.GPIO.output(self.processed_lamp, 0)
            time.sleep(1)

    def __del__(self):
        RPi.GPIO.cleanup(self.processed_lamp)
        RPi.GPIO.cleanup(self.start_btn)


Koyanagi().execute()
