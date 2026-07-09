from fastapi import FastAPI
from database import SessionLocal, engine
from databaseModels import Base, Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def fun():
    return "Hello, World!"

@app.get("/products")
def get_all_products():
    # db connection
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return {"products": products}