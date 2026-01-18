from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Define the shape of your data (The Schema)
class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    tax: float = 0.1

# 2. Define the POST endpoint
@app.post("/products/")
async def create_product(product: Product):
    # FastAPI automatically parses the JSON body into the 'product' object
    total_price = product.price + (product.price * product.tax)
    
    return {
        "message": "Product created successfully",
        "product_name": product.name,
        "total_cost": total_price
    }