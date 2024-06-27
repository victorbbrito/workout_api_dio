from typing import Annotated

from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchema

class TrainingCenter(BaseSchema):
    name: Annotated[str, Field(description="Training center name", example="Training Center of Commander", max_length=50)]
    address: Annotated[str, Field(description="Training center address", example="7609 Mckinley Avenue, Los Angeles, California", max_length=60)]
    owner: Annotated[str, Field(description="Training center owners name", example="McLovin", max_length=30)]


class TrainingCenterIn(TrainingCenter):
    super


class TrainingCenterOut(TrainingCenter):
    id: Annotated[UUID4, Field(description='Training center identifier')]
 
   
class TrainingCenterAthlete(BaseSchema):
    name: Annotated[str, Field(description="Training center name", example="Training Center of Commander", max_length=50)]