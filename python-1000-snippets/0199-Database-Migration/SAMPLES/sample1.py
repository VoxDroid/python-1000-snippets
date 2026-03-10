# sample1.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
print("Table created")

