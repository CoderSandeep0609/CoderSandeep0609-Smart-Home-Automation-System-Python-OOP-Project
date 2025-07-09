from abc import ABC, abstractmethod

class Device(ABC):
    '''----- device_id  would be unique for all device'''
    __id=None
    location=None
    __status=None

    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod 
    def turn_off(self):
        pass
    def get_status(self):
        pass



class Notifier(ABC):
    @abstractmethod
    def notify(self,message):
        pass




