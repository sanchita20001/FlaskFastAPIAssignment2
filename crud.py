from models import products
from database import database

async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)

async def get_all_products():
    query = products.select()
    return await database.fetch_all(query)

async def create_product(product):
    query = products.insert().values(**product)
    product_id = await database.execute(query)
    return {**product, "id": product_id}

async def update_product(product_id: int, product):
    query = products.update().where(products.c.id == product_id).values(**product)
    await database.execute(query)
    return await get_product(product_id)

async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    return await database.execute(query)

async def search_products(query_param: str):
    query = products.select().where(
        (products.c.name.ilike(f"%{query_param}%")) |
        (products.c.description.ilike(f"%{query_param}%")) |
        (products.c.category.ilike(f"%{query_param}%"))
    )
    return await database.fetch_all(query)
