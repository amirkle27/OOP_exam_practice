from abc import ABC, abstractmethod
from typing import override
import json

class Reports(ABC):
    def __init__(self,data):
        self.data = data

    def prepare(self):
        self.generate_data()
        self.load_data()
        self.process_data()
        self.present_data()

    @abstractmethod
    def generate_data(self):
        pass

    def load_data(self):
        print("📥 Loading data...")

    def process_data(self):
        print("🔍 Processing data...")

    @abstractmethod
    def present_data(self):
        pass


class TextReports(Reports):
    @override
    def generate_data(self):
        print("📄 Generating Text Report...")

    def present_data(self):
        print("📝 Presenting data as Text:")
        for entry in self.data:
            print(f"Name: {entry['Name']}, Age: {entry['Age']}")
        print("✅ Report completed!\n")

class CSVReports(Reports):
    @override
    def generate_data(self):
        print("📄 Generating CSV Report...")

    @override
    def present_data(self):
        print("📊 Presenting data as CSV:")
        for entry in self.data:
            print(f"{entry['Name']}, {entry['Age']}")
        print("✅ Report completed!\n")

class JSONReports(Reports):
    @override
    def generate_data(self):
        print("📄 Generating JSON Report...")

    @override
    def present_data(self):
        print("📜 Presenting data as JSON:")
        print(json.dumps(self.data, indent=2))
    print("✅ Report completed!\n")


data = [{"Name":"Alice","Age":30},
        {"Name":"Bob","Age":25}]

report1 = TextReports(data)
report1.prepare()

report2 = CSVReports(data)
report2.prepare()

report3 = JSONReports(data)
report3.prepare()
