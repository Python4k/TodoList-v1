from typing import Optional
from sqlalchemy import Date, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column


from app.database.db import Base



class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False, server_default=func.now())
    updated_at: Mapped[Date] = mapped_column(Date, nullable=False, server_default=func.now(), onupdate=func.now())
    deadline: Mapped[Date] = mapped_column(Date, nullable=False, server_default=func.now())


    def __repr__(self) -> str:
        return f"<Todo(id={self.id}, title={self.title}, description={self.description})>"
