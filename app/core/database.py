from sqlalchemy import create_engine, Column, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

env = os.getenv("ENVIRONMENT")
if env == "test":
    DATABASE_URL = "sqlite:///./test_db.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TimeStampedBaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
