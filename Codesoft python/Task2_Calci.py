print("MINI CALCULATOR")
a = float(input("enter the first no."))
b=float(input("enter the second no."))
#options
print("press 1 if you want to add the numbers")
print("press 2 if you want to sub. the numbers")
print("press 3 if you want to multiply the numbers")
print("press 4 if you want to div. the numbers")

choice=int(input("enter your choice from 1-4"))
#condition
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)    
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b) 
else:
    print("invalid choice")   