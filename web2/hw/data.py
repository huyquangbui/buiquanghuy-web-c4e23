from mongoengine import Document, StringField, IntField, ListField

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

class Quiz(Document):
    category = StringField()
    type1 = StringField()
    difficulty = StringField()
    question = StringField()
    correct_answer = StringField()
    incorrect_answers = ListField()