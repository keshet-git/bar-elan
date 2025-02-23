# Here come the functions:

# Function1: Add a new student

def add_student(student_dict):
    name = input("Enter the student's name: ")
    if name in student_dict:
        print("student exists")
    else:
        student_dict[name]= []
        print("The student's name has been added to the system.")

# Function2: Add job grade to student

def add_student_grade(student_dict):
    name = input("Enter the student's name: ")
    if name in student_dict:
        grade = float(input("Enter grade: "))
        student_dict[name].append(grade)
        print(f"The student grade {grade} has been added to {name}.")
    else:
        print("(student does not exist.")

# Function3: Remove an student

def remove_student(student_dict):
    name = input("Please enter the student's name: ")
    if name in student_dict:
        del student_dict[name]
        print("student removed.")
    else:
        print("student does not exist.")

# Function4: View grade average for an student

def view_student_grade(student_dict):
    name = input("Please enter the student's name: ")
    if name in student_dict:
        grade = student_dict[name]
        sum_grade = sum(student_dict[name])
        average_of_grade = sum_grade / len(grade)
        print(average_of_grade)
    else:
        print("student does not exist.")

# Here starts the main program:

student_dict = {}

while True:
    choice = input("Choose an option (1-5):")
    '''1. Add a new 
    2. Add grade to student
    3. Remove an student
    4. show average of grade
    5. End
    '''

    
    if choice == '1':
        add_student(student_dict)
    elif choice == '2':
        add_student_grade(student_dict)
    elif choice == '3':
        remove_student(student_dict)
    elif choice == '4':
        view_student_grade(student_dict)
    elif choice == '5':
        print("The End.")
        break
    else:
        print("Input Error")
