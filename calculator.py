#Here is the calculator in the phython code
#We are going to do calculator by using conditional statements


num1=int(input("enter the value of num1 :"))  #Entering the numbers
num2=int(input("enter the value of num2 :"))
operator=input("operators +,-,/,* :")        #Entering the operator

#Addition
if operator=="+":
    print("sum of numbers : ",num1+num2)
#Substraction
elif operator=="-":
    print("substraction of numbers :",num1-num2)
#Division
elif operator=="/":
    if num2==0:                              #Here we are using nested statement
        print("the value is infinity")
    else :
        print("division of number :",num1/num2)
#Multiplication
elif operator=="*" :
    print("mutiplication of numbers :",num1*num2)
#Invalid operator
else :
    print("Invalid operator")