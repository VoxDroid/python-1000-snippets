# 0214-MongoDB-Connection Cheatsheet

* Install Python driver: `pip install pymongo`.
* Start MongoDB server (`mongod`) on default port 27017.
* Connect: `client = MongoClient('mongodb://localhost:27017/')`.
* Select database: `db = client['mydb']`.
* Select collection: `collection = db['users']`.
* Insert document: `collection.insert_one({'name': 'Alice'})`.
* Query document: `collection.find_one({'name': 'Alice'})`.
* Update document: `collection.update_one({'name': 'Alice'}, {'$set': {'age': 30}})`.
* Delete document: `collection.delete_one({'name': 'Alice'})`.
* Use indexes for fast queries: `collection.create_index('name')`.
* Handle `pymongo.errors.ConnectionFailure` if MongoDB is not running.
* For advanced use, use `with client.start_session()` and `with session.start_transaction()` for transactions.

