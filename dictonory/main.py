##dictonory
'''
*it is combination of key and value pair
*in key is unique(single)
*in values store the int,float,string and boolen'''
'''
d={}
print(type(d))
output:
<class 'dict'>

d={"name":"krishnan","age":20}
print(d)

output:
{'name': 'krishnan', 'age': 20}
'''
#funtion:

#pop()=> remove the key value pair
'''
d={"name":"krishnan","age":20}
d.pop("age")
print(d)

output:
{'name': 'krishnan'}
'''
#key()=> print the keys
'''
d={"name":"krishnan","age":20}
print(d.keys())

output:
dict_keys(['name', 'age'])

d={"name":"krishna","age":20}
print(d["name"])

output:
krishna
'''
#values()=> print the values
'''
d={"name":"krishnan","age":20}
print(d.values())
 
output:
dict_values(['krishnan', 20])

d={"name":"krishnan","age":20,"phone":[8008449079,9492925563,6302456449]}
print(d["phone"])

output:
[8008449079, 9492925563, 6302456449]
'''
#item()=> print the combination of key and pair
'''
d={"name":"krishnan","age":20,"phone":[8008449079,9492925563,6302456449]}
print(d.items())

output:
dict_items([('name', 'krishnan'), ('age', 20), ('phone', [8008449079, 9492925563, 6302456449])])
'''
#update({})=> added the key and value pair
'''
d={"name":"krishnan","age":20,"phone":[8008449079,9492925563,6302456449]}
d.update({"addr":"chemalamarri"})
print(d)

output:
{'name': 'krishnan', 'age': 20, 'phone': [8008449079, 9492925563, 6302456449], 'addr': 'chemalamarri'}
'''
#clear()=> delete the dictonary
'''
d={"name":"krishnan","age":20,"phone":[8008449079,9492925563,6302456449]}
d.clear()
print(d)

output:
{}
'''