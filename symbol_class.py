from typing import List
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .user_class import User

symbols_metadata = MetaData()

class Base(DeclarativeBase):
    pass

class Symbol(Base):
    __tablename__ = 'symbols'
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    symbol_id: Mapped[List["User"]] = relationship(back_populates="Symbol")