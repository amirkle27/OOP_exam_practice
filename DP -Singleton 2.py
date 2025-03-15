from tkinter import PanedWindow


class Logger:
    _message = None

    def __new__(cls, *args, **kwargs):
        if cls._message == None:
            cls._message = super().__new__(cls)
        return cls._message

    def __init__(self):
        if not hasattr(self,"message"):
            self.message = input("Message please?")



    def log(self):
        print(f"[LOG]: {self.message}")


logger1 = Logger()
logger2 = Logger()

logger1.log()
logger2.log()

print(logger1==logger2)