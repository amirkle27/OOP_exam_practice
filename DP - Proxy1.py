# Proxy Pattern – מתווך חכם בין המשתמש לאובייקט
# 📌 מתי משתמשים ב-Proxy?
# 🔹 כשצריך לבצע פעולות נוספות לפני / אחרי גישה לאובייקט.
# 🔹 כשיש גישה יקרה (כמו קריאה למסד נתונים או קובץ) ורוצים לדחות אותה עד שבאמת צריך.
# 🔹 כשצריך לבקרת גישה (למשל, לוודא שלמשתמש יש הרשאות).

class Image:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_image(self):
        print(f"📂 Loading image: {self.file_name}")

    def display_image(self):
        print(f"🖼 Displaying image: {self.file_name}")

class ImageProxy:
    def __init__(self, file_name):
        self.file_name = file_name
        self.real_image = None

    def display_image(self):
        if self.real_image is None:
            self.real_image = Image(self.file_name)
            self.real_image.load_image()
        self.real_image.display_image()


image1 = ImageProxy("hero.png")
image1.display_image()

image2 = ImageProxy("enemy.png")
image2.display_image()