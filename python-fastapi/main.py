from typing import Annotated
from uuid import uuid4

from fastapi import Depends, FastAPI
from fastapi.params import Query
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from database import Bookmark, Category, database_engine
from parameter import GetBookmarksParams
from request import AddBookmarkRequest, AddCategoryRequest
from response import BookmarkResponse, CategoryResponse, DeleteBookmarkResponse, DeleteCategoryResponse

app = FastAPI()


@app.get("/category")
def get_categories(
    database_connection: Annotated[Engine, Depends(database_engine)],
    name: str | None = None,
):
    with database_connection.connect() as connection:
        result = connection.execute(select(Category))
        if name:
            result = filter(
                lambda category: name.lower() in category.name.lower(), result
            )
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


@app.get("/bookmark")
def get_bookmarks(
    database_connection: Annotated[Engine, Depends(database_engine)],
    params: Annotated[GetBookmarksParams, Query()],
):
    with Session(database_connection) as session:
        bookmarks = session.query(Bookmark)
        if params.category_id:
            bookmarks = filter(
                lambda bookmark: any(
                    str(category.id) == params.category_id
                    for category in bookmark.categories
                ),
                bookmarks,
            )
        return list(
            map(lambda bookmark: BookmarkResponse.from_bookmark(bookmark), bookmarks)
        )


@app.post("/bookmark")
def create_bookmark(
    request: AddBookmarkRequest,
    database_connection: Annotated[Engine, Depends(database_engine)],
):
    with Session(database_connection) as session:
        categories = list(
            session.scalars(
                select(Category).where(Category.id.in_(request.category_ids))
            ).all()
        )

        bookmark = Bookmark(
            id=str(uuid4()),
            name=request.name,
            url=request.url,
            categories=categories,
        )

        session.add(bookmark)
        session.commit()

        return BookmarkResponse.from_bookmark(bookmark)


@app.delete("/bookmark/{bookmark_id}")
def delete_bookmark(
    bookmark_id: str,
    database_connection: Annotated[Engine, Depends(database_engine)],
):
    with Session(database_connection) as session:
        bookmark = session.get(Bookmark, bookmark_id)
        if bookmark:
            session.delete(bookmark)
            session.commit()
        return DeleteBookmarkResponse(is_deleted=bool(bookmark))
