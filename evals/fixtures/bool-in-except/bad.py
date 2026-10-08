class NotEnoughMoney(Exception):
    pass


def charge(order, amount):
    try:
        order.pay(amount)
    except NotEnoughMoney:
        return False
    return True


def lookup(key, table):
    try:
        return table[key]
    except KeyError:
        return None
