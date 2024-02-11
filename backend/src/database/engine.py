from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import configuration

db = configuration.database

SQLALCHEMY_DATABASE_URL = f"postgresql://{db.user}:{db.password}@{db.server}:{db.password}/{db.name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

