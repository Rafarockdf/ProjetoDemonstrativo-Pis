from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


user = "postgres"
password = "rafa7887"
database = "analiseprecos"
host = "localhost"
port = "5433"


SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()