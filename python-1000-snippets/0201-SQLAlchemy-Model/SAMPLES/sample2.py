# sample2.py
# update an existing User and then delete
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
    user = session.query(User).first()
    if user:
        user.name = "Alice Updated"
        session.commit()
        print("Updated user to", user.name)
        session.delete(user)
        session.commit()
        print("Deleted user")
    else:
        print("No user to update")
    session.close()
