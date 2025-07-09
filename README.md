# CoderSandeep0609-Smart-Home-Automation-System-Python-OOP-Project

 Project Overview
This Smart Home Automation System is a fully object-oriented Python project designed to simulate the real-world behavior of smart devices in different rooms of a home. It demonstrates complete mastery of OOP concepts, including abstraction, inheritance, encapsulation, polymorphism, and exception handling — along with dynamic system configuration using dictionary-based setup.

🧠 Key Features
Register and manage multiple rooms (e.g., Bedroom, Kitchen, Living Room)

Install and control multiple smart devices in each room:

✅ Fan (with speed control)

✅ AC (with temperature control)

✅ Light (with brightness control)

Turn ON/OFF any device individually

Turn ON/OFF all devices in a room or the entire home

Get status of any device or entire room

Add new devices to existing rooms

Fully dynamic setup using a config dictionary

Robust exception handling for all edge cases

🏗️ Core OOP Concepts Used
Concept	Description
Abstraction	Implemented via abstract Device base class
Encapsulation	Private attributes like __id, __status
Inheritance	Fan, AC, and Light classes inherit from Device
Polymorphism	Devices override turn_on, turn_off, and get_status
Exception Handling	Custom exceptions for registration, validation, and logic errors
Factory Design Pattern	SmartHome.from_config() constructs system dynamically

🧰 Classes Overview
Class Name	Responsibility
Device (ABC)	Abstract base class for all smart devices
Fan, AC, Light	Device implementations with unique behavior
Room	Manages room-wise device storage and operations
SmartHome	Central controller that initializes the system and manages operations
Custom Exceptions	Error handling for all critical scenarios
🔧 Sample Configuration
config = {
    "rooms": {
        "Bedroom": [
            {"type": "Fan", "id": "Fan-01"},
            {"type": "AC", "id": "AC-01"}
        ],
        "Living Room": [
            {"type": "Light", "id": "Light-01"},
            {"type": "Fan", "id": "Fan-02"}
        ],
        "Kitchen": [
            {"type": "Light", "id": "Light-02"}
        ]
    }
}
🚀 Example Usage
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

✅ Why This Project Matters
This project is not just a device simulator — it's a complete OOP showcase:

Real-world inspired use-case

Clean and extensible architecture

Teaches how to design systems from scratch using Python classes

Ready to be extended into GUI or web-based interface (Flask, Django)

📌 Future Scope (Optional Enhancements)
Add User class and link users to preferred devices

Notification system using SMS/Email (with abstract Notifier base)

GUI interface using tkinter, PyQt or web framework

Database storage for persistent config



