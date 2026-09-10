from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
import os
load_dotenv()

engine = create_async_engine(f"postgresql+asyncpg://"
                             f"{os.getenv('PG_USER')}:"
                             f"{os.getenv('PG_PASSWORD')}@"
                             f"{os.getenv('PG_HOST')}"
                             f"/{os.getenv('PG_BD')}", future=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_session():
    async with new_session() as session:
        yield session

class BaseModel(DeclarativeBase):
    pass