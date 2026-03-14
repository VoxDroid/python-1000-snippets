# sample1.py
# Basic MongoDB insert/find example using pymongo
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['python_snippets']
    users = db['users']
    users.delete_many({})
    users.insert_one({'name': 'Alice'})
    doc = users.find_one({'name': 'Alice'})
    print('Found:', doc.get('name'))

