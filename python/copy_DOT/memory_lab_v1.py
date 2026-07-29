import copy
a = [[1],[2]]
b = a.copy() # swallow copy of a
c = copy.copy(a)
d = copy.deepcopy(a)


# Now append a value in both b and c

print("Testing swallow copy")
b.append(5)
c.append(6)
b[0].append(9)
print(a, b, c, sep="\n")

print("Now testing deepcopy")

print(f"Unchanged d -> {d}")

d[0].append(10)
print(d)
