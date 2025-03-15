# 💡 ה-Builder מאפשר ליצור אובייקטים מורכבים שלב-אחר-שלב בצורה ברורה ומובנית.
# 💡 במקום להעביר הרבה ארגומנטים ב-__init__, יוצרים "בונה" (Builder) שמוסיף חלקים לאובייקט בהדרגה.
#
# 📌 למה זה שימושי?
# ✅ כשיש הרבה מאפיינים לאובייקט.
# ✅ כשיש ערכים ברירת מחדל, שלא תמיד צריך להגדיר.
# ✅ כשלא רוצים להעמיס על ה-__init__ עם יותר מדי פרמטרים.
#
from tkinter.font import names


class Character:
    def __init__(self):
        self.name = None
        self.profession = None
        self.strength = None
        self.speed = None
        self.weapon = None
        self.armor = None

    def __str__(self):
        return f"Our character is a hero called {self.name or 'Unknown'}, a {self.profession or 'Unemployed'} with {self.strength or 'Unknown'} strength.\n" \
               f"{self.name or 'They'} can move {self.speed or 'Unknown'}, and has {self.weapon or 'bare hands'} and {self.armor or 'no armor'}."


class CharacterBuilder:
    def __init__(self):
        self.character = Character()

    def set_name(self,name):
        self.character.name = name
        return self

    def set_profession(self, profession):
        self.character.profession = profession
        return self

    def set_strength(self,strength):
        self.character.strength = strength
        return self

    def set_speed(self,speed):
        self.character.speed = speed
        return self

    def set_weapon(self,weapon):
        self.character.weapon = weapon
        return self

    def set_armor(self,armor):
        self.character.armor = armor
        return self

    def build_character(self):
        return self.character

builder = CharacterBuilder()
character1 = builder.set_name("Zonk")\
    .set_profession("Whore-Herder")\
    .set_strength("level 19 out of 10 in a barrels lifting contest")\
    .set_speed("4m an hour, stupidly slow")\
    .set_weapon("Hands only for a weapon, good as hammers")\
    .set_armor("No Armor. He doesn't need one!")\
    .build_character()
print(character1)
print()
character2 = builder.set_name("Maria")\
.set_profession("Whore working for Zonk")\
    .set_strength("No physical strength except for her love-making muscles in her pinky flowery cunt, in which she can definitely crush a man's skull")\
    .set_speed("100m an hour")\
    .set_weapon("Her tits for a weapon, her shiny ass, and of course, her Cunt! oh! What a Cunt!")\
    .set_armor("No Armor. She doesn't need one as you will fall right to her feet!")\
    .build_character()


print(character2)