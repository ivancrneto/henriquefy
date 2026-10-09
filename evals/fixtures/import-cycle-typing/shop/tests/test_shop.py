from shop.customers import Customer
from shop.orders import Order


def test_order_keeps_its_customer():
    customer = Customer()
    assert Order(customer).customer is customer
