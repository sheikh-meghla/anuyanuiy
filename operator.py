numbers = [1, 2, 3, 4, 5]

count = len(numbers)
if count > 4:
    print(f"List has {count} elements")

if (count := len(numbers)) > 4:
    print(f"List has {count} elements")
