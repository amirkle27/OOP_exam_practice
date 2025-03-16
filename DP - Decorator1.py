# 🎭 מה זה Decorator Pattern?
# מטרתו: להוסיף פונקציונליות לאובייקטים בלי לשנות את הקוד המקורי שלהם.
# איך זה עובד? משתמשים במחלקות שעוטפות (wrap) את האובייקט ומוסיפות לו יכולות חדשות.
# מתי משתמשים בזה?
# ✅ כשלא רוצים לשנות ישירות את הקוד של המחלקה המקורית.
# ✅ כשצריך להוסיף יכולות בצורה מודולרית וגמישה.
# ✅ כשיש התנהגות שחוזרת על עצמה בכמה מקומות (כמו Logging, Caching, Authorization וכו').

# מחלקת הבסיס - קפה רגיל


class Coffee:
    def cost(self):
        return 10  # מחיר בסיסי של קפה רגיל

# Decorator בסיסי - עוטף קפה ומוסיף תוספות
class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

# תוספות לקפה - כל אחת מוסיפה למחיר
class Milk(CoffeeDecorator):
    def cost(self):
        return super().cost() + 3  # תוספת חלב ב-3 שקלים

class Sugar(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2  # תוספת סוכר ב-2 שקלים

class Caramel(CoffeeDecorator):
    def cost(self):
        return super().cost() + 5  # תוספת קרמל ב-5 שקלים

# הכנת קפה רגיל
coffee = Coffee()
print(f"☕ Regular Coffee: {coffee.cost()}₪")

# קפה עם חלב
coffee_with_milk = Milk(coffee)
print(f"☕ Coffee with Milk: {coffee_with_milk.cost()}₪")

# קפה עם חלב וסוכר
coffee_with_milk_sugar = Sugar(coffee_with_milk)
print(f"☕ Coffee with Milk and Sugar: {coffee_with_milk_sugar.cost()}₪")

# קפה עם חלב, סוכר וקרמל 🍮
coffee_full = Caramel(coffee_with_milk_sugar)
print(f"☕ Coffee with Milk, Sugar and Caramel: {coffee_full.cost()}₪")
