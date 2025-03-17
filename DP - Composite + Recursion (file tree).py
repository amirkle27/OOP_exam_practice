# 💡 שילוב רקורסיה עם Composite – עץ תיקיות וקבצים
# 🔹 עכשיו נשלב את Composite עם רקורסיה כדי להדפיס מבנה תיקיות וקבצים בצורה היררכית!
# 🔹 ניצור מחלקות שמייצגות תיקיות וקבצים, כאשר כל תיקיה יכולה להכיל תיקיות נוספות או קבצים.
# 🔹 נשתמש ברקורסיה כדי לעבור על התיקיות והתוכן שלהן עד הסוף.
#
# 📌 איך המבנה ייראה?
# נניח שיש לנו את העץ הבא:
#

# 📁 Root
#  ├── 📁 Documents
#  │   ├── 📄 Resume.pdf
#  │   ├── 📄 Report.docx
#  │   ├── 📁 Personal
#  │       ├── 📄 ID_Card.jpg
#  │       ├── 📄 Birth_Certificate.pdf
#  ├── 📁 Pictures
#  │   ├── 📄 Beach.jpg
#  │   ├── 📄 Family.png
#  ├── 📄 Notes.txt
# 💡 המטרה:
# ✔ להדפיס את המבנה בעזרת Composite.
# ✔ לעבור על כל התיקיות עם רקורסיה ולהדפיס את הקבצים והתיקיות הפנימיות.
#


class FileSystemItem:
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        pass


class File(FileSystemItem):
    def display(self, indent=0):
        print(" " * indent + f"📄 {self.name}")



class Folder(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, item):
        self.children.append(item)

    def display(self, indent=0):
        print(" " * indent + f"📁 {self.name}")
        for item in self.children:
            item.display(indent + 4)


root = Folder("Root")

# יצירת תיקיות משנה
documents = Folder("Documents")
pictures = Folder("Pictures")
personal = Folder("Personal")

# יצירת קבצים
resume = File("Resume.pdf")
report = File("Report.docx")
id_card = File("ID_Card.jpg")
birth_certificate = File("Birth_Certificate.pdf")
beach_photo = File("Beach.jpg")
family_photo = File("Family.png")
notes = File("Notes.txt")

# בניית המבנה – הוספת קבצים ותיקיות
root.add(documents)
root.add(pictures)
root.add(notes)

documents.add(resume)
documents.add(report)
documents.add(personal)  # תיקיית "Personal" בתוך "Documents"
personal.add(id_card)
personal.add(birth_certificate)

pictures.add(beach_photo)
pictures.add(family_photo)

# הצגת עץ התיקיות והקבצים
root.display()


