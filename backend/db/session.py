from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings


engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"charset": 'utf8'})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

