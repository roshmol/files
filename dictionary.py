student={'name':'abc','rolll_no' : 1,'mark':[10,20,30]}
print(student)
print(type(student))
print(type(student))

#accessing dicg items

student={'name':'abc','rolll_no' : 1,'mark':[10,20,30]}
print(student['name'])
print(student['mark'])

#accessing using get method

student={'name':'abc','rolll_no' : 1,'mark':[10,20,30]}
print(student.get('mark'))

#accessing keys

print(student.keys())

#add a record
student={'name':'abc','rolll_no' : 1,'mark':[10,20,30]}
student['age']=12
print(student)

#accessing values
student={'name':'abc','rolll_no' : 1,'mark':[10,20,30]}
print(student.values())
#accessing items
student={'name':'abc','rolll_no' : 1,'mark':[10,20,30]}
student.popitem()
print(student)

#using delete method
student={'name':'abc','roll_no' :1,'mark':[10,20,30]}
del student['roll_no']
print(student)

#for loop in dict
d1={'fruits':'apple','number':1,'color':'red','price':10}
for i in d1:
    print(d1 [i])

#using function
d1={'fruits':'apple','number':1,'color':'red','price':10}
for i in d1.keys():
    print(i)
# using function
d1 = {'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}
for i,j in d1.items():
    print(i,j)

#making a copy method
#1 copy method
new=d1.copy()
print(new)

#nested dictionaries
main={'student':{'name':'abc','rolll_no' : 1,'mark':[10,20,30]},'d1':{'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}}
print(main)

#dict method
new1=dict(d1)
print(new1)





