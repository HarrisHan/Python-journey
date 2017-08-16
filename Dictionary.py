empty = {}
user = {"email": "harrishan@gmail.com", "workId": 14}

# use dict keyword it's just a habit
empty = dict()
user = dict({"email": "harrishan@gmail.com", "workId": 14})

# access
# print(user['adress']) # KeyError

# update dict
user['email'] = 'harris@ha.com'
user['address'] = "Nanjing"
user.update({'address': 'Nanjing'}) # advantages can update many

#delete
# delattr(user['address'])
# delattr(user)
user.clear() # clear all key & value

# 1.do not use same key in dict
user = dict({"email": "@@@", "workId": 11, "workId": 10})
print(user)

# 2.key must be read only so it can be string number tuple but not list
user = dict({"email": "@@@", "workId": 11, (11, 1101): "floor&Room"})
# user = dict({"email": "@@@", "workId": 11, [11, 1101]: "floor&Room"}) # TypeError: unhashable type: 'list'

# support
user = {"email": "harrishan@gmail.com", "workId": 14}
print(user.keys())
print(user.values())

print('email' in user)
print ("email" in user.keys()) # slower than ('email' in user)
