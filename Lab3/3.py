lst = list(map(int, input("Enter list elements: ").split()))

total = sum(lst)
avg = total / len(lst)

print("Sum =", total)
print("Average =", avg)
