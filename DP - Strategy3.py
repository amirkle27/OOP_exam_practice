from abc import ABC, abstractmethod
from typing import override
import re


class PaymentStrategy(ABC):
    def __init__(self, amount, card_number=None, phone_number=None, email=None):
        self.amount = amount
        self.card_number = card_number
        self.phone_number = phone_number
        self.email = email

    @abstractmethod
    def pay(self):
        pass

class Cash(PaymentStrategy):
    @override
    def pay(self):
        print(f"💵 You chose to pay {self.amount}$ with cash! Thanks! 💵")

class Credit(PaymentStrategy):
    @override
    def pay(self):
        if not self.card_number:
            print("❌ Error: No credit card number provided!")
            return
        print(f"💳 You chose to pay {self.amount}$ using Credit Card No. [{self.card_number[-4:]}],. Thank you. 💳")

class Bit(PaymentStrategy):
    @override
    def pay(self):
        if not self.phone_number:
            print("❌ Error: No phone number provided for Bit payment!")
            return
        print(f"📲 You transferred {self.amount}$ using Bit with Phone Number: [{self.phone_number[-6:]}]. Thanks a lot! 📲")

class PayPal(PaymentStrategy):
    def pay(self):
        if not self.email or not self.is_valid_email(self.email):
            print("❌ Error: Invalid email address for PayPal!")
            return
        print(f"📧 You paid {self.amount}$ via PayPal using the email: {self.email}. Thank you! 📧")

    def is_valid_email(self, email):
        pattern = r'^[^@]+@[^@]+\.[A-Za-z][A-Za-z0-9]*$'
        return re.match(pattern, email)

class Payer:
    def __init__(self, payment_strategy:PaymentStrategy):
        self.payment_strategy = payment_strategy

    def change_payment_method(self, payment_strategy:PaymentStrategy):
        self.payment_strategy = payment_strategy

    def pay(self):
        self.payment_strategy.pay()


payer = Payer(Cash(2000))
payer.pay()
payer.change_payment_method(Credit(1500, "4580-1601-2246-3215"))
payer.pay()
payer.change_payment_method(Bit(900,  None,"0525567711"))
payer.pay()