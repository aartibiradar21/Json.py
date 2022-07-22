# Q4.Python dictionary(sort by key) object ko json data :
# :mai convert karne ka program likho?

# import json


# a={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}

# myfile=json.dumps(a,sort_keys=True,indent=3)
# print(myfile)


# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])
# print(y["name"]) 




# file=open("my_file1.json","x")

# import json
# d={"name":"aarti","age":18,"college":"navgurukul"}
# file=open("my_file1.json","w")
# json.dump(d,file)


# import json
# d='{"name":"aarti","age":18,"college":"navgurukul"}'
# a=json.loads(d)
# print(a)