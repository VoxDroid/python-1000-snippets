# sample2.py
# Demonstrates eager loading with joinedload to reduce round-trip queries.

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
    from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
    from sqlalchemy.orm import declarative_base, relationship, Session, joinedload

    Base = declarative_base()

    class Author(Base):
        __tablename__ = "author"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        books = relationship("Book", back_populates="author")

        def __repr__(self):
            return f"<Author(id={self.id}, name={self.name})>"

    class Book(Base):
        __tablename__ = "book"
        id = Column(Integer, primary_key=True)
        title = Column(String, nullable=False)
        author_id = Column(Integer, ForeignKey("author.id"))
        author = relationship("Author", back_populates="books")

        def __repr__(self):
            return f"<Book(id={self.id}, title={self.title})>"

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        author = Author(name="Jane")
        author.books = [Book(title="Book A"), Book(title="Book B")]
        session.add(author)
        session.commit()

        # Eager-load books so the ORM does not issue extra queries per author.
        authors = session.query(Author).options(joinedload(Author.books)).all()
        for a in authors:
            print(a, "->", a.books)


if __name__ == "__main__":
    main()
