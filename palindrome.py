# function which return reverse of a string
def is_palindrome(cars):
    return cars == cars[::-1]

# Driver code
cars ="mercedes"
ans = is_palindrome(cars)

if ans:
    print("True")
else:
    print("False")
