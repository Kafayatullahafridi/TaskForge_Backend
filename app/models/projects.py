from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from sqlalchemy import ForeignKey
from app.models.users import User

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]= mapped_column(String(100))
    description: Mapped[str|None] = mapped_column(String(500),nullable=True)
    owner_id:Mapped[int] =mapped_column(ForeignKey("users.id"))