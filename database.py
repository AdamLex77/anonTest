from datetime import datetime
import pymongo
import gridfs
import pytz


class DataBase:
    def __init__(self):
        self.dataset, self.storage, self.database = self.connect()

    def connect(self):
        mongod = pymongo.MongoClient(
            "mongodb+srv://cool:susuboneto123@cluster0.kbtznjt.mongodb.net/?retryWrites=true&w=majority")

        database = mongod["TABLE"]

        dataset = database["COLLECTIONS"]

        storage = gridfs.GridFS(database)

        return dataset, storage, database

    def search(self, user_id=None, allEntry=None):
        if allEntry:
            result = self.dataset.find()
        else:
            result = self.dataset.find_one({"_id": user_id})

        return result

    def insert(self, user_id, name, username, age, tempat):
        # time-stamp
        IST = pytz.timezone('Asia/Jakarta')
        time_stamp = datetime.now(IST).strftime('%Y-%m-%d || %H:%M:%S')

        self.dataset.insert_one({"_id": user_id,
                                 "name": name,
                                 "username": username,
                                 "timestamp": time_stamp,
                                 "umur": age,
                                 "domisili": tempat})

    def update(self, user_id, new_data):
        self.dataset.update_one({"_id": user_id}, {"$set": new_data})

    def umur(self, age, new_data):
        self.dataset.update_one({"umur": age}, {"$set": new_data})
    
    def dom(self, tempat, new_data):
        self.dataset.update_one({"domisili": tempat}, {"$set": new_data})
