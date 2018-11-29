from mongoengine import Document, StringField, IntField

class VehicleInfo(Document):
    model = StringField()
    fee = IntField()
    image = StringField()
    year = IntField()