from fastapi import FastAPI, HTTPException
from crud import get_product, get_all_products, create_product, update_product, delete_product, search_products
from schemas import ProductCreate, ProductUpdate, Product

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/products/", response_model=Product)
async def create_new_product(product: ProductCreate):
    return await create_product(product.dict())


@app.get("/products/", response_model=list[Product])
async def read_all_products():
    return await get_all_products()


@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    product = await get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.put("/products/{product_id}", response_model=Product)
async def update_existing_product(product_id: int, product: ProductUpdate):
    updated_product = await update_product(product_id, product.dict())
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    product = await delete_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


@app.get("/search/")
async def search_product(query_param: str):
    return await search_products(query_param)
