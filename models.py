"""
ByteBites backend models.

Classes:
  Customer  - stores a customer's name and order history; verifies real users.
  Menu      - holds the full catalog of FoodItems; supports add, remove, and filter by category.
  Order     - groups selected FoodItems into one transaction and computes the total cost.
  Payment   - records and processes the payment for a completed Order.
"""

from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class FoodItem:
    name: str
    price: float
    category: str
    popularity_rating: float


@dataclass
class Customer:
    name: str
    past_purchases: list[Order] = field(default_factory=list)

    def verify_user(self) -> bool:
        return bool(self.name)

    def add_to_history(self, order: Order) -> None:
        self.past_purchases.append(order)


@dataclass
class Menu:
    items: list[FoodItem] = field(default_factory=list)

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        self.items.remove(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        return [item for item in self.items if item.category == category]


@dataclass
class Order:
    customer: Customer
    items: list[FoodItem] = field(default_factory=list)

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def compute_total(self) -> float:
        return sum(item.price for item in self.items)


@dataclass
class Payment:
    order: Order
    status: str = "pending"

    def process_payment(self) -> bool:
        self.status = "paid"
        return True


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 8.50, "Mains", 4.7)
    soda   = FoodItem("Large Soda",   2.00, "Drinks", 4.2)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)

    alice = Customer("Alice")
    order = Order(customer=alice)
    order.add_item(burger)
    order.add_item(soda)

    pay = Payment(order=order)
    pay.process_payment()
    alice.add_to_history(order)

    print(menu.filter_by_category("Drinks"))  # [FoodItem(name='Large Soda', ...)]
    print(order.compute_total())              # 10.5
    print(pay.status, alice.verify_user())   # paid True
