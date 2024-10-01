from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"


def database_engine():
    return create_engine(
        "postgresql://rosetta:g9fKklfPCrRivrqYYMltc48C@localhost:5432/postgres"
    )
