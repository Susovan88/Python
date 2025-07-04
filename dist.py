dist={
    "susovan" :123,
    "Ram":89,
    "sam":87,
    90:"sammi"
}
dist.update({"sam":99,"pupai":100})  ## update if exist, if not exist then add element
print(dist,type(dist))
print(dist.items())  # infrom of tuple
print(dist.keys()) 
print(dist.values())

print(dist.get("sam"))
print(dist["sam"])

pop1=dist.pop("Ram")
pop2=dist.popitem()  # remove last key value pair and retutn
print(pop1,pop2,dist)

print(dist.get("tani"))  ## if exist then give vale , if not exist then give none
# print(dist["tani"])   ## if exist then give vale , if not exist then give error


dist2={
    "Ram":[89,34,56],
    "sam":[94,8,91],
    "pupai":[87,57,72],
    "tani":[12,34,90],
    "mimi":[12,45,67],
}
print(dist2)
dist2["pupai"]=[99,89,19] ## dist is mutable 
print(dist2)

dist2["Ram"].sort()
dist2["pupai"].sort()
dist2["sam"].sort()

print(dist2)

n=input("Enter name :")
print(dist2[n])
n=input("Enter name :")
print(dist2[n])
n=input("Enter name :")
print(dist2[n])
 


