# 🎯 המטרה של Singleton:
# 🔹 לוודא שיש רק אובייקט אחד מסוג מסוים!
# 🔹 ולדאוג שכל מי שקורא לו – יקבל תמיד את אותו אובייקט!

class Database:
    _object = None

    def __new__(cls, *args, **kwargs):
        if cls._object == None:
            cls._object = super().__new__(cls)
        return cls._object

obj1 = Database()
obj2 = Database()

print(obj1)
print(obj2)

print(obj1 == obj2)