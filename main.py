from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def fun():
    return "Hello, World!"

# products = [
#         {"id": 1, "name": "Product 1", "price": 10.99, "quantity": 100},
#         {"id": 2, "name": "Product 2", "price": 19.99, "quantity": 50},
#         {"id": 3, "name": "Product 3", "price": 5.99, "quantity": 200}
# ]

products = [
    Product(1, "Product 1", 10.99, 100, "Description for Product 1"),
    Product(2, "Product 2", 19.99, 50, "Description for Product 2"),
    Product(3, "Product 3", 5.99, 200, "Description for Product 3")
]

@app.get("/products")
def get_products():
    return {"products": products}