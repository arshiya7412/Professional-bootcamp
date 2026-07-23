a = 100
b = a
print(a)
print(b)
print(id(a))
print(id(b))

a = 500
print("After Reassignment:")
print("a =", a)
print("b =", b)
print(id(a))
print(id(b))

#task 1
x = 42
y = x
print(x)
print(y)
print(id(x))
print(id(y))

#task 2
x = 99
print(x)
print(y)
print(id(x))
print(id(y))

#task 3
p = 7
q = p
r = q
print(id(p))
print(id(q))
print(id(r))

#task 4
name1 = "Arshiya"
name2 = name1
name1 = "Sana"

print(name1)
print(name2)