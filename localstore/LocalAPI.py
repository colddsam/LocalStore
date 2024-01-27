from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from pydantic import BaseModel
from localstore.LocalStore import LocalStore
import uvicorn


class Product(BaseModel):
    name: str = ''
    main_category: str = ''
    sub_category: str = ''
    image: str = ''
    link: str = ''
    ratings: str = ''
    no_of_ratings: str = ''
    discount_price: str = ''
    actual_price: str = ''


app = FastAPI()
myObj = LocalStore()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class LocalAPI:

    @app.get('/')
    async def root_page() -> str:
        return "This Project is for making a public Local Store API and Package"

    @app.get("/products/show/")
    def Show_product_List(product_name: Annotated[str, Query(...)] = '') -> dict:
        res = myObj.Show_product_List(product_name=product_name)
        return res

    @app.get("/products/random/")
    async def Show_Random_Product() -> dict:
        res = myObj.Show_Random_Product()
        return res

    @app.post("/products/insert/{product_name}")
    async def Add_New_Product(product_name: str, data: Product) -> dict:
        res = myObj.Add_New_Product(item_name=product_name, data=data.__dict__)
        return res

    @app.get("/data/show/")
    async def Show_Data(index: Annotated[str, Query(...)] = '') -> dict:
        res = myObj.Show_Data(index=index)
        return res

    @app.delete("/data/delete/")
    async def Delete_Data(index: Annotated[str, Query(...)] = '') -> dict:
        res = myObj.Delete_Data(index=index)
        return res

    @app.post("/items/insert/{product_name}")
    async def Add_New_Item(product_name: str = '') -> dict:
        res = myObj.Add_New_Item(item_name=product_name)
        return res

    @app.get('/items/show/')
    async def Show_Items() -> dict:
        res = myObj.Show_Items()
        return res

    def runServer(application=app) -> None:
        config = uvicorn.Config(application, port=5000, log_level="info")
        server = uvicorn.Server(config)
        server.run()
