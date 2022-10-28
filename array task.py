#find the maximum and minimum element of the array
array1=[1,2,3,4,5]
print(max(array1))
print(min(array1))

#arr[]={1,5,3,2}
# Give a random set of numbers, print them in sorted order

array1={2,4,1,5,6,7}
b=list(array1)
print(sorted(b))

#write a program to reversed array
arr1=[2,5,6,9]
arr1.reverse()
print(arr1)
#create 3 arrays and find the common element this array
arr3=[1,2,6,4,8]
arr4=[5,6,7,8,9]
arr5=[2,4,6,7,8]
set1=set(arr3)
set2=set(arr4)
set3=set(arr5)
n1=set1.intersection(set2,set3)
print(n1)
#using for loop
arr3=[1,2,6,4,8]
arr4=[5,6,7,8,9]
arr5=[2,4,6,7,8]
for i in arr3:
    if i in arr4 and arr5:
      print(i)

#find the factorial of a number using array




