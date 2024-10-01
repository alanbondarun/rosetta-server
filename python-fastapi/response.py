from dataclasses import dataclass
from typing import Self, Tuple, Union

from sqlalchemy import Row

from database import Category


@dataclass
class CategoryResponse:
    id: str
    name: str

    @classmethod
    def from_category(cls, category: Union[Category, Row[Tuple[Category]]]) -> Self:
        return cls(id=str(category.id), name=category.name)
