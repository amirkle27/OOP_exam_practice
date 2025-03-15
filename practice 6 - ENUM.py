from enum import Enum,auto

class PermissionLevel(Enum):

    BANNED = auto()
    GUEST = auto()
    USER = auto()
    EDITOR = auto()
    ADMIN = auto()


class User:
    def choose_level(self,level):
        try:
            self.level = PermissionLevel(level)
            print(f"You are classified as {PermissionLevel(level).name}")
        except ValueError:
            print("You entered an invalid level")
            self.level = PermissionLevel.GUEST
            print(f"You are automatically classified as {self.level.name}")




dan = User()
dan.choose_level(7)

