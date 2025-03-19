from abc import ABC, abstractmethod
from typing import override

class EatingStrategy(ABC):
    @abstractmethod
    def eat(self):
        pass

class SpoonEating(EatingStrategy):
    @override
    def eat(self):
        print("🥄 אוכל את הגלידה עם כפית... לאט לאט...")

class LickingEating(EatingStrategy):
    @override
    def eat(self):
        print("🍦 מלקק את הגלידה כמו שצריך!")

class BigBitesEating(EatingStrategy):
    @override
    def eat(self):
        print("😋 אוכל את הגלידה בביסים גדולים! זה נגמר מהר!")

class Kid:
    def __init__(self, eating_strategy:EatingStrategy):
        self.eating_strategy = eating_strategy

    def set_strategy(self, eating_strategy:EatingStrategy):
        self.eating_strategy = eating_strategy

    def eat_ice_cream(self):
        self.eating_strategy.eat()

    def get_strategy_name(self):
        return self.eating_strategy.__class__.__name__

#
# moshe = Kid(SpoonEating())
# moshe.eat_ice_cream()
# moshe.set_strategy(BigBitesEating())
# moshe.eat_ice_cream()

moshe = Kid(SpoonEating())  # הילד מתחיל עם כפית
moshe.eat_ice_cream()  # 🥄 אוכל את הגלידה עם כפית...

moshe.set_strategy(LickingEating())  # הילד מחליף שיטה
moshe.eat_ice_cream()  # 🍦 מלקק את הגלידה כמו שצריך!

print(f"הילד כרגע אוכל בשיטה: {moshe.get_strategy_name()}")

moshe.set_strategy(BigBitesEating())  # הילד הופך לרעב מאוד

print(f"הילד כרגע אוכל בשיטה: {moshe.get_strategy_name()}")
moshe.eat_ice_cream()  # 😋 אוכל את הגלידה בביסים גדולים!
