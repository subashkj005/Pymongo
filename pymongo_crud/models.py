from mongoengine import Document, StringField, EmailField

class User(Document):
    email = EmailField()
    name = StringField(max_length=20)
