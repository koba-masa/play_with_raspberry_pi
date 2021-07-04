require 'socket'
require 'i2c/device/aqm0802'

SLEEP_SECOND = 3600

def main()
  lcd = nil
  loop do
    begin
      if lcd.nil?
        lcd = I2CDevice::AQM0802A.new
        lcd.initialize_lcd()
      end
      my_ipaddress = get_my_ipaddress
      lcd.clear()
      lcd.put_line(0, "#{my_ipaddress[0]}.#{my_ipaddress[1]}.")
      lcd.put_line(1, "#{my_ipaddress[2]}.#{my_ipaddress[3]}")
      sleep SLEEP_SECOND
    rescue => exception
      lcd = nil
      sleep 60
      next
    end
  end
end

def get_my_ipaddress()
  udp = UDPSocket.new
  udp.connect("128.0.0.0", 7)
  my_ipaddress = Socket.unpack_sockaddr_in(udp.getsockname)[1]
  udp.close
  my_ipaddress.split(".", 0)
end

main()
