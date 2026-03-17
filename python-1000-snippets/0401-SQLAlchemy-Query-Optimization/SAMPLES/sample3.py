# sample3.py
# Demonstrates select statement building and performance-friendly execution.

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
    from sqlalchemy import Column, Integer, String, create_engine, select
    from sqlalchemy.orm import declarative_base, Session

    Base = declarative_base()

    class Product(Base):
        __tablename__ = "product"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        price = Column(Integer, nullable=False)

        def __repr__(self):
            return f"<Product(id={self.id}, name={self.name}, price={self.price})>"

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all(
            [
                Product(name="Widget", price=10),
                Product(name="Gadget", price=20),
                Product(name="Thing", price=15),
            ]
        )
        session.commit()

        stmt = select(Product).where(Product.price > 10).order_by(Product.price)
        results = session.execute(stmt).scalars().all()
        print("Products priced > 10:", results)


if __name__ == "__main__":
    main()
