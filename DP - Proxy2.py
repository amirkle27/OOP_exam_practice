class SecretData:
    def __init__(self):
        self.data = "🔒 Displaying Super Secret Data"

    def get_data(self):
        return self.data

class SecretDataProxy:
    def __init__(self,user_role):
        self.user_role = user_role
        self.real_data = SecretData()

    def get_data(self):
        if self.user_role == "Admin":
            return self.real_data.get_data()
        else:
            return f"⛔ Access Denied for {self.user_role}!"

admin = SecretDataProxy("Admin")
print(admin.get_data())

guest = SecretDataProxy("Guest")
print(guest.get_data())

