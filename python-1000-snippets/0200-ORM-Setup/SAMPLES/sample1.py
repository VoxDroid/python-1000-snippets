# sample1.py
# basic ORM setup: create engine and open/close a session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("sqlite:///sample1.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Engine URL:", engine.url)
    session.close()
    print("session closed")
