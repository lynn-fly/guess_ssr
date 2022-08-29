# -*-coding:utf-8-*-
# fix to ModuleNotFound
import sys; sys.path = ['', '..'] + sys.path[1:]
import logging
from backend.db.init_db import init_db
from backend.db.session import engine, SessionLocal
from backend.db.base import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()

