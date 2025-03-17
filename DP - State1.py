# 📌 מה זה State Pattern?
# 🔹 כשלאובייקט יש "מצבים" שונים והוא מתנהג אחרת בהתאם לכל מצב.
# 🔹 כל מצב מיוצג ע"י מחלקה נפרדת עם ההתנהגות הייחודית שלו.
# 🔹 מאפשר הפרדה ברורה בין לוגיקת המצבים השונים ומונע if-else ענקי בקוד.
#
# 🔎 מתי משתמשים בזה?
# ✅ כשיש אובייקט שצריך לשנות התנהגות דינמית בהתאם למצבו הנוכחי.
# ✅ למשל: דלת אוטומטית (פתוחה/סגורה/נעולה), מכונת משקאות (ממתינה/מכניסה כסף/נותנת מוצר), דמות במשחק (נורמלית/משוריינת/פצועה/מתה).

from abc import ABC, abstractmethod
from typing import override

class State(ABC):
    @abstractmethod
    def handle_state(self):
        pass

class HasMoney(State):
    @override
    def handle_state(self):
        print("✅ Dispensing drink... 🥤")
        return NoMoney()

class NoMoney(State):
    def handle_state(self):
        print("❌ Insert money first! 💰")
        return self

class VendingMachine:
    def __init__(self,):
        self.state = NoMoney()

    def add_money(self):
        print("💵 Money inserted!")
        self.state = HasMoney()

    def press_button(self):
        self.state = self.state.handle_state()

machine = VendingMachine()
machine.press_button()
machine.add_money()
machine.press_button()
