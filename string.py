b="pupslajhwf"
c='jnsiufhiuweh'
a='''ygkubljhouhfeiuhou'''

name="sUsOvAn PAuL"  # string are immutable which means yoy can not change the string using buildin functions
nameshort=name[1:4] # start from 1 to 3 (excluding 4)
ch=name[1]
print("name is - ",name)
print("length is ", len(name))
print(name.swapcase())
print(name.upper())
print(name.count('s'))
print("nume start with 'susa' - ",name.startswith("susa"))
print("nume ends with 'aul' - ",name.endswith("aul"))
print("find 'ovan' in name index is ", name.find("ovan"))  # find 
print("replace 'PAuL' to 'dey' ", name.replace('PAuL','dey'))
print(nameshort.capitalize())  # first charecter capitalize
print(name.capitalize())
print(nameshort)
print(ch)

print(name[-4:-1])
print(name[1:4]) 

print(name[:4]) # name[0:4]
print(name[2:]) # name[2:len(name)]
print(name[2:len(name)])

print(name[2:len(name):3])

num="1234567890"
print(len(num))
print(num[3:8])
print(num[3:8:2])

a="I am a good boy \n but not a bad boy. \n\t BYE!!! \n  \"Susovan Paul\" "
print(a)

"""

✅ String Methods in Python
Method	Description
capitalize()	Converts the first character to uppercase.
casefold()	Converts string to lowercase (more aggressive than lower()).
center(width)	Returns a centered string of given width.
count(substring)	Returns the number of times a substring occurs.
encode()	Returns an encoded version of the string.
endswith(suffix)	Checks if the string ends with the given suffix.
expandtabs(tabsize)	Replaces tabs with spaces.
find(substring)	Returns the lowest index of the substring or -1.
format()	Formats string using placeholders.
format_map(mapping)	Formats string using a mapping object (like a dict).
index(substring)	Same as find() but raises error if not found.
isalnum()	Checks if all characters are alphanumeric.
isalpha()	Checks if all characters are alphabetic.
isascii()	Checks if all characters are ASCII.
isdecimal()	Checks if all characters are decimal.
isdigit()	Checks if all characters are digits.
isidentifier()	Checks if string is a valid Python identifier.
islower()	Checks if all characters are lowercase.
isnumeric()	Checks if all characters are numeric.
isprintable()	Checks if all characters are printable.
isspace()	Checks if all characters are whitespace.
istitle()	Checks if string follows title case.
isupper()	Checks if all characters are uppercase.
join(iterable)	Joins elements of an iterable with string as separator.
ljust(width)	Left aligns the string within specified width.
lower()	Converts string to lowercase.
lstrip()	Removes leading whitespace.
maketrans()	Creates a mapping table for translation.
partition(sep)	Splits string at first occurrence of sep.
replace(old, new)	Replaces substring with another substring.
rfind(substring)	Returns highest index of substring or -1.
rindex(substring)	Same as rfind() but raises error if not found.
rjust(width)	Right aligns the string within specified width.
rpartition(sep)	Splits string at last occurrence of sep.
rsplit(sep)	Splits string from the right.
rstrip()	Removes trailing whitespace.
split(sep)	Splits string into a list.
splitlines()	Splits string at line breaks.
startswith(prefix)	Checks if string starts with the given prefix.
strip()	Removes leading and trailing whitespace.
swapcase()	Swaps case of all characters.
title()	Converts string to title case.
translate(table)	Returns a translated string using the mapping table.
upper()	Converts string to uppercase.
zfill(width)	Pads string on the left with zeros to fill width.

"""

