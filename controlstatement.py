num=int(input("Enter number: "))

if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")



# create a program that checks if someone can vote or not using the age above 18
age=int(input("Enter age:"))
if age>=18:
    print("Your eligible to vote")
else:
    print("You are under age")

#  create a program to grade students

marks=int(input("Enter marks:"))

if marks<=100 and marks>=90:
    print("You have an A")
elif marks<=60 and marks>=59:
    print("You have an B")
elif marks<=40 and marks>=58:
    print("You have an c")
elif marks==0 and marks>=39:
    print("You have failed terribly")
else:
    print("invalid marks entered")



