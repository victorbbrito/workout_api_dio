from workout_api.contrib.models import BaseModel

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy import Float

from sqlalchemy import DateTime

from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped

from sqlalchemy.orm import mapped_column

from sqlalchemy.orm import relationship

from datetime import datetime

from workout_api.training_center.models import TrainingCenterModel


class AthleteModel(BaseModel):
    __tablename__ = 'athletes'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    gender: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    category: Mapped['CategoriesModel'] = relationship(back_populates='athlete', lazy='selectin')
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.pk_id'))
    training_center: Mapped['TrainingCenterModel'] = relationship(back_populates="athlete", lazy='selectin')
    training_center_id: Mapped[int] = mapped_column(ForeignKey('training_centers.pk_id'))
    
    
    
    
    
    