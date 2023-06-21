#enter any number between 100 and 500. keep asking the user for correct input until its in range.(logical operator) using while loop
n=int(input("enter number :"))
while n<100 or n>500:
    print("invalid input")
    n=int(input("enter the number between 100 and 500 : "))
print("the number entered is:",n)
