#print set ,find type and length of the set
a={'apple','orenge','cherry','gua'}
print(a)
print(type(a))
print(len(a))

#tuple to set
b={'apple','orenge','cherry','gua'}
print(set(b))

#accessing set items
a={'apple','orenge','cherry','gua'}
for i in a:
    print(i)

#print new value,remove and discard item,discard function didn't shoe any error
a={'apple','orenge','cherry','gua'}
a.add('banana')
print(a)
a.remove('apple')
print(a)
a.discard('orange')
print(a)

#add a set to another set
a={'apple','orenge','cherry','gua'}
b={1,2,3,4,5}
a.update(b)
print(a)
#add lis to set
a={'apple','orenge','cherry','gua'}
b=['a','b']
b={1,2,3,4,5}
a.update(b)
print(a)


#join sets
#union,intersection
a={'apple','orenge','cherry','gua'}
b={1,2,3,4,5}
a.update(b)
print(a)
# intersection,intersection_update
a={'apple','orenge','cherry','gua','a'}
b={1,2,3,4,5,'a'}
d=a.intersection(b)
print(d)
# symmetric,difference,symmetric difference_update
a={'apple','orenge','cherry','gua','a'}
b={1,2,3,4,5,'a'}
d=a.symmetric_difference(b)
print(d)


