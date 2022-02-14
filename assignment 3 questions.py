Assignment-3
sanchit thakur
SID-21103126
QUESTIONS


QUESTION 1
A=str(input("ENTER ANY STRING: "))
List=A.split() #splitting of every letter in the input string
Dict={} #initializing an empty dictionary
if List.__len__()==1:   #if single input is there (single word)
    for i in List[0]:
        if i in Dict:
            Dict[i]+=1
        else:
            Dict[i]=1
    print(Dict)   
else:                   #if there are multiple input (not single word)
    for i in List:
        if i in Dict:
            Dict[i]+=1
        else:
            Dict[i]=1
    print(Dict)
print("\n")

QUESTION 2
Month=int(input("ENTER THE MONTH"))


if(Month in[1,3,5,7,8,10,12]):
    Day=int(input("ENTER THE DATE"))
    if(1<=Day<=31):
        Year=int(input("ENTER THE YEAR"))
        if(1800<=Year<=2025):
            print("Date-",Day,"/",Month,"/",Year)
            if(Month==12 and day==31):
                print("Next Date-","1/1/",Year+1)
            elif(Day==31):
                print("Next Date-","1/",Month+1,"/",Year)
            else:
                print("Next Date-",Day+1,"/",Month,"/",Year)
        else:
            print("INVALID YEAR")
    else:
         print("INVALID DATE")
elif(Month in[4,6,9,11]):
    Day=int(input("ENTER THE DATE"))
    if(1<=Day<=30):
        Year=int(input("ENTER THE YEAR"))
        if(1800<=Year<=2025):
            print("Date-",Day,"/",Month,"/",Year)
            if(Day==30):
                print("Next Date-","1/",Month+1,"/",Year)
            else:
                print("Next Date-",Day+1,"/",Month,"/",Year)
        else:
            print("INVALID YEAR")
    else:
         print("INVALID DATE")
elif(Month==2):
    Year=int(input("ENTER THE YEAR"))
    if(1800<=year<=2025):
        Day=int(input("ENTER THE DATE"))
        if(Year%4==0):
            if(1<=Day<=29):
                print("Date-",Day,"/",Month,"/",Year)
                if(Day==29):
                    print("Next Date-","1/",Month+1,"/",Year)
                else:
                    print("Next Date-",Day+1,"/",Month,"/",Year)              
            else:
                print("INVALID DAY")
        else:
            if(1<=Day<=28):
                print("Date-",Day,"/",Month,"/",Year)
                if(Day==28):
                    print("Next Date-","1/",Month+1,"/",Year)
                else:
                    print("Next Date-",Day+1,"/",Month,"/",Year)       
            else:
                print("INVALID DAY")     
    else:
        print("INVALID YEAR")
else:
    print("INVALID MONTH") 

	
QUESTION 3
INPUTLIST = input('Enter elements of a list with proper spaces in between ')
our_list = INPUTLIST.split()
# print list
print('List: ', INPUTLIST)

# convert each item to int type
for i in range(len(our_list)):
    # convert each item to int type
    our_list[i] = int(our_list[i])
square_of_list =[(our_list[i], our_list[i]**2) for i in range(len(our_list))]

print(square_of_list)

print("\n")


QUESTION 4
def input_point():
    point = int(input("Enter Grade Point: "))
    # checking if the grade point satisfy the input given conditions
    if point>10 or point<4:
        print("Invalid grade point, please Try Again") #error message
        point = input_point()
    return point
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and performance is poor")
elif(grade==5):
    print("Your Grade is 'C' and performance is Below Average")
elif(grade==6):
    print("Your Grade is 'C+' and performance is Average")
elif(grade==7):
    print("Your Grade is 'B' and performance is Good")
elif(grade==8):
    print("Your Grade is 'B+' and performance is very Good")
elif(grade==9):
    print("Your Grade is 'A' and performance is Excellent")
else:
    print("Your Grade is 'A+' and performance is outstanding")
print("\n")


QUESTION 5
X = 6
for A in range(X):
    # printing spaces
    for B in range(A):
        print(' ', end='')
    # printing alphabet
    for B in range(2*(X-A)-1):
        print(chr(65 + B), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n")



QUESTION 6
SID = int(input("Enter SID: "))
NAME = input("Enter Name: ")
students = {SID:NAME}

while True:
    ouestion = input("Do you want to enter another students entry(Y or N):").upper()
    if ouestion == 'Y':
        SID = int(input("Enter SID: "))
        NAME = input("Enter Name: ")
        students[SID] = NAME
    elif ouestion == 'N':
        break
    else:
        print('Invalid input')

#part a. print the dictionary
print("<a>",students)

#part b. sort acc to the names
print("<b>",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c>",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("<d>",students[sid])



QUESTION 7
# Function  is used to display the Fibonacci sequence
# with use of recursion
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avgerage=float(sum/no_of_terms)
print("AVERAGE OF RESULTANT FIBONACCI SERIES IS",avgerage)


QUESTION 8
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)

#part a(subrtacting set union from set intersection)
Part_A_Set_solution = Set_Union - Set_Intersection
print("<a>", Part_A_Set_solution)

# part B(Subtracting intersection of sets taken two at a time from the Union rest of all three sets)
Part_B_Set_solution = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set_solution)

# part C(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set_solution=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set_solution)
# part D(Excluding numbers from 1 to 10 that are occuring in Set1)
Part_D_Set_solution = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set_solution.add(i)
print("<d>", Part_D_Set_solution)
# part E(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set_solution = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set_solution.add(i)
print("<e>", Part_E_Set_solution)
