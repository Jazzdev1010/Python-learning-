# typecasting list to set
t=["a", "b", "c"]
print(type(t))
s = set(t)
print(type(s))

s.add("d")
s.add(10)
print(s)