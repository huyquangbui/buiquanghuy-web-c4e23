from mongoengine import Document, StringField, IntField, BooleanField

class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()

class CusInfo(Document):
    username = StringField()
    password = StringField()
    # email = StringField()