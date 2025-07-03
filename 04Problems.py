space="Sus  ovan Pa  ul is a goo  d  B  oy"
print(space.find("  "))
print(space.count("  "))
print(space.replace("  ",""))


name=input("Enter you name: ")
print(f"Good morning, {name}. How are you? (good or bad)")
fill=input(" -> ")
print("Great!!!")
date=input("Please enter the date - ")
letter='''
Dear <|Name|>,
You are Selected For You Internship, duration is 6 months.
you joining date is <|Date|>. See you soon. BYE!!!
ph - 8910769487

'''

print(letter.replace("<|Name|>",name).replace("<|Date|>",date))

