from uuid import uuid4

from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import UUID

from sqlalchemy.orm import Mapped

from sqlalchemy.orm import mapped_column

from sqlalchemy.dialects.postgresql import UUID as PG_UUID

# classe base que é pai de todas as outras classes e vamos importar ela nas outras classes da nossa API

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)