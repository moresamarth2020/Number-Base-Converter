def base_converter():
    print("----- NUMBER BASE CONVERTER -----\n")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice: ")

        if choice == "1":
            num = int(input("Enter decimal number: "))
            print("Binary:", bin(num)[2:])

        elif choice == "2":
            num = int(input("Enter decimal number: "))
            print("Octal:", oct(num)[2:])

        elif choice == "3":
            num = int(input("Enter decimal number: "))
            print("Hexadecimal:", hex(num)[2:].upper())

        elif choice == "4":
            num = input("Enter binary number: ")
            print("Decimal:", int(num, 2))

        elif choice == "5":
            print("Exiting converter.")
            break

        else:
            print("Invalid choice. Try again.")

base_converter()
