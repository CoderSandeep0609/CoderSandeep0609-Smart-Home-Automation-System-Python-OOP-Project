class DeviceRegistrationError(Exception):
    def __init__(self,message='Fan registration error'):
        self.message=message
    def __str__(self):
        return self.message

class FanSpeedError(Exception):
    def __init__(self,message='Fan speed invalid'):
        self.message=message
    def __str__(self):
        return self.message

class ACTemperatueError(Exception):
    def __init__(self,message='Temperatue failure'):
        self.message=message
    def __str__(self):
        return self.message

class LightBrightnessError(Exception):
    def __init__(self,message='Brightness invalid'):
        self.message=message
    def __str__(self):
        return self.message

class RoomRegestrationError(Exception):
    def __init__(self,message='invalid data'):
        self.message=message
    def __str__(self):
        return self.message

class DuplicateDeviceError(Exception):
    def __init__(self,message='Data already avail'):
        self.message=message
    def __str__(self):
        return self.message

class ValueNotFoundError(Exception):
    def __init__(self,message='value not found'):
        self.message=message
    def __str__(self):
        return self.message