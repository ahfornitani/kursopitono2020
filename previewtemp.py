# identeca operaciilo
x = 3
y = x
z = 3
print(x is y)  # True
print(y is z)  # True
print(x is not z)  # False

listo_a = [1, 2, 3]
listo_b = listo_a
listo_c = [1, 2, 3]

print(listo_a is listo_b)  # True
print(listo_b is listo_c)  # False
print(listo_a is not listo_c)  # True
