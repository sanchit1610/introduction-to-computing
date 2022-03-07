#name sanchit thakur
#SID 21103126
#assignment 1


#question 1
numb1= int(input("enter the first number: ") )
numb2= int(input("enter the second number: ") )
numb3= int(input("enter the third number: ") )
average= (numb1 + numb2 + numb3) / 3
print("average is:", average)


#question 2
standard_deduction=10000
depend_deduction=3000
gross=input("enter your gross income")
No_of_dependents=input("Enter your number of dependents")
taxable_income=int(gross)-int(standard_deduction)-(int(depend_deduction)+int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :")
print(float(tax))


#question 3
SID=input("enter your SID")
Name=input("enter your Name")
Gender=input("enter your Gender")
course_name=input("enter your couse_name")
CGPA=input("enter your CGPA")
STUDENT=[SID,Name,Gender,course_name,CGPA]#list of elements
print(STUDENT)#printing the list


#question 4
marks=[]
for i in range(5):
    marks.append(input("enter marks of student"))
marks.sort()
print(marks)


#question 5
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("part a :" ,colour)
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple']#changing element
print("part b :" ,colour)
