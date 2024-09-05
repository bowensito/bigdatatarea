from pymongo import *

def get_db():
    client = MongoClient('mongodb+srv://cluster0.rzmj2.mongodb.net/',
                         27017, connect=False, username='mongoadmin', password='root')
    db = client["universidad"]
    return db
