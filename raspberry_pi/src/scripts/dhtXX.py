import sys
import Adafruit_DHT


class DhtXX(object):
    def __init__(self, model_number, pin):
        self.model_number = model_number
        self.pin = pin
        
    def get_values(self):
        humidity, temperature = Adafruit_DHT.read_retry(
            self.model_number, self.pin
        )
        return {
            'humidity': humidity,
            'temperature': temperature
        }