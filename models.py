"""
ByteBites backend models.

Classes:
  Customer  - stores a customer's name and order history; verifies real users.
  Menu      - holds the full catalog of FoodItems; supports add, remove, and filter by category.
  Order     - groups selected FoodItems into one transaction and computes the total cost.
  Payment   - records and processes the payment for a completed Order.
"""