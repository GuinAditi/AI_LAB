n = int(input("Enter number of key-value pairs: "))
d = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Dictionary contents:")
for k, v in d.items():
    print(k, ":", v)
