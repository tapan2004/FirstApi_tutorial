from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Tmanna@localhost:5432/FastApiDb"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
     autoflush=False,
      bind=engine
      )