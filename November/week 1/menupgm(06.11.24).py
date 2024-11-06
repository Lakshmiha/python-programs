num=int(input("Enter number of elements to the list:"))
no_list=[]
for i in range(num):
    element=int(input("Enter elements:"))
    no_list.append(element)
print(no_list)
while True:
    print("\nMenu")
    print("1.Greatest and smallest")
    print("2.Sorting")
    print("3.create another list")
    print("4.exit")
    choice=input("Enter your choice (1-4):")

    if choice=='1':
        print("The greatest no is:",max(no_list))
        print("The smallest no is:",min(no_list))

    elif choice=='2':
        print("sorted list:",sorted(no_list))

    elif choice=='3':
        even_nos=[]
        for n in no_list:
            if n%2==0:
                even_nos.append(n)
        print("The even numbers list is:",even_nos)

    elif choice==4:
        print("exit")
        break
    else:
        print("Invalid choice!!")
