from pymongo import MongoClient
from homeapp import db


class User():
    default_message = "You're Great!"
    def __init__(self, username, email, password, dateCreated):
        self.username = username
        self.email = email
        self.encrypted_pass = password
        self.personal_message = self.default_message
        self.dateCreated = dateCreated
    
    def buildJSON(self):
        self.user_entry = {
            'name': f"{self.username}",
            'email': f"{self.email}",
            'password': f"{self.encrypted_pass}",
            'message': f"{self.personal_message}",
            'date_created': f"{self.dateCreated}"
        }
        return self.user_entry
    def setMessage(self, message):
        self.personal_message = message
    

class DB():
    def __init__(self):
        self.conn = MongoClient('mongodb://db1:27017,db2:27017,db3:27017/?replicaSet=mongo-cluster')
        self.db = self.conn.homeapp
    
    def userExist(self, email):
        collection = self.db.Users
        if(collection.find_one({'email':f"{email}"})):
            self.conn.close()
            return True
        else:
            self.conn.close()
            return False
    
    def getUser(self, email):
        collection = self.db.Users
        user = collection.find_one({'email':f"{email}"})
        self.conn.close()
        return user
    
    def addUser(self, user):
        collection = self.db.Users
        try:
            collection.insert_one(user)
            self.conn.close()
            return True
        except:
            self.conn.close()
            return False

