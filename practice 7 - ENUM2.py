import enum

class OrderStatus(enum.Enum):
    PENDING = "Pending"
    PREPARING = "Preparing"
    READY = "Ready"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class Order:
    def __init__(self, order_id, client_name):
        self.order_id = order_id
        self.client_name = client_name
        self.order_status =  OrderStatus.PENDING

    def update_status(self, new_status):
        if self.order_status == OrderStatus.COMPLETED:
            print(f"🚫 Cannot change status after {self.order_status.value}.")
        if not self.order_status == OrderStatus.COMPLETED:
            self.order_status = new_status
            print(f"✅ Order No.{self.order_id} for {self.client_name} is now {self.order_status.value}.")




lily = Order(32, "Lily")

lily.update_status(OrderStatus.PREPARING)
lily.update_status(OrderStatus.READY)
lily.update_status(OrderStatus.COMPLETED)


lily.update_status(OrderStatus.CANCELED)


david = Order(33, "David")
david.update_status(OrderStatus.CANCELED)
ron = Order(41, "Ron")
ron.update_status(OrderStatus.COMPLETED)
ron.update_status(OrderStatus.PENDING)