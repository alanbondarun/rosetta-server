from typing import Annotated
from fastapi import Depends, FastAPI
from sqlalchemy import Engine, select

from database import Category, database_engine
from response import CategoryResponse

app = FastAPI()


@app.get("/category")
def get_categories(database_connection: Annotated[Engine, Depends(database_engine)]):
    with database_connection.connect() as connection:
        result = connection.execute(select(Category))
        return list(
            map(lambda category: CategoryResponse.from_category(category), result)
        )
