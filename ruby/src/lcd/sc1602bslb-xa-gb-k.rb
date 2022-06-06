#https://www.slideshare.net/catmoney/siersierraspberry-pi4-l
require pi_piper

class GPIO
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
end

class SC1602
  include PiPiper

  DISPLAY_ROWS = 2
  DISPLAY_COLS = 16

  @pin = {
      VDD: GPIO.PW_5V_1
    , VSS: PIO.GND_2
    , VO : None
    , RS : Pin.new(pin:GPIO.GPIO_7, direction: :out)
    , R/W: Pin.new(pin:GPIO.GPIO_17, direction: :out)
    , E  : Pin.new(pin:GPIO.GND_5, direction: :out)
    , DB0: None
    , DB1: None
    , DB2: None
    , DB3: None
    , DB4: Pin.new(pin:GPIO.GPIO_27, direction: :out)
    , DB5: Pin.new(pin:GPIO.GPIO_22, direction: :out)
    , DB6: Pin.new(pin:GPIO.GPIO_5, direction: :out)
    , DB7: Pin.new(pin:GPIO.GPIO_6, direction: :out)
  }

  def initialize()

  end

  def message(text)
    text.each_char do | c |
      ord(c)
  end
  end
end