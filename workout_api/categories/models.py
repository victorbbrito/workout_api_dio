from workout_api.contrib.models import BaseModel

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy.orm import Mapped

from sqlalchemy.orm import mapped_column

from sqlalchemy.orm import relationship


class CategoriesModel(BaseModel):
    __tablename__ = "categories"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    athlete: Mapped['AthleteModel'] = relationship(back_populates='category')
    