def reverse(input_string):
    return input_string[::-1]
def isPalindrome(input_string):
    reversed_string=reverse(input_string)
    if(input_string==reversed_string):
        return True
    return False
str=input("enter a string:")
result=isPalindrome(str)
if(result == 1):
    print("Is palindrome")
else:
    print("Not palindrome")
