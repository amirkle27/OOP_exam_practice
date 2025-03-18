from collections.abc import Iterator, Iterable

class NameIterator(Iterator):
    def __init__(self, names):
        self.names = names
        self.index = 0

    def __next__(self):
        if self.index >= len(self.names):
            raise StopIteration
        name = self.names[self.index]
        self.index += 1
        return name

class NamesCollection(Iterable):
    def __init__(self, names):
        self.names = names

    def __iter__(self):
        return NameIterator(self.names)


names = NamesCollection(["Alice", "Bob", "Charlie", "Diana"])


for name in names:
    print(f"👤 Name: {name}")

