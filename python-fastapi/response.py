from dataclasses import dataclass
from typing import List, Self, Tuple, Union

from pydantic import AliasGenerator, BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from sqlalchemy import Row

from database import Bookmark, Category


@dataclass
class CategoryResponse:
    id: str
    name: str

    @classmethod
    def from_category(cls, category: Union[Category, Row[Tuple[Category]]]) -> Self:
        return cls(id=str(category.id), name=category.name)


class DeleteCategoryResponse(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            serialization_alias=lambda field_name: to_camel(field_name)
        )
    )

    is_deleted: bool


class BookmarkResponse(BaseModel):
    id: str
    name: str
    url: str
    categories: List[CategoryResponse]

    @classmethod
    def from_bookmark(cls, bookmark: Union[Bookmark, Row[Tuple[Bookmark]]]) -> Self:
        return cls(
            id=str(bookmark.id),
            name=bookmark.name,
            url=bookmark.url,
            categories=list(
                map(
                    lambda category: CategoryResponse.from_category(category),
                    bookmark.categories,
                )
            ),
        )


class DeleteBookmarkResponse(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            serialization_alias=lambda field_name: to_camel(field_name)
        )
    )

    is_deleted: bool
