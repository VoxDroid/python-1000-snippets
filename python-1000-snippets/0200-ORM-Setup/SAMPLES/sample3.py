# sample3.py
# insert and query using sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    engine = create_engine("sqlite:///sample3.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # add a record
    session.add(Person(name="Bob"))
    session.commit()
    # query
    bob = session.query(Person).filter_by(name="Bob").first()
    print("Found person:", bob.name if bob else None)
    session.close()
