import os
from shop import pricing


def total(order):
    from shop import taxes

    return pricing.subtotal(order) + taxes.for_order(order)


def ship(order):
    from . import shipping
    import json

    return shipping.quote(order), json.dumps(order), os.sep
