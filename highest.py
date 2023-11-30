# Take three numbers a, b, c as input from the user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

# if a > b
if a > b:
    # if a > c  
    if a > c:
        # Display a
        print(a)
    # else 
    else:
        # Display c
        print(c)
# else
else:
    # if b > c
    if b > c:
        # Displayt b
        print(b)
    # else
    else:
        # Display c
        print(c)