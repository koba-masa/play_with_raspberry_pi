# https://akizukidenshi.com/catalog/g/gI-15752/

from gpio import GPIO

class A_574SR_LF:
  NUMBERS = [
    [1, 1, 1, 1, 1, 1, 0], # 0
    [0, 1, 1, 0, 0, 0, 0], # 1
    [1 ,1 ,0 ,1 ,1 ,0 ,1], # 2
    [1, 1, 1, 1, 0, 0, 1], # 3
    [0, 1, 1, 0, 0, 1, 1], # 4
    [1, 0, 1, 1, 0, 1, 1], # 5
    [1, 0, 1, 1, 1, 1, 1], # 6
    [1, 1, 1, 0, 0, 1, 0], # 7
    [1, 1, 1, 1, 1, 1, 1], # 8
    [1, 1, 1, 1, 0, 1, 1], # 9
  ]

  # PIN01, PIN02, PIN03, PIN04, PIN05, PIN06,
  # PIN07, PIN08, PIN09, PIN10, PIN11, PIN12
  def __init__(self,
    PIN12, PIN11, PIN10, PIN09, PIN08, PIN07,
    PIN06, PIN05, PIN04, PIN03, PIN02, PIN01
  ):
    # 1桁目(12), 2桁目(9), 3桁目(8), 4桁目(6)
    self.digit_pins = [PIN12, PIN09, PIN08, PIN06]
    # A(11), B(7), C(4), D(2), E(1), F(10), G(5)
    self.segment_pins = [PIN11, PIN07, PIN04, PIN02, PIN01, PIN10, PIN05]
    self.dot_pin = PIN03
    self.setup()

  def setup(self):
    GPIO.set_mode_borad()
    [GPIO.setup_out(pin) for pin in self.digit_pins]
    [GPIO.setup_out(pin) for pin in self.segment_pins]
    GPIO.setup_out(self.dot_pin)

  def display(self, digit, contents, dot=False):
    GPIO.output_high(self.digit_pins[digit])
    for i in range(7):
      GPIO.output(self.segment_pins[i], self.reverse(contents[i]))
    GPIO.output(self.dot_pin, self.reverse(1 if dot else 0))
    GPIO.output_low(self.digit_pins[digit])

  def clear(self):
    for i in range(7):
        GPIO.output(self.segment_pins[i], 0)
    GPIO.output(self.dot_pin, self.reverse(0))


  def cleanup(self):
    [GPIO.cleanup(pin) for pin in self.digit_pins]
    [GPIO.cleanup(pin) for pin in self.segment_pins]
    GPIO.cleanup(self.dot_pin)

  def reverse(self, value):
    return 0 if value == 1 else 1
