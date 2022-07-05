#Simple Calculator2
#suppose we want to create a simple calcultor using if and else statement 
# And operators +,-,*,/:
#Sum,Difference,Product,Division are kept in variables

print("What Calculation operation you want?:")
operator=input("Enter the operation +,-,*,/:")
n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
sum =n1+n2
diff=n1-n2
prod1 =n1*n2
divi1 =n1/n2

if operator=='+':
    print("Sum of two number is:",n1,operator,n2,'=',sum)   #sum=n1+n2
elif operator=='-':
    print("Difference of two number is:",n1,operator,n2,'=',diff)   #diff=n1-n2
elif operator=='*':
    print("Product of two number is:",n1,operator,n2,'=',prod1)   #prod=n1*n2
elif operator=='/':
    print("Division between two number is:",n1,operator,n2,'=',divi1)   #divide=n1/n2
else :
    print("Invalid operation")
