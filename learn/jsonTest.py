import json

#python 字典类型转换为 json

data = {'no':1,'name':"leiyang",'age':21}

json_str = json.dumps(data)

print("Python 原始数据:" +  repr(data))
print("json 数据:"+json_str)


data2 = json.loads(json_str)

print(data2['name'])
print(data2['age'])
