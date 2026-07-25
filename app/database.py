from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from contextlib import contextmanager

DATABASE_URL="postgresql://taskuser:taskpass@localhost:5432/taskdb"

engine=create_engine(DATABASE_URL)

Session=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

@contextmanager
def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()