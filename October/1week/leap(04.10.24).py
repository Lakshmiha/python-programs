year=int(input("Enter the final year:"))
current_year=int(input("Enter the current year:"))
for i in range(current_year,year):
    
    if(i%4==0 and year%100!=0)or (year%400==0):
        print(i)
