Assignment-2 CSE
sanchit thakur
SID-21103126
QUESTIONS



# Question 1
string1="Python is a case sensitive language" #String1
print("<A>THE LENGTH OF STRING IS",len(string1)) #Function to Find LENGTH OF STRING
print("<B>THE REVERSED STRING IS ",string1[-1::-1])
string2=string1[10:26] #STORED a case sensitive IN A NEW STRING
string2.replace("a case sensitive","object oriented") #REPLACED "a case sensitive" WITH "object oriented"
print("<E>THE INDEX OF SUBSTRING a is ",string1.find('a'))
print("<F>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS",string1.replace(" ",""))
print("\n")


#Question 2
NAME=input("ENTER YOUR NAME")
SID=int(input("ENTER YOUR SID"))
DEPARTMENT=input("ENTER YOUR DEPARTMENT")
CGPA=float(input("ENTER YOUR CGPA"))
print("Hey %s,"%NAME,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%DEPARTMENT,"and my CGPA is %f"%CGPA)
print("\n")


#Question 3
a=56
b=10
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print("\n")


#Question 4
numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))
numb3 = int(input("Enter third number: "))
 
if (numb1 > numb2) and (numb1 > numb3):
   largest = numb1
elif (numb2 > numb1) and (numb2 > numb3):
   largest = numb2
else:
   largest = numb3
 
print("THE LARGEST NUMBER IS ",largest)
print("\n")


#Question 5
i=input("ENTER A STRING")
if 'name' in i:
    print ("Yes")
else:
    print ("No")
print("\n")


#Question 6
a=float(input("ENTER FIRST SIDE OF TRIANGLE"))
b=float(input("ENTER SECOND SIDE OF TRIANGLE"))
c=float(input("ENTER THIRD SIDE OF TRIANGLE"))
if(a>=(b+c)):      #[Equality symbol is used because if sum of two sides is equal to third then also triangle is not valid]
    print("No")
elif(b>=(a+c)):
    print("No")
elif(c>=(a+b)):
    print("No")
else:
    print("Yes")
