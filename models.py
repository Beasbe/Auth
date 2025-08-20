from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class CredsModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
