from fastapi.testclient import TestClient
from app.database import get_db
import pytest
from app.main import app

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
from sqlalchemy.orm import sessionmaker
from app.database import Base
from alembic import command



SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:alen1234@localhost:5432/fastapi_test'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
    # connect_args={"sslmode": "require"})

TestingSessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

@pytest.fixture(scope="function")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)