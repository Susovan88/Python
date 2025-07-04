a=(1,2,3,6,4,7,5,9,"qweasd",False,"asxzc",90,"dsqwmvb",True)
print(type(a))
print(a)
#Because tuples are immutable, you can’t add, remove, or change their elements.
#So there are no methods like append(), remove(), or sort() that lists have.
no=a.count(9)
idx=a.index(False)
print(no,idx)
print(len(a))

# a[2]="paul"  # it is immutable. so not prossible


l2=[23,67,1,2,3,0]
print(sum(l2))


marks=[]
m1=int(input("Enter marks : "))
marks.append(m1)
m2=int(input("Enter marks : "))
marks.append(m2)
m3=int(input("Enter marks : "))
marks.append(m3)

m4=int(input("Enter marks : "))
marks.append(m4)
m5=int(input("Enter marks : "))
marks.append(m5)
marks.sort()
print(marks)