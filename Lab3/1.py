

# Input list
print("Enter list elements separated by space:")
lst = list(map(int, input("> ").split()))

# Insert operation
print("\nINSERT OPERATION")
pos = int(input("Enter position to insert: "))
val = int(input("Enter value to insert: "))
lst.insert(pos, val)
print("List after insertion:", lst)

# Delete operation
print("\nDELETE OPERATION")
del_val = int(input("Enter value to delete: "))
if del_val in lst:
    lst.remove(del_val)
    print("List after deletion:", lst)
else:
    print("Value not found in list")

# Search operation
print("\nSEARCH OPERATION")
search = int(input("Enter value to search: "))
if search in lst:
    print("Value found at index:", lst.index(search))
else:
    print("Value not found")


