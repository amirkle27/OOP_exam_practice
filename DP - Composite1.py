# 🔹 מתי משתמשים ב-Composite?
# כשיש לך מבנה היררכי שבו אובייקטים בעלי מבנה דומה, ואתה רוצה לטפל בהם באותה דרך – בין אם זה אלמנט יחיד או קבוצה של אלמנטים.
# דוגמאות: תיקיות וקבצים, מחלקות בחברה, רכיבי ממשק משתמש וכו'.
#
from logging import Manager


class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"{self.name} ({self.role}) earns: {self.salary}₪"

class Manager(Employee):
    def __init__(self, name, role, salary):
        super().__init__(name, role, salary)
        self.employees = []

    def hire_employee(self, employee):
        self.employees.append(employee)
        print(f"📢 {employee.name} was hired as {employee.role}!")

    def fire_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"❌ {employee.name} was fired from {employee.role}!")
        else:
            print(f"{employee.name} is not in the team!")

    def calculate_team_salary(self):
        total_salary = self.salary
        for emp in self.employees:
            if isinstance(emp,Manager):
                total_salary += emp.calculate_team_salary()
            else:
                total_salary += emp.get_salary()
        return total_salary

    def __str__(self):
        team_list = "\n  ".join(f"- {emp.name} ({emp.role})" for emp in self.employees) or "No employees"
        secondary_teams = []
        for emp in self.employees:
            if isinstance(emp, Manager):
                secondary_teams.append(str(emp))
        secondary_team_str = "\n  ".join(secondary_teams)
        return ( f"👨‍💼 Manager {self.name} ({self.role})\n  Employees:\n  {team_list}\n {secondary_team_str}\n  Total team cost: {self.calculate_team_salary()}₪")


employee1 = Employee("John", "Software Developer", 5000)
employee2 = Employee("Alice", "QA Engineer", 7000)
employee3 = Employee("Bob", "DevOps Engineer", 6000)
employee4 = Employee("Eve", "Cleaner", 3000)


manager1 = Manager("David", "Team Lead", 10000)
manager1.hire_employee(employee1)
manager1.hire_employee(employee2)
manager1.hire_employee(employee3)


print("\n📜 Employee List:")
print(employee1)
print(employee2)
print(employee3)
print(employee4)

print("\n👨‍💼 Manager Info:")
# print(manager1)


manager1.fire_employee(employee3)

print("\n👨‍💼 Updated Manager Info:")
# print(manager1)

print()
manager2 = Manager("Brian", "Field Manager",20000)
manager2.hire_employee(manager1)
print()
print(manager2)