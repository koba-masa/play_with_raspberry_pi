require 'sensor/pressure/mf02a'

#SLEEP_SECOND = 600
SLEEP_SECOND = 10


def main(pin)
  sensor = PiPiper::Pin.new(pin: pin,  direction: :in、trigger: :both)

  attendance = False
  punch_in_time = nil
  punch_out_time = nil

  loop do
    if sensor.on?
      attendance = True

    elsif

    else
      attendance = False

      punch_in_time = nil
      punch_out_time = nil
    end

  end
end

def record(punch_in_time, punch_out_time)
