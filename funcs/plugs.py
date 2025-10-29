"""
You're building a system that processes a list of Product objects (let's use our @dataclass from before). You want to allow users to specify different sorting criteria via a simple string command, and also register custom "plugins" (functions) that can analyze the products.
"""
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price: float
    weight: float = 1.0
    stock: int = 0

Products = [
    Product("P001", "Laptop", 1200.0, 2.5, 10),
    Product("P002", "Mouse", 25.0, 0.1, 50),
    Product("P003", "Keyboard", 150.0, 1.0, 20),
    Product("P004", "Monitor", 300.0, 5.0, 5),
    Product("P005", "Webcam", 75.0, 0.2, 30),
]
def sortProducts(productList, criteria):
    pass
def run_plugin(plugin_func, product_list):
    pass
def count_high_value_items(products: list[Product]) -> int:
    pass


