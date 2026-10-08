from shop import billing


def place(order):
    return billing.charge(order)
