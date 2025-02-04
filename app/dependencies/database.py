from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.models.auction_result import Base 
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_tables():
    Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

create_tables()
