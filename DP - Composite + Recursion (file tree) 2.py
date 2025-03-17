import os

def display_directory(path, indent=0):
    try:
        print(" " * indent + f"📁 {os.path.basename(path)}")

        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):  # אם זה תיקייה, ניכנס פנימה (רקורסיה)
                display_directory(full_path, indent + 4)
            else:  # אם זה קובץ, פשוט נדפיס אותו
                print(" " * (indent + 4) + f"📄 {item}")

    except PermissionError:
        print(" " * indent + "⛔ Access Denied")  # במקרה של תיקייה חסומה


# 🔹 בחר נתיב להצגת עץ תיקיות
directory_path = input("Enter directory path: ")
display_directory(directory_path)
