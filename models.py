# for data validation
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: str

    # def __init__(self, id: int, name: str, price: float, quantity: int, description: str = "No description available"):
    #     self.id = id
    #     self.name = name
    #     self.price = price
    #     self.quantity = quantity
    #     self.description = description