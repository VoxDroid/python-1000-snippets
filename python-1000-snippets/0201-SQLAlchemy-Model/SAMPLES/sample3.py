# sample3.py
# demonstrate filtering and multiple inserts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    engine = create_engine("sqlite:///model1.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    # add two users
    session.add_all([User(name="Bob"), User(name="Carol")])
    session.commit()
    # filter
    users = session.query(User).filter(User.name.like("B%"))
    print("Users starting with B:", [u.name for u in users])
    session.close()
