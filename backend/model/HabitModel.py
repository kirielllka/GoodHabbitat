from backend.database import BaseModel

from sqlalchemy import String,Integer

from sqlalchemy.orm import Mapped, mapped_column

class HabitModel(BaseModel):
    __tablename__ = "habits"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    user_tg_id : Mapped[int] = mapped_column(Integer, nullable=False)
    habit : Mapped[str] = mapped_column(String, nullable=False)
    unit : Mapped[str] = mapped_column(String, nullable=False)
    count : Mapped[int] = mapped_column(Integer, nullable=False)

    