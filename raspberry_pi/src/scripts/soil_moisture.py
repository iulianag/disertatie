from src.scripts.MCP3008 import MCP3008

class SoilMoisture(object):
    def __init__(self, bus, device, channel):
        self.channel = channel
        self.mcp = MCP3008(bus, device)
        
    def get_values(self):
        value = self.mcp.read(self.channel)
        return {'soil_moisture': value}
    
    def close(self):
        self.mcp.close()

    