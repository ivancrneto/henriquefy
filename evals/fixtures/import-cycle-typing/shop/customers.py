from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shop.orders import Order


class Customer:
    def orders(self) -> "list[Order]":
        return []
