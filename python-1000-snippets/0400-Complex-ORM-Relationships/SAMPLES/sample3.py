# sample3.py
# Demonstrates eager loading and query options with SQLAlchemy.

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
    from sqlalchemy import Column, Integer, String
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
        author_id = Column(Integer, sqlalchemy.ForeignKey("author.id"))
        author = relationship("Author", back_populates="books")

        def __repr__(self):
            return f"<Book(id={self.id}, title={self.title})>"

    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        author = Author(name="Jane Austen")
        author.books = [Book(title="Pride and Prejudice"), Book(title="Sense and Sensibility")]
        session.add(author)
        session.commit()

        # Use joinedload to eager-load related books in a single query.
        author_with_books = session.query(Author).options(joinedload(Author.books)).first()
        print(author_with_books)
        print("Books:", author_with_books.books)


if __name__ == "__main__":
    main()
