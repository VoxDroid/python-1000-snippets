# sample1.py
# Demonstrates query limiting and indexing with SQLAlchemy.

import subprocess
import sys


def ensure_sqlalchemy():
    try:
        import sqlalchemy  # type: ignore
        return sqlalchemy
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sqlalchemy"])  # nosec
        import sqlalchemy  # type: ignore
        return sqlalchemy


def main() -> None:
    sqlalchemy = ensure_sqlalchemy()
    from sqlalchemy import Column, Integer, String, create_engine
    from sqlalchemy.orm import declarative_base, Session

    Base = declarative_base()

    class Item(Base):
        __tablename__ = "item"
        id = Column(Integer, primary_key=True)
        name = Column(String, index=True)

        def __repr__(self):
            return f"<Item(id={self.id}, name={self.name})>"

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all([Item(name=f"Item {i}") for i in range(1, 101)])
        session.commit()

        # Limit results to avoid fetching everything.
        limited = session.query(Item).limit(5).all()
        print("Limited query (5 items):", limited)


if __name__ == "__main__":
    main()
