from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.settings import database_settings


engine = create_async_engine(
    f'postgresql+asyncpg://{database_settings.user}:{database_settings.password}@{database_settings.host}/{database_settings.db}'
)
SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


async def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        await session.close()
