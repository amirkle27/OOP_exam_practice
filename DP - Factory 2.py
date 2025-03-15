from abc import ABC, abstractmethod
from typing import override

class Character(ABC):
    def __init__(self, name, profession, ability):
        self.name = name
        self.profession = profession
        self.ability = ability

    @abstractmethod
    def describe(self):
        pass

class Hero(Character):
    @override
    def describe(self):
        print(f"You chose {self.name}, who is a {self.profession} and has a lot of {self.ability} ability")


class CharacterFactory:
    @classmethod
    def create_character(cls, name, char_type):
        characters = {
            "warrior": "strength",
            "mage": "magic",
            "thief": "stealth",
            "shepherd": "herding",
            "cleaner": "cleaning",
            "salesman": "persuasion",
            "whore": "pleasure"
        }

        profession = char_type.capitalize()  # הופך ל- Warrior במקום warrior
        ability = characters.get(char_type, "basic skills")  # מחזיר תכונה או ברירת מחדל

        return Hero(name, profession, ability)  # החזרנו דמות מסוג Hero


name = input("Enter character name: ")
char_type = input(f"Enter character type: ")

character = CharacterFactory.create_character(name, char_type)

if character:
     character.describe()

hero1 = CharacterFactory.create_character(name, char_type)

# 🔴 שלב 1: הפעלת הקובץ
# 📌 איך זה קורה?
# 🔹 המשתמש מריץ את הקובץ (python my_file.py) או לוחץ על "Run" ב- PyCharm / VS Code / Terminal.
# 🔹 Python מתחיל לקרוא את הקוד שורה אחר שורה מלמעלה למטה.
#
# 🟢 שלב 2: Python מזהה מחלקות (אבל לא יוצר אותן!)
# 📌 Python קורא ומזהה את המחלקות (אבל עדיין לא מפעיל אותן)
# 🔹 הוא מזהה את Character בתור מחלקה מופשטת (ABC).
# 🔹 הוא מזהה את Hero כיורשת ממנה.
# 🔹 הוא מזהה את CharacterFactory בתור מחלקה עם מתודה סטטית create_character.
#
# 🚨 שימו לב:
# ✔ Python לא יוצר עדיין אובייקטים של מחלקות אלה!
# ✔ הוא רק שומר את המבנה שלהם בזיכרון.
#
# 🟡 שלב 3: Python מגיע לקלט מהמשתמש (input)
# 📌 עכשיו Python מגיע לשורות:
#
# python
# Copy code
# name = input("Enter character name: ")
# char_type = input("Enter character type: ")
# 🔹 כאן Python עוצר ומחכה שהמשתמש יקליד קלט!
# 🔹 שלב ראשון: Python מדפיס "Enter character name: " במסך.
# 🔹 המשתמש מקליד שם (לדוגמה: "Arthur") ולוחץ על Enter.
# 🔹 שלב שני: Python מדפיס "Enter character type: " במסך.
# 🔹 המשתמש מקליד סוג דמות (לדוגמה: "warrior") ולוחץ על Enter.
# 🔹 שני המשתנים מתעדכנים בזיכרון:
#
# python
# Copy code
# name = "Arthur"
# char_type = "warrior"
# 🟠 שלב 4: קריאה לפונקציה create_character מתוך CharacterFactory
# 📌 Python מבצע את השורה:
#
# python
# Copy code
# character = CharacterFactory.create_character(name, char_type)
# 🔹 Python מזהה את המתודה create_character כמחלקתית (@classmethod).
# 🔹 הוא שולח לה את המשתנים:
#
# python
# Copy code
# CharacterFactory.create_character("Arthur", "warrior")
# 🔵 שלב 5: ביצוע הפונקציה create_character
# 📌 Python נכנס לפונקציה:
#
# python
# Copy code
# @classmethod
# def create_character(cls, name, char_type):
# 🔹 cls מתייחס ל- CharacterFactory
# 🔹 name = "Arthur"
# 🔹 char_type = "warrior"
#
# 📌 Python מחפש את היכולת של הדמות במילון characters
#
# python
# Copy code
# characters = {
#     "warrior": "strength",
#     "mage": "magic",
#     "thief": "stealth",
#     "shepherd": "herding",
#     "cleaner": "cleaning",
#     "salesman": "persuasion",
#     "whore": "pleasure"
# }
# 🔹 הוא מחפש את "warrior" במילון – ומוצא את "strength".
#
# 🔹 אחרי זה:
#
# python
# Copy code
# profession = char_type.capitalize()  # "warrior" -> "Warrior"
# ability = characters.get(char_type, "basic skills")  # "strength"
# 🔹 profession = "Warrior"
# 🔹 ability = "strength"
#
# 🟣 שלב 6: יצירת מופע של Hero
# 📌 Python מבצע:
#
# python
# Copy code
# return Hero(name, profession, ability)
# 🔹 הוא שולח את שלושת המשתנים למחלקת Hero:
#
# python
# Copy code
# Hero("Arthur", "Warrior", "strength")
# 🔹 כעת הוא נכנס ל- Hero.__init__ שקיבל בירושה מ- Character:
#
# python
# Copy code
# def __init__(self, name, profession, ability):
# 🔹 שם ערכים במשתנים:
#
# python
# Copy code
# self.name = "Arthur"
# self.profession = "Warrior"
# self.ability = "strength"
# 🔹 נוצר אובייקט חדש של Hero, והוא מוחזר חזרה לקוד הראשי.
#
# 🟤 שלב 7: קריאה למתודה describe
# 📌 Python מגיע לשורה:
#
# python
# Copy code
# if character:
#     character.describe()
# 🔹 הוא מזהה שהמשתנה character מכיל אובייקט תקף של Hero
# 🔹 נכנס למתודה:
#
# python
# Copy code
# def describe(self):
#     print(f"You chose {self.name}, who is a {self.profession} and has a lot of {self.ability} ability.")
# 🔹 משתנים מוחלפים בערכים שלהם:
#
# python
# Copy code
# "You chose Arthur, who is a Warrior and has a lot of strength ability."
# 🔹 ההודעה מודפסת למסך!
#
# 🟠 שלב 8: יצירת דמות נוספת (hero1)
# 📌 כעת הקוד מבצע:
#
# python
# Copy code
# hero1 = CharacterFactory.create_character(name, char_type)
# hero1.describe()
# 🔹 כל השלבים הקודמים חוזרים על עצמם (מ- שלב 4 ועד 7).
# 🔹 שוב נוצר אובייקט חדש של Hero, ושוב מופעל describe.
# 🔹 הודעה נוספת מודפסת על המסך.
#
# 🟢 שלב 9: סיום התוכנית
# 📌 מה קורה עכשיו?
# 🔹 כל הקוד הסתיים ו-Python מגיע לסוף הקובץ.
# 🔹 אם הכל עבד טוב, התוכנית נסגרת ללא שגיאות.
# 🔹 אם הייתה שגיאה, הטרייסבק מוצג במסך.
#
# 🔴 סיכום כל השלבים בקצרה
# Python מריץ את הקובץ.
# Python קורא ומזהה מחלקות (אבל לא יוצר מופעים עדיין).
# Python מבקש קלט מהמשתמש (name ו- char_type).
# Python שולח את הנתונים לפונקציה create_character.
# create_character בודק אם הדמות חוקית, ושולף יכולת מתאימה.
# create_character מחזיר אובייקט חדש של Hero.
# המתודה describe מופעלת ומדפיסה את הנתונים למסך.
# הקוד יוצר דמות נוספת (hero1), וכל השלבים חוזרים שוב.
# הקובץ מסתיים ו-Python מסיים את התהליך.