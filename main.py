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
    Product(id=1, name="Product 1", price=10.99, quantity=100, description="Description for Product 1"),
    Product(id=2, name="Product 2", price=19.99, quantity=50, description="Description for Product 2"),
    Product(id=3, name="Product 3", price=5.99, quantity=200, description="Description for Product 3")
]

@app.get("/products")
def get_products():
    return {"products": products}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return {"product": product}
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully", "product": product}

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    for index, existing_product in enumerate(products):
        if existing_product.id == id:
            products[index] = product
            return {"message": "Product updated successfully", "product": product}
    return {"error": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            deleted_product = products.pop(index)
            return {"message": "Product deleted successfully", "product": deleted_product}
    return {"error": "Product not found"}