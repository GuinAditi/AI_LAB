lst = list(map(int, input("Enter list elements: ").split()))

freq = {}
for x in lst:
    freq[x] = freq.get(x, 0) + 1

print("Frequency of elements:")
print(freq)
