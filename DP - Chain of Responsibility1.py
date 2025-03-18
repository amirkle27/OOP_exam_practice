# ✅ Chain of Responsibility – שרשרת אחריות
# 📌 מתי משתמשים בזה?
# 🔹 כשיש רצף של מטפלים פוטנציאליים לבקשה, וכל אחד מחליט אם לטפל בה או להעביר אותה הלאה.
# 🔹 במקום if-elif-else ענקי, כל רמה יודעת רק על השלב הבא, בלי תלות באחרים.
#
# 💡 דוגמאות שימושיות:
# ✔ מערכת הרשאות – אם בקשה מגיעה, היא עוברת דרך מנהל, ואז למנכ"ל אם צריך.
# ✔ מסנן הודעות ספאם – כל מסנן בודק את ההודעה ומחליט אם להעביר הלאה או לחסום.
# ✔ טיפול בשגיאות – כל מודול במערכת בודק אם הוא יודע לתקן את השגיאה או להעביר הלאה.

from abc import ABC, abstractmethod
from typing import override

class Approver(ABC):
    def __init__(self, approval_limit):
        self.approval_limit = approval_limit
        self.next_approver = None

    def set_next(self,approver):
        self.next_approver = approver

    @abstractmethod
    def approve_request(self,amount):
        pass

class Manager(Approver):
    def __init__(self):
        super().__init__(approval_limit = 100)

    @override
    def approve_request(self,amount):
        if amount <= self.approval_limit:
            print(f"✅ Manager approved ${amount}")
        elif self.next_approver:
            print(f"➡ Manager forwards request of ${amount} to next level")
            self.next_approver.approve_request(amount)

class Director(Approver):
    def __init__(self):
        super().__init__(approval_limit = 1000)

    @override
    def approve_request(self,amount):
        if amount<= self.approval_limit:
            print(f"✅ Director approved ${amount}")
        elif self.next_approver:
            print(f"➡ Director forwards request of ${amount} to next level")
            self.next_approver.approve_request(amount)

class VP(Approver):
    def __init__(self):
        super().__init__(approval_limit = 5000)

    @override
    def approve_request(self,amount):
        if amount <= self.approval_limit:
            print(f"✅ VP approved ${amount}")
        elif self.next_approver:
            self.next_approver.approve_request(amount)

class CEO(Approver):
    def __init__(self):
        super().__init__(approval_limit = float("inf"))

    @override
    def approve_request(self, amount):
        print(f"✅ CEO approved ${amount}")



manager = Manager()
director = Director()
vp = VP()
ceo = CEO()

manager.set_next(director)
director.set_next(vp)
vp.set_next(ceo)

requests = [50,500,2000,7000]

for amount in requests:
    print(f"\n🔹 Requesting approval for ${amount}")
    manager.approve_request(amount)
