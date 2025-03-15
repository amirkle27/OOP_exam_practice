class Office:
    employees_number = 0

    def __init__(self):
        Office.employees_number += 1

    @classmethod
    def get_total_employees(cls):
        print(f"there are {cls.employees_number} employees in the office:")



Office.get_total_employees()

danny = Office()
ruth = Office()
ami = Office()

Office.get_total_employees()