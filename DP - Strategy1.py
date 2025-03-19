#  מה זה Strategy Pattern?
#
# מאפשר להחליף אלגוריתמים שונים מבלי לשנות את הקוד של המחלקה הראשית.
# כל אלגוריתם מיוצג כ-מחלקה נפרדת, והאובייקט הראשי יכול להחליף ביניהם בזמן ריצה.
# מונע שימוש בענקיות של if-else לבחירת אלגוריתם.
# דוגמאות:
# ✅ סוגי מיון שונים (Bubble Sort, Quick Sort, Merge Sort).
# ✅ שיטות תשלום שונות (אשראי, PayPal, ביטקוין).
# ✅ סוגי התקפה במשחקים (חרב, קשת, קסם).


from abc import ABC, abstractmethod
from typing import override

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self):
        pass

class BuiltInSort(SortingStrategy):
    @override
    def sort(self, data):
        print("🚀 Using Python's built-in sort")
        return sorted(data)


class QuickSort(SortingStrategy):
    @override
    def sort(self, data):
        print("⚡ Using Quick Sort")
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class BubbleSort(SortingStrategy):
    @override
    def sort(self, data):
        print("🔵 Using Bubble Sort")
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class Sorter:
    def __init__(self, strategy:SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy:SortingStrategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)


data = [5, 3, 8, 6, 2, 7, 4, 1]

sorter = Sorter(BubbleSort())
print(sorter.sort(data.copy()))

sorter.set_strategy(QuickSort())
print(sorter.sort(data.copy()))

sorter.set_strategy(BuiltInSort())
print(sorter.sort(data.copy()))
