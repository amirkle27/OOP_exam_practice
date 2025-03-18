from abc import ABC, abstractmethod

class HiringProcess(ABC):
    def hire(self):
        self.review_resume()
        self.interview()
        self.offer_salary()
        print("✅ Hiring process completed!\n")

    def review_resume(self):
        print("📄 Reviewing resume...")

    @abstractmethod
    def interview(self):
        pass

    @abstractmethod
    def offer_salary(self):
        pass

class DeveloperHiring(HiringProcess):
    def interview(self):
        print("💻 Conducting technical interview...")

    def offer_salary(self):
        print("💰 Offering competitive salary for Developer.")

class ManagerHiring(HiringProcess):
    def interview(self):
        print("📊 Conducting management interview...")

    def offer_salary(self):
        print("💰 Offering high salary with bonuses for Manager.")


dev_hiring = DeveloperHiring()
dev_hiring.hire()

manager_hiring = ManagerHiring()
manager_hiring.hire()
