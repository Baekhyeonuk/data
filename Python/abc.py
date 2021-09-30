

import json

# some JSON:
#x = ´{ "name":"John", "age":30, "city":"New York"}´
file = open("abc.json","r")

x = file.read()
y = json.loads(x)

# the result is a Python dictionary:
#print(y)

for key, value in y.items():
    print("키 값은 {}이고 항목은 {}입니다".format(key,value))
