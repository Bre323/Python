import json


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Leo', 25)


def encode(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('The object is not JSON serializable')


userJSON = json. dumps(user, default=encode)
print(userJSON)


def decode(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode)
print(type(user))
print(user.name)


'''


from json import JSONEncoder


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age}
        return JSONEncoder.default(self, o)

userJSON2 = UserEncoder(). encode(user)
print(userJSON2)
'''
