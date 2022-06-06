require 'pi_piper'
require "i2c"
require "i2c/driver/i2c-dev"

class AQM0802A
  include PiPiper

  COLUMN = 8
  ROW = 2

  SLAVE_ADDRESS = 0x3e

  GPIO_RST = 17
  GPIO_LED = 4
  GPIO_SCL = 3
  GPIO_SDA = 2

  CMD_INIT = [0x38, 0x39, 0x14, 0x70, 0x56, 0x6c]
  CMD_CLEAR = [0x38, 0x0d, 0x01]
  CMD_RETURN = [0x00, 0xc0]

  def initialize()
    @device = I2CDevice.new(address: SLAVE_ADDRESS, driver: I2CDevice::Driver::I2CDev.new("/dev/i2c-1"))
    @pin_led = PiPiper::Pin.new(pin: GPIO_LED,  direction: :out)
    init()
  end

  def init()
    i2cset(CMD_INIT)
  end

  def clear()
    i2cset(CMD_CLEAR)
  end

  def turn_on_backlight()
    @pin_led.on
  end

  def turn_off_backlight()
    @pin_led.off
  end

  def message(upper_row, lower_row="")
    if upper_row.length > COLUMN
      raise Exception
    end

    if !lower_row.nil? && lower_row.length > COLUMN
      raise Exception
    end

    @device.i2cset(upper_row.bytes)
    @device.i2cset(CMD_RETURN)
    @device.i2cset(lower_row.bytes)

  end

  def i2cset(data)
    @device.i2cset(data.unpack("C*"))
  end

end
