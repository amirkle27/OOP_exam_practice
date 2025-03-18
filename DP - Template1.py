# ✅ Template Method – דפוס עיצוב לשליטה בתהליך עם שלבים קבועים
# 📌 מה הרעיון של הדפוס הזה?
# 🔹 יש לנו תהליך עם סדר שלבים קבוע, אבל כל תת-מחלקה יכולה לממש שלבים בצורה שונה.
# 🔹 המחלקה האבסטרקטית מגדירה את ה"מתכון" (Template) והמחלקות היורשות קובעות איך לבצע חלקים ממנו.
#
# 📌 דוגמאות מהחיים:
# ✅ משחקי לוח – החוקים קבועים, אבל לכל משחק יש שלבים שונים.
# ✅ הזמנת אוכל במסעדה – השלבים זהים (הזמנה, הכנה, תשלום), אבל כל מסעדה מכינה אחרת.
# ✅ הכנת קפה – תמיד יש מים חמים, אבל יש סוגים שונים (אספרסו, פילטר, נמס).

from abc import ABC, abstractmethod

class HotBeverage(ABC):
    def prepare(self):
        """Template Method - מגדיר את השלבים הכלליים להכנת משקה חם"""
        self.boil_water()
        self.brew()
        self.pour_into_cup()
        self.add_condiments()
        print("☕ Your drink is ready!\n")

    def boil_water(self):
        print("💧 Boiling water...")

    def pour_into_cup(self):
        print("🫖 Pouring into cup...")

    @abstractmethod
    def brew(self):
        """שלב שמשתנה בין סוגי המשקאות"""
        pass

    @abstractmethod
    def add_condiments(self):
        """תוספות שמשתנות לפי סוג המשקה"""
        pass


class Coffee(HotBeverage):
    def brew(self):
        print("☕ Brewing coffee...")

    def add_condiments(self):
        print("🥄 Adding sugar and milk...")


class Tea(HotBeverage):
    def brew(self):
        print("🍵 Steeping the tea...")

    def add_condiments(self):
        print("🍋 Adding lemon and honey...")


class HotChocolate(HotBeverage):
    def brew(self):
        print("🍫 Mixing hot chocolate powder...")

    def add_condiments(self):
        print("🥛 Adding whipped cream on top...")


# יצירת משקאות שונים בעזרת ה-Template Method
coffee = Coffee()
coffee.prepare()

tea = Tea()
tea.prepare()

hot_chocolate = HotChocolate()
hot_chocolate.prepare()
