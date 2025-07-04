e=set() # empty set
d1={} # empty dist
print(type(e),type(d1))

s={12,778,2,987,2234,122,23,2,3,2,3,7,2,3,4,7} ## unordered , have unique elemnts , can not access element by index
t={778,90,2,4,65,9,23,54,34,7}
s1={12,23,2,4}
s2={12,23,121,2}

print(s,type(s))
s.remove(122)
s.add(123)
print(s)
# s.pop() ## remove random element
print(s.union(t))   ## a+b  (no duplicate elements)
print(s.intersection(t)) ## common b/w s & t

print(s-t) #s-t
print(s1.issubset(s))
print(s2.issubset(s))

a=set()
a.add(18)
a.add('18')
a.add(18.0)   # 1==1.0 ? -> True 
print(a,len(a))



# b={1,2,4,8,[1,2,3]} # gives error ->  Sets in Python can only contain hashable (immutable) items.
#[1,2,3] => mutable

b={1,2,3,5,(1,3,5),"susovan Paul"} # correct 
print(b)
b.add("pupaI")
b.add((9,7,5))
print(b)





