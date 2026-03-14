# sample3.py
# Index creation and querying with a filter
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['python_snippets']
    users = db['users']
    users.delete_many({})
    users.insert_many([{'name': 'Carol', 'score': 10}, {'name': 'Dave', 'score': 20}])
    users.create_index('score')
    high = list(users.find({'score': {'$gt': 15}}))
    print('High score users:', [u['name'] for u in high])

