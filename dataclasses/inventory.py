"""
You're building an inventory system and need a flexible,
feature-rich Product class. This class should store a product's details,
support custom methods, handle default values, and demonstrate control over __repr__ and comparisons.
@dataclass is the ideal choice here.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True, order=True)
class Product:
    product_id: str
    name: str
    price: float
    quantity: int
    description: str = "no description"
    tags: list[str] = field(default_factory=list)

    def get_value(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:
        return f"Product(product_id={self.product_id!r}, name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f} ({self.quantity} in stock)"

    # Method to validate prices
    def __post_init__(self):
        if self.price < 0:
            print(f"Warning: negative price detected for {self.name}\n resetting to 0.")
            object.__setattr__(self, "price", 0.0)
        if self.quantity < 0:
            print(
                f"Warning: negative quantity detected for {self.name}\n resetting to 0."
            )
            object.__setattr__(self, "quantity", 0.0)


p_laptop = Product(
    "L001",
    "Laptop",
    1200.0,
    5,
    "High-performance laptop",
    tags=["electronics", "computers"],
)
p_mouse = Product("M001", "Gaming Mouse", 50.0, 10)
p_invalid = Product("INV01", "Invalid Item", -5.0, -2)
p_laptop_alt = Product(
    "L001", "Laptop", 1200.0, 5, "Another description", tags=["computers"]
)
products = [p_laptop, p_mouse, p_laptop_alt]
for i in products:
    print(i)
