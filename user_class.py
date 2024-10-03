from typing import List
from sqlalchemy import ForeignKey, String, BigInteger, MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from core.settings import dbconfigs
from .symbol_class import Symbol

url = f"postgresql+asyncpg://{dbconfigs.db_login}:{dbconfigs.db_pass}@{dbconfigs.db_host}/{dbconfigs.db_name}"
engine = create_async_engine(url, echo=True)
user_metadata = MetaData()
async_session = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    fk_id: Mapped[int] = mapped_column(ForeignKey("symbols.symbol_id"))
    user_id: Mapped[List["Symbol"]] = relationship(back_populates="user")
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger)
    symbol: Mapped[str] = mapped_column(String)
    sheet_id: Mapped[BigInteger] = mapped_column(BigInteger, nullable=True)


async def connectdb():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all())