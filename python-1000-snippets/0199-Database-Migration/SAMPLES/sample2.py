# sample2.py
# mock adding column
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)  # new field
engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
print("Added email column (if not exists)")

