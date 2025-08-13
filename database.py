from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

user = "uekkhbapqr25vhjk"
password = "J7k925l9eAT41hnzXrFm"
host = "b3rdmbq3ap25mkv6xgub-mysql.services.clever-cloud.com"
port = "3306"
database = "b3rdmbq3ap25mkv6xgub"
DATABASE_URL = f"mysql+aiomysql://{user}:{password}@{host}:{port}/{database}"

# 建立 Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# 建立 SessionLocal（AsyncSession）
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base 類別
Base = declarative_base()

# Dependency: 提供 DB Session
async def get_db():
	async with AsyncSessionLocal() as session:
		yield session