def my_func(a ,b):
    for i in range (1, 11):
     for j in range (1 , 11):
        return a * b
     
x = int (input("Enter first num: "))
y = int (input("Enter second num:"))

print (my_func (x , y))
