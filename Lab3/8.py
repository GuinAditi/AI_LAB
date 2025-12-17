stack = []

while True:
    print("\n1.Push  2.Pop  3.Display  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        stack.append(val)

    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")

    elif choice == 3:
        print("Stack:", stack)

    elif choice == 4:
        break
