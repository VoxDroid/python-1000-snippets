# sample2.py
# define a simple declarative model and create its table
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    engine = create_engine("sqlite:///sample2.db")
    Base.metadata.create_all(engine)
    print("created table for", Item.__tablename__)

