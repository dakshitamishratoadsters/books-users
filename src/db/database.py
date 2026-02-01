from sqlmodel import SQLModel, create_engine, Session
from src.config import Config

# Create sync engine
engine = create_engine(
    Config.DATABASE_URL,
    echo=True
)

# Create tables
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependency for routes
def get_session():
    with Session(engine) as session:
        yield session
