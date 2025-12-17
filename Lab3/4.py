lst = list(map(int, input("Enter list elements: ").split()))

i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

lst[i], lst[j] = lst[j], lst[i]

print("After swapping:", lst)
