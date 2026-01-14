a=int(input("Enter a  first number:"))
b=int(input("Enter a second number:"))
c=operation=input("Enter the operation you want to perform (+,-,*,/,%,**):")
print("your result is:",eval(f"{a}{c}{b}"))
add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
exp=a**b
list=(add,sub,mul,div,mod,exp)
print("The sum of two numbers:",add)
print("The difference of two numbers:",sub)
print("The product of two numbers:",mul)
print("The division of two numbers:",div)
print("The modulus of two numbers:",mod)
print("The exponent of two numbers:",exp)
print("The list of all operations:",list)
#This program performs basic arithmetic operations on two numbers provided by the user and displays the results.
#It calculates addition, subtraction, multiplication, division, modulus, and exponentiation.
#Finally, it compiles all the results into a list and prints it out.

