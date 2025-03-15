# 💡 מה זה Factory Pattern?
# זה דפוס עיצוב (Design Pattern) שבו במקום ליצור אובייקטים ישירות עם __init__, אנחנו נותנים למתודה מיוחדת ליצור אותם בשבילנו.
#
# 🤔 למה צריך את זה?
# ✔ מקצר קוד – לא צריך לכתוב ClassName(...) כל פעם מחדש.
# ✔ מקנה גמישות – קל לשנות את סוג האובייקט שנוצר בלי לשנות את הקוד הראשי.
# ✔ הופך את הקוד לקריא יותר – משתמשים בשם פונקציה ברור במקום יצירת מופעים ישירה.

class Robot:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def describe(self):
        print(f"Hello, I am {self.name}. My function is to {self.function}.")

    @classmethod
    def robot_factory(cls,name):
        robots = {
            "Lily":"Clean",
            "Shem":"Read",
            "Ami":"Fix things",
            "Eyal":"Go Shopping",
            "Avner":"Do the dishes",
            "Ayelet": "Do laundry",
            "Gabi":"Suck Dicks"}
        return cls(name,robots.get(name, "Work"))

robot1 = Robot.robot_factory("Ami")
robot2 = Robot.robot_factory("Lily")
robot3 = Robot.robot_factory("Gabi")
robot4 = Robot.robot_factory("Sasson")

robot1.describe()
robot2.describe()
robot3.describe()
robot4.describe()
