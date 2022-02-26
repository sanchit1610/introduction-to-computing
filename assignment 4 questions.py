Assignment-4
sanchit thakur
SID-21103126
QUESTIONS


QUESTION 1
# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n , source_rod, to_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, source_rod, aux_rod, to_rod)
	print("Move disk",n,"source rod",source_rod,"to rod",to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, source_rod)
		
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods


QUESTION 2
from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("BY METHOD OF LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for proper spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr formula = n!/((n-r)!*r!)
	print()	# for new line in between
print("\n\n")

print("BY METHOD OF RECURSSIONS")

def pascal_triangle(n,originalength=n):  
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    # as we know that the first number is alwaysgona to be 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        # by using the method of Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")


QUESTION 3
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#print(A)
print("A=. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#print(B)
if (Quotient == 0):
    print("<B>= The quotient is zero")
if (Remainder == 0):
    print("<B>= The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<B>= All the values are non zero")

#print(C)
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<C>= Filtered out numbers that are greater than 4 are : {result}")

#print(D)
setresult = set(result)
print("<D>= Set:",setresult)

#print(E)
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("<E>= Immutable set:",immutableSet)

#print(F)
print("<F>= Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")


QUESTION 4
class STUDENT:
    def __init__(self, student,Roll_no):
        self.name = student
        self.Roll_no = Roll_no
    
    def __del__(self):
        print("Object destroyed")


student1 = STUDENT("sanchit", 21103126)  #creating of the object
print("Object created")

print(f"The name of the student is {student1.name} and SID is {student1.Roll_no}.")  #printing of the assigned values

del student1  #deleting of the object
print("\n")


QUESTION 5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part <a> updating salary
employee1.salary = 70000
print(f"<a> The updated salary of {employee1.name} is {employee1.salary} ")

#part <b> deleting a record
print("<b>Record of Viren deleted", end='')
del employee3
print("\n")


QUESTION 6
#INPUT OF THE WORD FROM THE FIRST FRIEND (GEORGE)
Word =input("Enter the word: ")
Word=Word.lower()

#INPUT OF THE NEW WORD FORM FROM THE WORD GIVEN BY THE FIRST FRIEND (GEORGE)
new_word = input("Enter the new meaningful word using the same exact letter to test the friendship between them: ")
new_word=new_word.lower()
#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper's to verify the word's meaning
def userinput():
    if count_in_dict(Word) != count_in_dict(new_word):
        print("The letters are not the exact, friendship is a fake one")
        return
    ans = input("Does the new word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass their friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is a  fake one")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()


