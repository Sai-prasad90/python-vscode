# Program 0
# dict and dict2 refer to the same dictionary
dict = {
    "firstName": "sai",
    "lastName": "wate",
    "email": "01saiprasad@gmail.com",
    "rollNo": 25
}
dict2 = dict
dict2['no'] = 9011212430
print(dict2)  # {'firstName': 'sai', 'lastName': 'wate', 'email': '01saiprasad@gmail.com', 'rollNo': 25, 'no': 9011212430}
print(dict)   # {'firstName': 'sai', 'lastName': 'wate', 'email': '01saiprasad@gmail.com', 'rollNo': 25, 'no': 9011212430}

# Program 1
# copy()
dict3 = {
    "firstName": "sai",
    "lastName": "prasad"
}
dict4 = dict3.copy()
dict4['lastName'] = "wate"
print(dict4)  # {'firstName': 'sai', 'lastName': 'wate'}
print(dict3)  # {'firstName': 'sai', 'lastName': 'prasad'}

# Program 2
# update()
info1 = {
    "color": "Black",
    "model": "gls"
}
info2 = {
    "regNo": 656468
}
info2.update(info1)
print(info1)  # {'color': 'Black', 'model': 'gls'}
print(info2)  # {'regNo': 656468, 'color': 'Black', 'model': 'gls'}

# Program 3
# popitem()
info3 = {
    "color": "black",
    "mobileNumber": 90112124,
    "city": "pune"
}
info3.popitem()
print(info3)  # {'color': 'black', 'mobileNumber': 90112124}

# Program 4
# setdefault()
info4 = {
    "city": 134,
    "district": 34,
    "state": 29
}
info4.setdefault("city", "345")
print(info4)  # {'city': 134, 'district': 34, 'state': 29}

# Program 5
props = ["fn", "ln", "age"]
info5 = dict.fromkeys(props, 0)
print(info5)  # {'fn': 0, 'ln': 0, 'age': 0}
