import mongoengine

# mongodb://admin:admin@ds021182.mlab.com:21182/c4e


host = "ds161346.mlab.com"
port = 61346
db_name = "movies"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())