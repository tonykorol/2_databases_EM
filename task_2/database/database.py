from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = DeclarativeBase()

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
