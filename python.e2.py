odd1 = int(input("please Enter first,lower number: "))
odd2 = int(input("please Enter second,higher number: "))
print("Odd numbers between", odd1 ,"and", odd2 , "are :")
i = odd1 + 1 
while  i < odd2 : 
    if i % 2 != 0 :
        print(i, end=" ")
    i += 1