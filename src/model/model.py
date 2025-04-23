import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

load_dotenv()
engine = create_async_engine(os.getenv("SQLALCHEMY_DATABASE_URL"))

session_local = async_sessionmaker(engine, autocommit=False)

Base = declarative_base()

async def get_db():
    async with session_local() as session:
        yield session   