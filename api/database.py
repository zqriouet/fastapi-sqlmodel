from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, echo=True)


def get_db():
    with Session(engine) as session:
        yield session
