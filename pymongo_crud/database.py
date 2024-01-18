from urllib.parse import quote_plus
from mongoengine import connect
from mongoengine.connection import get_connection
from models import User

uri = 'mongodb://127.0.0.1:27017/practice'

try:
    connect(host=uri)
    print("Connected to MongoDB Atlas using MongoEngine!")
    

except Exception as e:
    print("Error:", e)
    
    
user = User(email='hello2@gmail.com', name='Aravind')
user.save()
