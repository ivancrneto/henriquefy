from shop.customers import Customer


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
