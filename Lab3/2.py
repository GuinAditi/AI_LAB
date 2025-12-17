lst = list(map(int, input("Enter list elements: ").split()))

unique = []
for x in lst:
    if x not in unique:
        unique.append(x)

print("List without duplicates:", unique)
