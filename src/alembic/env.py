import os
import asyncio
import model

from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from model.model import Base
from dotenv import load_dotenv

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

load_dotenv()
url = os.getenv("SQLALCHEMY_DATABASE_URL")

def run_migrations_offline():
    """Executa migrações no modo offline."""
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Executa migrações no modo online."""
    connectable = create_async_engine(url, future=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    """Configura e executa as migrações."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())