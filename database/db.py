from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database url for connection 
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Argument: connect_args only for sqlite not for other database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Each instance of the SessionLocal class will be a database session. 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Later we will inherit from this class to create each of the database models or classes (the ORM models)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
