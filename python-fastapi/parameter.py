from pydantic import AliasGenerator, BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class GetBookmarksParams(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: to_camel(field_name),
            serialization_alias=lambda field_name: to_camel(field_name),
        )
    )

    category_id: str | None = None
