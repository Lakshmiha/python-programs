def check_lengths(intg_list1, intg_list2):
    Len1 = len(intg_list1)
    Len2 = len(intg_list2)

    if Len1 == Len2:
        print("Lengths are same", Len1, Len2)
    else:
        print("Lengths are not same", Len1, Len2)

def check_sums(intg_list1, intg_list2):
    Sum1 = sum(intg_list1)
    Sum2 = sum(intg_list2)

    if Sum1 == Sum2:
        print("Sums are equal", Sum1, Sum2)
    else:
        print("Sums are not equal", Sum1, Sum2)

def check_common_values(intg_list1, intg_list2):
    common_values = set(intg_list1) & set(intg_list2)
    if common_values:
        print("Common values:", common_values)
    else:
        print("No common values")

def menu():
    intg_list1 = []
    intg_list2 = []

    while True:
        print("\nMenu:")
        print("1. Enter List 1")
        print("2. Enter List 2")
        print("3. Check lengths of List 1 and List 2")
        print("4. Check sums of List 1 and List 2")
        print("5. Check common values between List 1 and List 2")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            intg_list1 = list(map(int, input("Enter List 1 elements (comma separated): ").split(',')))
        elif choice == '2':
            intg_list2 = list(map(int, input("Enter List 2 elements (comma separated): ").split(',')))
        elif choice == '3':
            check_lengths(intg_list1, intg_list2)
        elif choice == '4':
            check_sums(intg_list1, intg_list2)
        elif choice == '5':
            check_common_values(intg_list1, intg_list2)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

# Calling the menu function will start the program
menu()

