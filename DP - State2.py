from abc import ABC, abstractmethod
from typing import override

class DoorState(ABC):
    @abstractmethod
    def handle_state(self, door):
        pass

class DoorOpen(DoorState):
    @override
    def handle_state(self, door):
        print("🚪 The door is already open!")
        return self

class DoorLocked(DoorState):
    @override
    def handle_state(self, door):
        print("❌ The door is locked! You must unlock it first.")
        return self

class DoorUnlocked(DoorState):
    @override
    def handle_state(self, door):
        print("✅ You opened the door!")
        return DoorOpen()

class Door:
    def __init__(self):
        self.state = DoorLocked()

    def set_state(self, new_state):
        self.state = new_state

    def lock_door(self):
        if isinstance(self.state, DoorOpen):
            print("❌ Cannot lock an open door! Close it first.")
        else:
            print("🔒 You Locked the door")
        self.state = DoorLocked()

    def unlock_door(self):
        if isinstance(self.state, DoorLocked):
            print("🔒 You Unlocked the door")
            self.state = DoorUnlocked()
        else:
            print("❌ The door is already unlocked.")


    def close_door(self):
        if isinstance(self.state, DoorOpen):
            print("🚪 You closed the door.")
            self.state = DoorUnlocked()
        else:
            print("❌ The door is already closed.")


    def press_handle(self):
        self.state = self.state.handle_state(self)


door = Door()

door.press_handle()
door.unlock_door()
door.press_handle()
door.close_door()
door.press_handle()
door.press_handle()

