from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import declarative_base # type: ignore

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread":False}
)

Base = declarative_base()
