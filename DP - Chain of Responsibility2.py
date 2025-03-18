from abc import ABC, abstractmethod
from typing import override

class SupportLevel(ABC):
    def __init__(self, support_limit):
        self.support_limit = support_limit
        self.next_support_level = None

    def set_next(self, support_level):
        self.next_support_level = support_level

    @abstractmethod
    def support(self,problem):
        pass

class BasicSupport(SupportLevel):
    def __init__(self):
        super().__init__(support_limit = "basic_support")

    @override
    def support(self,problems):
        for level, issues  in problems.items():
            for problem in issues:
                if level == "basic_support":
                    print(f"✅ Basic Support resolved: [{problem}]")
                elif self.next_support_level:
                    print(f"➡ Basic Support forwards issue: [{problem}]")
                    self.next_support_level.support({level: [problem]})

class AdvancedSupport(SupportLevel):
    def __init__(self):
        super().__init__(support_limit = "advanced_support")

    @override
    def support(self,problems):
        for level, issues in problems.items():
            for problem in issues:
                if level == "advanced_support":
                    print(f"✅ Advanced Support resolved: [{problem}]")
                elif self.next_support_level:
                    print(f"➡ Advanced Support forwards issue: [{problem}]")
                    self.next_support_level.support({level:[problem]})

class ExpertSupport (SupportLevel):
    def __init__(self):
        super().__init__(support_limit = "expert_support")

    @override
    def support(self,problems):
        for level, issues in problems.items():
            for problem in issues:
                if level == "expert_support":
                    print(f"✅ Expert Support resolved: [{problem}]")
                else:
                    print(f"❌ No support available for: [{problem}]")


basic_support = BasicSupport()
advanced_support = AdvancedSupport()
expert_support = ExpertSupport()

basic_support.set_next(advanced_support)
advanced_support.set_next(expert_support)

problems = {
    "basic_support": ["I forgot my password", "My account is locked"],
    "advanced_support": ["Program problem", "Software installation failed"],
    "expert_support": ["Server Crashed", "Network down"]
}

basic_support.support(problems)