# 📌 מה הרעיון?
# לפעמים יש לנו אובייקט מורכב, ואנחנו רוצים לשכפל אותו במהירות במקום ליצור מחדש.
# במקום להשתמש ב-__init__, פשוט נעתיק את האובייקט עם כל התכונות שלו.
#
# איך עושים את זה?
# 1️⃣ נגדיר מחלקת אבסטרקטית עם שיטת השכפול (clone).
# 2️⃣ כל מחלקה שתירש תוכל להעתיק אובייקטים עם שינויים קלים.
# 3️⃣ נשתמש ב- copy.deepcopy() כדי לשכפל אובייקט שלם.

from abc import ABC, abstractmethod
import copy
from typing import override


class Character(ABC):
    @abstractmethod
    def clone(self):
        pass

class Hero(Character):
    def __init__(self, name, weapon, armor, special_ability, magic_power):
        self.name =name
        self.weapon = weapon
        self.armor = armor
        self.special_ability = special_ability
        self.magic_power = magic_power

    def __str__(self):
        return f"Warrior - [Name]: {self.name} [Weapon]: {self.weapon or 'None'}, [Armor]: {self.armor or 'None'}, [Special Ability]: {self.special_ability}, [Magic Power]: {self.magic_power or 'None'} "
    @override
    def clone(self):
        return copy.deepcopy(self)

warrior = Hero("Erik", "Axe", "Golden Shield", "Extraordinary strength", None)
mage = Hero("Onkimberg", "Magic Staff", "Invisible Shield of Dark Magic (Upon using Mana Points)", "Magic Power", "Level 10 - Master")
thief = Hero("Ben", None, None, "Super Fast and Agile, Can go Unnoticed", None)

warrior2 = warrior.clone()
warrior2.name = "Mush"
mage2 = mage.clone()
mage2.name = "Alexander"
thief2 = thief.clone()
thief2.name = "Anton"

print(warrior)
print(mage)
print(thief)


print(warrior2)
print(mage2)
print(thief2)

#########################################################
#SHALLOW COPY
#########################################################
import copy

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs  # רשימה של שירים

    def clone(self):
        return copy.copy(self)  # שיכפול רדוד

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {self.songs}"

# רשימת שירים מקורית
songs_list = ["Song A", "Song B", "Song C"]
playlist1 = Playlist("My Playlist", songs_list)

# שיכפול רדוד
playlist2 = playlist1.clone()

# שינוי ברשימת השירים של playlist2
playlist2.songs.append("Song D")
playlist1.songs.append("SONONFDSFDFS")
print(playlist1)  # גם בפלייליסט המקורי נוסף השיר!
print(playlist2)
