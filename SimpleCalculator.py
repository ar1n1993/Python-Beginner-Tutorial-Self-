#Simple Calculator1
#suppose we want to create a simple calcultor using if and else statement 
# And operators +,-,*,/:"


print("What Calculation operation you want?:")
operator=input("Enter the operation +,-,*,/:")
n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))


if operator=='+':
    print("Sum of two number is:",n1,'+',n2,'=',n1+n2)   #sum=n1+n2
elif operator=='-':
    print("Difference of two number is:",n1,'-',n2,'=',n1-n2)   #diff=n1-n2
elif operator=='*':
    print("Product of two number is:",n1,'*',n2,'=',n1*n2)   #prod=n1*n2
elif operator=='/':
    print("Division between two number is:",n1,'/',n2,'=',n1/n2)   #divide=n1/n2
else :
    print("Invalid operation")

