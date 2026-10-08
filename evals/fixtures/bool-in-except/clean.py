class NotEnoughMoney(Exception):
    pass


def charge(order, amount):
    order.pay(amount)
    return amount


def is_paid(order):
    return order.status == "paid"
