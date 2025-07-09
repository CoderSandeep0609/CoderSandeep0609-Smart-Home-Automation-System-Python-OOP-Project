from exception import *
from abstraction import *

class Fan(Device):
    def __init__(self,id=None):
        if not id:
            raise DeviceRegistrationError('Value missing for Fan regestration check again-----')
        else:
            self.__id=id
            self.status='OFF'
            self.speed=20

    def get_id(self):
        return self.__id
    
    def turn_on(self):
        self.status='ON'
        print(f'Fan has turned ON and rotating at speed of {self.speed}')

    def speed_change(self,speed):
        if speed >100 or speed<0:
            raise FanSpeedError('Fan speed would be in between 1-100')
        elif speed==0:
            self.status='OFF'
        elif isinstance(speed,int)==False:
            raise ValueError('You have entered correct data for Fan speed')
        else:
            self.speed=speed
            print(f'Fan is spinning at {self.speed} speed....')

    def turn_off(self):
        self.status='OFF'
        print('Fan turned off')

    def get_status(self):
        if self.status=='OFF':
            return f'Fan is {self.status} and spinning at the speed of None'
        return f'Fan is {self.status} and spinning at the speed of {self.speed}'

class AC(Device):
    def __init__(self,id=None):
        if not id:
            raise DeviceRegistrationError('Value missing for AC registration')
        else:
            self.__id=id
            self.status='OFF'
            self.temperature=25

    def temperature(self,temp):
        if temp>35 or temp<5:
            raise ACTemperatueError('Invalid AC temperature--- 5<temperature<35')
        elif isinstance(temp,int)==False:
            raise ValueError('You have to entered correct data for AC temperature')
        else:
            self.temperature=temp
            print(f'Temperature have seted for {self.temperature} Temperature')
    def get_id(self):
        return self.__id
    def turn_on(self):
        self.status='ON'
        print(f'AC turned ON at {self.temperature} temperature')

    def turn_off(self):
        self.status='OFF'
        print('AC turned OFF----')

    def get_status(self):
        if self.status=='OFF':
            return f'AC if {self.status} and temperature is None'
        return f'AC if {self.status} and temperature is {self.temperature}'

class Light(Device):
    def __init__(self,id=None):
        if not id:
            raise DeviceRegistrationError('Entered invalid data for light regestration')
        else:
            self.__id=id
            self.status='OFF'
            self.brightness=20
    
    def get_id(self):
        return self.__id
    
    def brightness_change(self,brightness=None):
        if not brightness:
            raise ValueNotFoundError('U have to provide brightness in numeric')
        elif brightness<0 or brightness>100:
            raise LightBrightnessError('U have entered invalid Value for setting brghtness')
        elif isinstance(brightness,int) == False:
            raise ValueError('Brightness bvalue would be in numeric')
        else:
            self.brightness=brightness
            print(f'light is glowing with {self.brightness} Brightness')

    def turn_off(self):
        self.status='OFF'
        print('Light turned OFF')

    def turn_on(self):
        self.status='ON'
        print(f'light is ON and glowing at the {self.brightness} brightness')

    def get_status(self):
        if self.status=='OFF':
            return f'Light is {self.status} and Brightness is None'
        return f'Light is {self.status} and Brightness is {self.brightness}'

class Room:
    room_device_data={}
    # data={'bedroom':[{'id':1,'device':'obj'},]}
    def __init__(self, location=None):
        if location:
            Room.room_device_data[location]=[]
        else:
            pass
            
    def add_device(self,location=None,device=None):
        if not location or not device:
            raise RoomRegestrationError('U have to provide bedroom name and device obj')
        elif isinstance(location,str)==False or isinstance(device,list)==False:
            raise ValueError('U have provide wrong detail for adding device make sure that bedroom>>string,,, device>>list')
        else:
            if location not in Room.room_device_data.keys():
                Room.room_device_data[location]=device
            else:
                for j in device:
                    for i in Room.room_device_data[location]:
                        if j['device'].get_id() == i['device'].get_id():               
                            raise DuplicateDeviceError(f'Entered  device data already installed in the Location')
                else:
                    Room.room_device_data[location].extend(device)
        

    def remove_device(self,location,device_id):
        if location not in Room.room_device_data.keys():
            raise ValueNotFoundError('Room not registered ')
        else:
            for id in Room.room_device_data[location]:
                if id[device_id] == device_id:
                    Room.room_device_data[location].remove(id)
                    print(f'{device_id} from {location} has been removed successfully')
            else:
                raise ValueNotFoundError(f'Device_id {device_id} not found in in {location} ')

    def turn_all_on(self):
        if not Room.room_device_data:
            raise ValueNotFoundError('No Data avail in records')
        else:
            for room in Room.room_device_data.keys():
                for devices in Room.room_device_data[room]:
                    devices['device'].turn_on()

    def turn_all_off(self):
        if not Room.room_device_data:
            raise ValueNotFoundError('No Data avail in records')
        else:
            for room in Room.room_device_data.keys():
                for devices in Room.room_device_data[room]:
                    devices['device'].turn_off()

    def status_report(self):
        if not Room.room_device_data:
            raise ValueNotFoundError('No Data avail in records')
        else:
            for room in Room.room_device_data.keys():
                for devices in Room.room_device_data[room]:
                    devices['device'].get_status()

class SmartHome:
    def __init__(self):
        self.room_data=Room.room_device_data

    @classmethod
    def from_config(cls,config_dict):
        temp=config_dict['rooms'].keys()
        for room in temp:
            room_creation=Room(room)
            device=[]
            for dev in config_dict['rooms'][room]:
                if dev['type']=='Fan':
                    new_dev=Fan(dev['id'])
                elif dev['type']=='Light':
                    new_dev=Light(dev['id'])
                elif dev['type']=='AC':
                    new_dev=AC(dev['id'])
                else:
                    raise ValueError('Invalid device type')
                device.append({'device_id':dev['id'],'device':new_dev})
            room_creation.add_device(room,device)
        print('Device added successfully')
        return cls()
    def add_device(self,location=None,device_data=None):
        if not location or not device_data:
            raise ValueNotFoundError('Value not provided for regestration')
        else:
            if device_data['type']=='Light':
                obj=Light(device_data['id'])
            elif device_data['type']=='Fan':
                obj=Fan(device_data['id'])
            elif device_data['type']=='AC':
                obj=AC(device_data['id'])
            room=Room()
            room.add_device(location,[{'device_id':device_data,'device':obj}])
        print('Device added successfully')

    config={"rooms":{
            "Bedroom": [
                {"type": "Fan", "id": "Fan-01"},
                {"type": "AC", "id": "AC-01"}
            ]
        }}


    def turn_on(self,location=None,device_id=None):
        if not location or not device_id:
            raise ValueNotFoundError('value not found for turn ON the device')
        else:
            if location not in self.room_data.keys():
                raise ValueNotFoundError('Location not found enter again----')
            else:
                for dev in self.room_data[location]:
                    if dev['device'].get_id()==device_id:
                        if dev['device'].status=='ON':
                            print(f'{location} {device_id} {dev['device'].__class__.__name__} is already ON')
                            break
                        else:
                            dev['device'].turn_on()
                            break
                    else:
                        raise ValueNotFoundError('Enteed Device_Id not found for turning ON device')
    
    def turn_off(self,location=None,device_id=None):
        if not location or not device_id:
            raise ValueNotFoundError('value not found for turn ON the device')
        else:
            if location not in self.room_data.keys():
                raise ValueNotFoundError('Location not found enteren again----')
            else:
                for dev in self.room_data[location]:
                    if dev['device'].get_id()==device_id:
                        if dev['device'].status=='OFF':
                            print(f'{location} {device_id} {dev['device'].__class__.__name__} is already OFF')
                            break
                        else:
                            dev['device'].turn_off()
                            break
                    else:
                        raise ValueNotFoundError('Enteed Device_Id not found for turning OFF device')
    
    def get_status(self,location=None,device_id=None):
        if not location or not device_id:
            raise ValueNotFoundError('value not found for find status the device')
        else:
            if location not in self.room_data.keys():
                raise ValueNotFoundError('Location not found enteren again----')
            else:
                for dev in self.room_data[location]:
                    if dev['device'].get_id()==device_id:
                        print(dev['device'].get_status())
                        break
                    else:
                        raise ValueNotFoundError('Enteed Device_Id not found for getting status of  device')
    
    def turn_on_all(self,location=None):
        if not location:
            raise ValueNotFoundError('U have to enter location for turning ON all device')
        else:
            if location not in self.room_data.keys():
                raise ValueNotFoundError('Location Not Found for turn ON all Devices')
            else:
                for dev in self.room_data[location]:
                    dev['device'].turn_on()

    def turn_off_all(self,location=None):
        if not location:
            raise ValueNotFoundError('U have to enter location for turning OFF all device')
        else:
            if location not in self.room_data.keys():
                raise ValueNotFoundError('Location Not Found for turn OFF all Devices')
            else:
                for dev in self.room_data[location]:
                    dev['device'].turn_off()

    def get_status_all(self,location=None):
        if not location:
            raise ValueNotFoundError('U have to enter location for getting status of all device')
        else:
            if location not in self.room_data.keys():
                raise ValueNotFoundError('Location Not Found for getting status of  all Devices')
            else:
                for dev in self.room_data[location]:
                    print(dev['device'].get_status())

    def turn_on_all_device(self):
        for room in self.room_data.keys():
            for dev in self.room_data[room]:
                dev['device'].turn_on()

    def turn_off_all_device(self):
        for room in self.room_data.keys():
            for dev in self.room_data[room]:
                dev['device'].turn_off()

    def get_status_all_device(self):
        for room in self.room_data.keys():
            for dev in self.room_data[room]:
                print(dev['device'].get_status())

config={"rooms":{
        "Bedroom": [
            {"type": "Fan", "id": "Fan-01"},
            {"type": "AC", "id": "AC-01"}
        ],
        "Living Room": [
            {"type": "Light", "id": "Light-01"},
            {"type": "Fan", "id": "Fan-02"}
        ],
        "Kitchen": [
            {"type": "Light", "id": "Light-02",}
        ]
    }}


try:
    ghar=SmartHome.from_config(config)
    print(Room.room_device_data)
    # ghar.turn_on('Bedroom',"Fan-01")
    # ghar.turn_off('Bedroom',"Fan-01")
    # ghar.get_status_all('Bedroom')
    # ghar.turn_on('Bedroom',"Fan-01")
    # ghar.get_status_all('Bedroom')
    # ghar.turn_off_all('Bedroom')
    # ghar.get_status_all('Bedroom')
    # ghar.add_device('Garden',{"type": "Light", "id": "Light-02",})
    # ghar.add_device('Bedroom',{"type": "Light", "id": "Light-02",})
    # ghar.add_device('Garden',{"type": "Light", "id": "Light-02",})
    # ghar.turn_on_all_device()
    # ghar.turn_off_all_device()
    # ghar.get_status('Kitchen','Light-02')
    ghar.get_status_all_device()
except ValueError as e:
    print(e)
except DeviceRegistrationError as e:
    print(e)
except FanSpeedError as e:
    print(e)
except ACTemperatueError as e:
    print(e)
except LightBrightnessError as e:
    print(e)
except RoomRegestrationError as e:
    print(e)
except DuplicateDeviceError as e:
    print(e)
except ValueNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('Operation Performed')
