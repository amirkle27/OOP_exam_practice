# 🔹 מתי משתמשים ב-Composite?
# כשיש לך מבנה היררכי שבו אובייקטים בעלי מבנה דומה, ואתה רוצה לטפל בהם באותה דרך – בין אם זה אלמנט יחיד או קבוצה של אלמנטים.
# דוגמאות: תיקיות וקבצים, מחלקות בחברה, רכיבי ממשק משתמש וכו'.
#

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
        total_salary = self.salary + sum(emp.get_salary() for emp in self.employees)
        return total_salary

    def __str__(self):
        team_list = "\n  ".join(f"- {emp.name} ({emp.role})" for emp in self.employees) or "No employees"
        return f"👨‍💼 Manager {self.name} ({self.role})\n  Employees:\n  {team_list}\n  Total team cost: {self.calculate_team_salary()}₪"


employee1 = Employee("John", "Software Developer", 5000)
employee2 = Employee("Alice", "QA Engineer", 7000)
employee3 = Employee("Bob", "DevOps Engineer", 6000)
employee4 = Employee("Eve", "Cleaner", 3000)


manager = Manager("David", "Team Lead", 10000)
manager.hire_employee(employee1)
manager.hire_employee(employee2)
manager.hire_employee(employee3)


print("\n📜 Employee List:")
print(employee1)
print(employee2)
print(employee3)
print(employee4)

print("\n👨‍💼 Manager Info:")
print(manager)


manager.fire_employee(employee3)

print("\n👨‍💼 Updated Manager Info:")
print(manager)
