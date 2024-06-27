from workout_api.contrib.schemas import BaseSchema

from typing import Annotated

from pydantic import UUID4, Field

class Categories(BaseSchema):
    name: Annotated[str, Field(description="Category name", example="Scale", max_length=20)]


class CategoriesIn(Categories):
    super

class CategoriesOut(Categories):
    id: Annotated[UUID4, Field(description='Category identifier')]