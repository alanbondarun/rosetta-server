from typing import Annotated
from uuid import uuid4

from fastapi import Depends, FastAPI
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from database import Category, database_engine
from request import AddCategoryRequest
from response import CategoryResponse, DeleteCategoryResponse

app = FastAPI()


@app.get("/category")
def get_categories(database_connection: Annotated[Engine, Depends(database_engine)]):
    with database_connection.connect() as connection:
        result = connection.execute(select(Category))
        return list(
            map(lambda category: CategoryResponse.from_category(category), result)
        )


@app.post("/category")
def create_category(
    request: AddCategoryRequest,
    database_connection: Annotated[Engine, Depends(database_engine)],
):
    with Session(database_connection) as session:
        category = Category(id=str(uuid4()), name=request.name)
        session.add(category)
        session.commit()
        return CategoryResponse.from_category(category)


@app.delete("/category/{category_id}")
def delete_category(
    category_id: str,
    database_connection: Annotated[Engine, Depends(database_engine)],
):
    with Session(database_connection) as session:
        category = session.get(Category, category_id)
        if category:
            session.delete(category)
            session.commit()
        return DeleteCategoryResponse(is_deleted=bool(category))
