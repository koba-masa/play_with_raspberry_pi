# TODO 要理解・要リファクタリング

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

import time

# https://www.amazon.co.jp/dp/B085C67PF1
# https://micropython-docs-ja.readthedocs.io/ja/latest/esp8266/tutorial/ssd1306.html
# https://learn.adafruit.com/monochrome-oled-breakouts/python-setup
class SSD1306:
  def __init__(self, slave_address, vertical_pixcel, horizontal_pixcel):
    self.slave_address = slave_address
    self.vertical_pixcel = vertical_pixcel
    self.horizontal_pixcel = horizontal_pixcel
    self.setup()

  def setup(self):
    self.i2c = busio.I2C(board.SCL, board.SDA)
    self.oled = adafruit_ssd1306.SSD1306_I2C(self.vertical_pixcel, self.horizontal_pixcel, self.i2c, addr=self.slave_address)
    self.clear()
    self.font = ImageFont.load_default()

  def clear(self):
    self.oled.fill(0)
    self.oled.show()

  def write(self, text):
    # https://pillow.readthedocs.io/en/stable/reference/Image.html#constructing-images
    self.image = Image.new('1', (self.oled.width, self.oled.height), 0)
    self.draw = ImageDraw.Draw(self.image)
    font_width, font_height = self.font.getsize(text)
    self.draw.text(
        (self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
        text,
        font=self.font,
        fill=255,
    )
    self.oled.image(self.image)
    self.oled.show()

  def reset(self):
    self.clear()
