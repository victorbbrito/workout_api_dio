from workout_api.contrib.models import BaseModel

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy.orm import Mapped

from sqlalchemy.orm import mapped_column

from sqlalchemy.orm import relationship


class TrainingCenterModel(BaseModel):
    __tablename__ = "training_centers"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True,nullable=False)
    address: Mapped[str] = mapped_column(String(60), nullable=False)
    owner: Mapped[str] = mapped_column(String(30), nullable=False)
    athlete: Mapped['AthleteModel'] = relationship(back_populates='training_center')
    