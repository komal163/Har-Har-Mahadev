#question 1.
'''print("hello komal how are you")

#question 2.

a=int(input("enter first no:"))
b=int(input("Enter second no:"))
a=a+b
b=a-b
a=a-b
print("swap",a,b)'''


#2.check if a given number is even or odd

'''n=int(input("Enter a number"))
if n%2==0:
   print("even")
else:
    print("odd")'''
     
#3.find the largest of three number
'''a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if a>b and a>c:
    print("a")
elif b>a and b>c:
    print("b")
else:
    print("c")'''
#4.convert string in integer
'''string="123"
print(int(string))'''
#5.convert an intiger to string
'''num=123
str_num=str(num)
print(type(str_num))'''
#6.wap a demostrate implicit and Explicit type conversion
#implicit
'''n=12
m=2.0
result=n+m
print(result)
print(type(result))
#Explicit
a=9
b=float(a)
print(b)
print(type(b))'''
#7.covert revenue to currency format







#8.write a program to calculate sum of 5 sub and find percentage
'''hindi=int(input("Enter marks of hinddi:"))
english=int(input("Enter marks of english:"))
chemistry=int(input("Enter marks of chemistry"))
maths=int(input("Enter marks of maths"))
bio=int(input("Enter marks of biology"))
total=hindi+english+chemistry+maths+bio
avg=total/5
percentage=(total/500)*100
print("total",total)
print("average",avg)
print("percentage",percentage)'''

#9.write a program to find gross salay
'''bs=float(input("Enter basic salary:"))
hra=float(input("enter hra "))
da=float(input("Enter da"))
pf=float(input("Enter pf"))
gross=bs+hra+da+pf
print("gross salary",gross)'''

#10.write a program to calculate area of rectangle square scales

#rectangle
'''length=float(input("Enter the length"))
width=float(input("Enter the width"))
area=length*width
print("area of rectangle",area)'''
#square
'''side=float(input("Enter of side"))
area=side*side
print("area of square",area)'''
#scalence
'''a=int(input("Enter number of a"))
b=int(input("Enter number of b"))
c=int(input("Enter number of c"))
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))*0.5
print("area of scalence",area)'''

#11.write a proram to find  the perimeter of a circle ,rectangle and trianle
'''radius=float(input("Enter value of radius"))
peri=2*3.14*radius
print("perimeter of circle",peri)'''
#rectzngle
'''l=float(input("enter the lenght"))
w=float(input("enter the width"))
peri=2(l+w)
print("perimeter of rectangle",peri)'''

#triangle
'''a=int(input("Enter the value of a "))
b=int(input("Enter value of b "))
c=int(input("Enter value of c"))
peri=a+b+c
print("perimeter of triangle",peri)'''

#13.Write a program to compute simple interest
'''p=int(input("Enter the principle"))
r=int(input("Enter the rate"))
t=int(input("Enter the time"))
SI=p*r*t
print("simple interest",SI)'''

#14.write a program to swap the value of two variable with using third varaible
'''a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
temp=a
a=b
b=temp
print("the value ofa after swaping  ",a)
print("the value of b after swaping",b)'''

'''a=int(input("Enter the value a:"))
b=int(input("Enter the value of b:"))
a=a^b
b=a^b
a=a^b
print("swapppinyg",a)
print("swaping",b)'''



#15.write a program to perform aithmatic operationon a=8,b=3
'''a=8
b=3
addition=a+b
sub=a-b
multi=a*b
div=a/b
modulo=a%b
print("addition",addition)
print("subraction",sub)
print("multiplication",multi)
print("division",div)
print("modulo",modulo)'''
#16.write a program to apply relational operation on a=8 b=3
'''a=8
b=3
if(a>b):
    print("a is graterthan b")
else:
    print("a is lessthan equal to b")
if(a>=b):
    print("a is greaterthan equal to b")
else:
    print("a is lesserthan b")
if(a<b):
    print("a is lessthan b")
else:
    print("a is graterthan or equal to b")
if(a<=b):
    print("a is lesserthan equal to b")
else:
    print("a is greaterthan b")
if(a==b):
    print("a is eual to b")
else:
    print("a and b are not equal")
if(a!=b):
    print("a is not equal to b")
else:
    print("a is equal to b")'''
#17.write a program to apply assignment operation on a=8,b=3
'''a=8
b=3
a+=b
a-=b
a*=b
a/=b
a%=b
a//=b
a**=b
#a&=b
#a|=b
#a^=b
#a>>=b
#a<<=b
print("a+=b",a)
print("a-=b",a)
print("a*=",a)
print("a/=",a)
print("a%=b",a)
print("a//=b",a)
print("a**=b",a)
#print("a&=b",a)
#print("a|=b",a)
#print("a^=b",a)
#print("a<<=b",a)
#print("a>>=b",a)'''
#19.write a program to apply bitwise operation on a=8,b=3
'''a=8
b=3
print("a&b=",a&b)
print("a|b=",a|b)
print("a^b=",a^b)
print("~a=",~a)
print("a<<1=",a<<1)
print("b<<1=",b<<1)'''
#20. write a program to apply identity operators.
'''list=[1,2,3,4,5]
str1="Hello world"
dict1={1:"Geek",2:"for",3:"geeks"}
print(2 in list)
print("0" in str1)
print(3 in dict1)'''

#21.write va program to swap the contents of two numbers using bitwise XOR operation
'''def swap_number(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
num1=10
num2=5
print("Before swapping:",num1,num2)
num1,num2=swap_numbers(num1,num2)
print("After swapping:",num1,num2)'''

#22.wap to find absolute value of the given number
'''n=float(input("Enter the number"))
c=abs(n)
print(c)
#without using  absolute fuction'''
'''n=float(input("Enter number"))
if n<0:
    print("the absolute of:",n,"is",n)
else:
    print(n)'''
#23.write a program to add two complex number
'''real1=int(input("Enter first real number:"))
img1=int(input("Enter the first imaginary number:"))
real2=int(input("Enter the second real number:"))
img2=int(input("Enter second imaginary number:"))
real=real1+real2
imag=img1+img2
print("The sum of two complex number",real,"+", imag,"i")'''

#24. Write a program to find roots of a quadradic expression



















#25.program calculate the average of a list of a number using the division operator
'''list=[4,5,6,7,8,9,10,3,8]
count=0
for i in list:
    count+=i
avg=count/len(list)
print("sum",count)
print("average",avg)'''

#26.program to compare two numbers and determine if they are qeual
'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1==num2:
    print("the number are equal .")
else:
    print("tne numbers are not equal.")'''
#27.program to compare two number and determine whether they are greater than or less than
'''a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    print("a is grater than b")
else:
    print("a is not greater than b")
if a<b:
    print("a is lessthan b")
else:
    print("a is not lessthan b")'''
#28.program to check if given string is equal to specific value

'''string=input("Enter a string")
specific_value=input("Enter a apecific value")
if string==specific_value:
    print("the string are equal to specific value")
else:
    print("the string value is not equal to specific value")'''

#29.program to calculate compound interest using compound assignment operator
'''p=float(input("Enter the principle"))
r=float(input("Enter the rate"))
t=int(input("Enter the time"))
Amount=p*(pow((1+r/100),t))
CI=Amount-p
print("compound interest is",CI)'''

#30.program to check if a given number is odd or even using bitwise operator
'''def even(n):
    return not(n&1)
num=int(input("Enter a number"))
if even(num):
    print(f"number is even")
else:
    print("number is odd")'''

#31.program to check if a number is positive negative odd evenn
'''num=int(input("Enter a number"))
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")
if num%2==0:
    print("even")
else:
    print("odd")'''
#32.write a program to accept two integer and check if they are equal
'''num1=int(input("Enter a number"))
num2=int(input("Enter a second number"))
if num1==num2:
    print("number are equal")
else:
    print("number are not equal")'''
#33.write a program to check if a given integer is divisible by 7 or not
'''num=int(input("Enter a number"))
r=num%7
if r==0:
    print(" number is divisible by 7")
else:
    print("number is not divisible ny 7")'''
#34.write a program to find the greatest of three number using else if lader
'''num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if (num1>=num2) and( num1>=num3):
    print("num1 is greater")
if (num2>=num1 )and (num2>=num3):
    print("num2 is greater")
if (num3>=num1) and (num3>=num2):
    
    print("num3 is greater")
#35. write a program to find the greatest of three number using else if lader
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if (num1>=num2) and( num1>=num3):
    print("num1 is greater")
elif (num2>=num1 )and (num2>=num3):
    print("num2 is greater")
else:
    print("num3 is greater ")'''
#36.write a proram to convert an uppercase character into lower case and vise versa
'''name="KoMaL"
print(name.swapcase())'''
#37.write a program to chaeck weather an entered year is leapyear or not
'''year=int(input("Enter year"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("year is leapyear")
else:
    print("year is not leapyear")'''
#38.write a program to check whather alphabet enterned by the user is a vowel or consonat
'''ch=input("enter a character")
if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='U' or ch=='u' or ch=='O'
   ch=='o'):
    print(ch, "vowel")
else:
    print(ch,"consonant")'''
#39.
'''num=int(input("Enter a number"))
if num==1:
    print("monday")
elif num==2:
    print("tuesday")
elif num==3:
    print("wednesday")
elif num==4:
    print("thursday")
elif num==5:
    print("friday")
elif num==6:
    print("saturday")
elif num==7:
    print("sunday")
#40.wap a program print color name if enter first chacter of that color
color=input("enter color name")'''











#41.wap to simulate arithmatic calculator
a=float(input("enter first number"))
b=float(input("enter secomd number"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)




    


        










        










        







