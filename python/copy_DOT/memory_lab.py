a = [1,2,3]
b = a
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))


print("swallow copy of a")
c = a.copy()
print("Append 5 into c")
c.append(5)
print(f" c -> {c} ")

print(f" a -> {a} ")

