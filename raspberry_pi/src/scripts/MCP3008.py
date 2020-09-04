from spidev import SpiDev

class MCP3008:
    def __init__(self, bus, device, max_speed_hz = 1000000):
        self.bus = bus
        self.device = device
        self.spi = SpiDev()
        self.open()
        self.spi.max_speed_hz = max_speed_hz

    def open(self, max_speed_hz = 1000000):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = max_speed_hz 
    
    def read(self, channel):
        cmd1 = 4 | 2 | (( channel & 4) >> 2)
        cmd2 = (channel & 3) << 6

        adc = self.spi.xfer2([cmd1, cmd2, 0])
        data = ((adc[1] & 15) << 8) + adc[2]
        return data
            
    def close(self):
        self.spi.close()
