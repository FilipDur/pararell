import datetime

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Objednávka {self.order_id}: {self.quantity}x {self.product} ({self.date.strftime('%H:%M:%S')})"
