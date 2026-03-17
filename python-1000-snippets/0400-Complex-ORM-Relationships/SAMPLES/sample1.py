# sample1.py
# Demonstrates a one-to-many relationship using SQLAlchemy.

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
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.orm import declarative_base, relationship, Session

    Base = declarative_base()

    class Parent(Base):
        __tablename__ = "parent"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        children = relationship("Child", back_populates="parent")

        def __repr__(self):
            return f"<Parent(id={self.id}, name={self.name})>"

    class Child(Base):
        __tablename__ = "child"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        parent_id = Column(Integer, ForeignKey("parent.id"))
        parent = relationship("Parent", back_populates="children")

        def __repr__(self):
            return f"<Child(id={self.id}, name={self.name}, parent_id={self.parent_id})>"

    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        mom = Parent(name="Mom", children=[Child(name="Alice"), Child(name="Bob")])
        session.add(mom)
        session.commit()

        print("Parents and children:")
        for parent in session.query(Parent).all():
            print(parent)
            for child in parent.children:
                print("  ", child)


if __name__ == "__main__":
    main()
