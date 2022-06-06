require 'pi_piper'

class MF02A

  def initialize(pin)
    @sensor = PiPiper::Pin.new(pin: pin,  direction: :in)
  end

  def on?()
    @sensor.on?
  end

  def off?()
    @sensor.off?
  end

  def read()
    pin.read
    @last_value = pin.last_value
    @now_value = pin.value
  end

  def last_value()
    @last_value
  end

  def now_value()
    @now_value
  end
end
