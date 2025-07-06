# i=0
# while(i<9):
#     print(i)
#     i+=1

# for i in range(9):  ## start from 0 -> end in 8
#     print(i)

# for i in range(4,101,4):   #  4 -> 100 and jump 4
#     print(i)

# print("twice - ")

# j=0
# while(j<101):
#     print(j)
#     j+=4


li=["susovan",9087,"pupai",True,7654,False,"Bye"]
tu=("mimi",False,987,234,"ABCD",48,90,"hii",False,"UYTR")
st="zYASYxFDFGHHJyZKKlooXaiuuygbYZnnmzxYqwzx"
skip="XYZxyz"

for i in range(908):
    pass    ## Do nothing for now, but keep the code syntactically correct.

# use in list
for i in li:
    print(i)
else:
    print("-> List print Done.")

# use in tuple
for i in tu:
    if(i==48):
        break
    print(i)
else:
    print("-> tuple print done!")

# string
for i in st:
    if(i in skip):
        continue  ## skip if exist x y z
    print(i)
else:
    print("-> string print done!")