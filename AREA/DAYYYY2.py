print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of Circle =", int(area))

    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of Rectangle =", int(area))

    elif choice == 3:
        side = float(input("Enter side: "))
        area = side * side
        print("Area of Square =", int(area))

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
