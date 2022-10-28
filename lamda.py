#lambda function
x=lambda a:a+10
a=0
print(x(5))

#two parameters
x=lambda a,b:a+b
print(x(2,3))

#nested lambda
def function(n):
    return lambda a:a*n
result=function(10)
print(result(10))

