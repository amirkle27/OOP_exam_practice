
class Store:
    products = {}

    def __init__(self, product, price, quantity_in_store):
        self.product = product
        self.price = price
        self.quantity_in_store = quantity_in_store
        self.products[product.lower()] = {"price":self.price, "quantity_in_store":self.quantity_in_store}

class Customer:

    def __init__(self):
        self.wanted_product = None
        self.wanted_quantity = None
        self.budget = None

    def purchase_item(self, wanted_product, budget, wanted_quantity):
        self.wanted_product = wanted_product
        self.budget = budget
        self.wanted_quantity = wanted_quantity

        try:
            if self.wanted_quantity <= 0:
                raise ValueError ("Wanted quantity must be above 0$")
            if self.budget <= 0:
                raise ValueError("Your budget must be above 0$")
            if self.wanted_product.lower() not in (key for key in Store.products):
                raise ValueError ("Product not in store or mistype")
            if self.wanted_quantity > Store.products[wanted_product]["quantity_in_store"]:
                raise ValueError (f"Not enough items in store. you can only buy {Store.products[wanted_product]["quantity_in_store"]} {self.wanted_product}s")
            if self.budget < Store.products[wanted_product]["price"]*self.wanted_quantity:
                raise ValueError (f"Your budget is too low.\
                \nFor {self.budget}$ you can buy {self.budget//Store.products[wanted_product]["price"]} {self.wanted_product}s.\
                \nEach {self.wanted_product} costs {Store.products[wanted_product]["price"]}$")


            else:
                print(f"Purchase successful!\nYou just bought {self.wanted_quantity} {self.wanted_product}s for {Store.products[self.wanted_product]["price"]*self.wanted_quantity}$!")
                Store.products[self.wanted_product]["quantity_in_store"] -=  self.wanted_quantity
        except Exception as e:
            print(str(e))

iphone = Store("IPhone", 2000, 200)
fax = Store("Fax machine", 300, 15)
computer = Store("Computer", 4000, 30)
cigarettes = Store("Cigarettes", 45.9, 4000)

customer = Customer()

customer.purchase_item("IPhone", 4000, 10 )
customer.purchase_item("faxxmachine", 4000, 1 )
customer.purchase_item("computer", 90000000, 1000 )
customer.purchase_item("cigarettes", -10, 1)
customer.purchase_item("iphone", 1, -20)
customer.purchase_item("iphone", 5000, 1)

########################################################################################
class Store:
    products = {}

    def __init__(self, product, price, quantity_in_store):
        self.product = product.lower()  # שמירה באותיות קטנות
        self.price = price
        self.quantity_in_store = quantity_in_store
        self.products[self.product] = {"price": self.price, "quantity_in_store": self.quantity_in_store}


class Customer:
    def __init__(self):
        self.wanted_product = None
        self.wanted_quantity = None
        self.budget = None

    def purchase_item(self, wanted_product, budget, wanted_quantity):
        self.wanted_product = wanted_product.lower()  # המרה לאותיות קטנות
        self.budget = budget
        self.wanted_quantity = wanted_quantity

        try:
            if self.wanted_quantity <= 0:
                raise ValueError("❌ Wanted quantity must be above 0$")

            if self.budget <= 0:
                raise ValueError("❌ Your budget must be above 0$")

            if self.wanted_product not in Store.products:
                raise ValueError("❌ Product not in store or mistype.")

            real_product_name = self.wanted_product  # משתמשים בשם הנכון

            if self.wanted_quantity > Store.products[real_product_name]["quantity_in_store"]:
                raise ValueError(
                    f"❌ Not enough items in store. You can only buy {Store.products[real_product_name]['quantity_in_store']} {real_product_name}s.")

            if self.budget < Store.products[real_product_name]["price"] * self.wanted_quantity:
                raise ValueError(f"❌ Your budget is too low.\n"
                                 f"For {self.budget}$ you can buy {self.budget // Store.products[real_product_name]['price']} {real_product_name}s.\n"
                                 f"Each {real_product_name} costs {Store.products[real_product_name]['price']}$.")

            print(
                f"✅ Purchase successful!\nYou just bought {self.wanted_quantity} {real_product_name}s for {Store.products[real_product_name]['price'] * self.wanted_quantity}$!")
            Store.products[real_product_name]["quantity_in_store"] -= self.wanted_quantity

        except Exception as e:
            print(str(e))


# מוצרים בחנות – השמות נשמרים באותיות קטנות!
iphone = Store("IPhone", 2000, 200)
fax = Store("Fax machine", 300, 15)
computer = Store("Computer", 4000, 30)
cigarettes = Store("Cigarettes", 45.9, 4000)

# בדיקות עם אותיות גדולות וקטנות
customer = Customer()
customer.purchase_item("IPhone", 4000, 10)  # ✅ עובד גם באותיות גדולות
customer.purchase_item("IPHONE", 5000, 1)  # ✅ עובד גם באותיות רנדומליות
customer.purchase_item("iphone", 5000, 1)  # ✅ עובד גם באותיות קטנות
customer.purchase_item("Fax MACHINE", 5000, 1)  # ✅ עובד בכל שילוב אותיות!
