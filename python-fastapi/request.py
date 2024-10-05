from typing import List

from pydantic import AliasGenerator, BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class AddCategoryRequest(BaseModel):
    name: str


class AddBookmarkRequest(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: to_camel(field_name)
        )
    )

    name: str
    url: str
    category_ids: List[str]
