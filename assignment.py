#Question One (6 Marks)
#Differentiate Between Assigning and Declaring a variable giving practical Examples of Each 
"""
Assigning a variable means storing a specific value into that reserved space


for example

score = 9
input_score = int(intput("enter your score"))
score = intput_score # reassignment
if score >= 89:
    print("B")
else:
  print("FAIL")

while

Declaring a variable means reserving a space in memory to store a value and giving that space a name

for example

a = 10        # Declaring an integer variable named 'a'
"""


##age = "8"
##length = “56.90”
##height = “34.09944”
## convert the variable age to integer datatype

age = 8
new_age = float(age)
print(f"float: {new_age}")


length = 56.90
new_length = int(length)
print(f'integer: {new_length}')


height = 34.0994
new_height = int(height)
print(f"integer: {new_height}")






##Question Two (4 Marks)
##Given the code below

##age = "8"
##length = “56.90”
##height = “34.09944”
## convert the variable age to integer datatype

age = 8
new_age = float(age)
print(f"float: {new_age}")


length = 56.90
new_length = int(length)
print(f'integer: {new_length}')


height = 34.0994
new_height = int(height)
print(f"integer: {new_height}")



##Question Two (10 Marks)

# With the use of If statements, write a python program that allows an instructor to enter a mark strictly
# between 0 and 100. On receiving the mark, the program has to assign a grade based on your defined
# clusters ie 80-90 is A, 91 -100 is A+ etc. When a negative mark is entered, the program should not stop
# but prompt the user to enter a valid mark.



mark = int(input("Enter a mark between 0 and 100: "))
if mark < 0 or mark > 100:
  print("Enter a valid mark")
elif mark >= 91 and mark <= 100:
  print("allocate A+")
elif mark >= 80 and mark < 91:
  print("allocate A")
elif mark >= 70 and mark < 80:
  print("allocate B")
elif mark >= 60 and mark < 70:
  print("allocate C")
elif mark >= 50 and mark < 60:
 print("allocate D")
else:
  print("allocate F")