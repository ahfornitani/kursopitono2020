some_list = [10, 20, 30, 40]

for index, item in enumerate(some_list):
    print(f"This is the index: {index}, and this is the item: {item}")

a = 5
b = 10
a, b = b, a
print(f"\n a = {a}, b = {b}")

print("\n >> a, b = b, a")
print(f"Now swapped: a = {a}, b = {b}")

a = 9
b = 11
c = 44

a, (b, c) = 1, (2, 3)
print("\n >> a, (b, c) = 1, (2, 3)")
print(f"a = {a}, b = {b}, c = {c}")

x, y, z = 1, 2, 3
print("\n >> x, y, z = 1, 2, 3")
print(f"x = {x}, y = {y}, z = {z}")


a, *rest = [1, 2, 3]
# a = 1, rest = [2, 3]
print("\n >> a, *rest = [1, 2, 3]")
print(f"a = {a}, rest = {rest}")

a, *middle, c = [1, 2, 3, 4]
# a = 1, middle = [2, 3], c = 4
print("\n >> a, *middle, c = [1, 2, 3, 4]")
print(f"a = {a}, middle = {middle}, c = {c}")
