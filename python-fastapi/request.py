from pydantic import BaseModel


class AddCategoryRequest(BaseModel):
    name: str
