from typing import Annotated, Optional

from pydantic import UUID4, Field

from pydantic import PositiveFloat

from workout_api.categories.schemas import CategoriesIn
from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.training_center.schemas import TrainingCenterAthlete

class Athlete(BaseSchema):
    name: Annotated[str, Field(description="Athlete's name", example="Jhon", max_length=50)]
    cpf: Annotated[str, Field(description="Athlete's CPF", example="12345678911", max_length=11)]
    age: Annotated[int, Field(description="Athlete's age", example=23)]
    weight: Annotated[PositiveFloat, Field(description="Athlete's weight", example=76.3)]
    height: Annotated[PositiveFloat, Field(description="Athlete's height", example=1.75)]
    gender: Annotated[str, Field(description="Athlete's gender", example="M", max_length=1)]
    category: Annotated[CategoriesIn, Field(description="Athlete category")]
    training_center: Annotated[TrainingCenterAthlete, Field(description="Athlete training center")]
    
class AthleteIn(Athlete):
    super

class AthleteOut(Athlete, OutMixin):
    super

class AthleteUpdate(BaseSchema):
    name: Annotated[Optional[str], Field(None,description="Athlete's name", example="Jhon", max_length=50)]
    age: Annotated[Optional[int], Field(None,description="Athlete's age", example=23)]
    weight: Annotated[Optional[PositiveFloat], Field(None,description="Athlete's weight", example=76.3)]
    height: Annotated[Optional[PositiveFloat], Field(None,description="Athlete's height", example=1.75)]
    category: Annotated[Optional[CategoriesIn], Field(None,description="Athlete category")]
    training_center: Annotated[Optional[TrainingCenterAthlete], Field(None,description="Athlete training center")]