from multiprocessing.resource_tracker import unregister


class FileSystem:
    def read_file(self,file_name):
        print(f"Displaying the file [{file_name}]")

    def write_file(self, file_name, content):
        print(f"Writing new file [{file_name}]:\n{content} ")

    def delete_file(self,file_name):
        print(f"Deleting file [{file_name}]")

class FileSystemProxy:
    def __init__(self, user):
        self.user = user
        self.access = FileSystem()

    def read_file(self,file_name):
        return self.access.read_file(file_name)

    def write_file(self,file_name,content):
        if self.user == "Admin":
            return self.access.write_file(file_name,content)
        else:
            print(f"⛔ Access Denied for {self.user}!")

    def delete_file(self, file_name):
        if self.user == "Admin":
            return self.access.delete_file(file_name)
        else:
            print(f"⛔ Access Denied for {self.user}!")

user1 = FileSystemProxy("Admin")
user2 = FileSystemProxy("Guest")

user1.read_file("Top Secret")
user2.read_file("Benny goes to sea")

user1.write_file("Ways to kill your wife", "There are about a million ways to kill your wife!")
user2.write_file("I ate an Apple", "I ate a green apple. it was super tasty!")

user1.delete_file("Beautiful Sonatas")
user2.delete_file("Butterflies of the Caribbeans")





