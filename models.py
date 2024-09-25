from sqlalchemy import Column,Integer,String,Float,Table,MetaData
metadata=MetaData()
products=Table(
  "products",
  metadata,
  Column("id",Integer,primary_key=True),
  Column("name",String(100)),
  Column("description",String(250)),
  Column("price",Float),
  Column("inventory_count",Integer),
  Column("category",String(50)),
  Column("popularity_score",Float,default=0.0),
  
)