# sample2.py
# Demonstrate update and delete operations
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['python_snippets']
    users = db['users']
    users.delete_many({})
    users.insert_one({'name': 'Bob', 'age': 25})
    users.update_one({'name': 'Bob'}, {'$set': {'age': 26}})
    updated = users.find_one({'name': 'Bob'})
    print('Updated age:', updated.get('age'))
    users.delete_one({'name': 'Bob'})
    print('Remaining docs:', users.count_documents({}))

