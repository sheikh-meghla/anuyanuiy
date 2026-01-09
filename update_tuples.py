# Updating Tuples
x = ("apple", "banana", "cherry", "orange", "grape")
y = ("kiwi", "melon",)
x += y


y = list(x)
y.remove("grape")
del y[0]
y[3] = "kiwi"
x = tuple(y)
y.append("mango")

print(x)