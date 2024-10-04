from typing import List

from sqlalchemy import Column, ForeignKey, Table, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


bookmark_category_link_table = Table(
    "bookmark_category_link",
    Base.metadata,
    Column("bookmark_id", ForeignKey("bookmark.id")),
    Column("category_id", ForeignKey("category.id")),
)


class Category(Base):
    __tablename__ = "category"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"


class Bookmark(Base):
    __tablename__ = "bookmark"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    categories: Mapped[List[Category]] = relationship(
        secondary=bookmark_category_link_table
    )


def database_engine():
    return create_engine(
        "postgresql://rosetta:g9fKklfPCrRivrqYYMltc48C@localhost:5432/postgres"
    )
