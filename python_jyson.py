import json
x='{"name":"rosh","age":21,"city":"nilambur"}'
#print(x(name))
y=json.loads(x)#parsing
print(y["name"])

#python convert to json
x1={"name":"rosh","age":21,"city":"nilambur"}
y1=json.dumps(x1)
print(y1)

print(json.dumps(["apple","banana","orenge"]))