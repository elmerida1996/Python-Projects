def my_func(a):
    if a % 2 == 0:
        print ("The number you've entered is even")
    elif a % 2 != 0:
        print ("The number you've entered is odd")
 

x = int(input("Enter a number: "))
my_func(x)
