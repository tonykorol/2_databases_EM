from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    basis_name: str
    volume: int
    total: int
    count: int
    date: str
