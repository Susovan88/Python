friends=["pupai","taniya",True,90.67,"susovan",123]

print(friends[0])
print(friends[3])
friends[5]="Ram"  # lists are mutable
friends[1]=1278   # lists are mutable
print(friends[1])  
print(friends[5])
print(friends[0:5])
print(friends[3:6])

friends.append("samm")  # push-back
print(friends)
friends.insert(3,"Paul")  # in the 3 index insert the element
print(friends)
value=friends.pop(6)  # remove element from this index
friends.remove("samm")
print(value)
print(friends)

l1=[1,2,5,10,23,12,3,89,12]
l1.sort()
print(l1)
l1.reverse()
print(l1)
