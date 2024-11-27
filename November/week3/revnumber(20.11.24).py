def read_number():
    while True:
        try:
            # Prompt the user for input
            num = int(input("Enter a number (minimum 4 digits): "))
            
            # Check if the number has at least 4 digits
            if num >= 1000:  # Check if the number has at least 4 digits
                return num
            else:
                print("Please enter a number with at least 4 digits.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def reverse_number(num):
    reverse = 0
    while num > 0:
        # Get the last digit of the number
        last_digit = num % 10
        # Add the last digit to the reverse number
        reverse = reverse * 10 + last_digit
        # Remove the last digit from the number
        num = num // 10
    return reverse

# Read a number from the user
number = read_number()

# Find the reverse of the number
reversed_number = reverse_number(number)

# Display the original number and its reverse
print(f"The original number is: {number}")
print(f"The reverse of the number is: {reversed_number}")

