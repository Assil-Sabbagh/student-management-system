def get_non_empty_string(prompt):
   while True:
        entry=input(prompt).strip()
        if entry == "":
            print("Invalid entry. Please try again.")
            continue
        elif "," in entry:
            print("Input cannot contain commas.")
            continue
        else:
            return entry

def get_valid_score(prompt):
    while True:
        try:
            value=float(input(prompt))
            if value < 0 or value > 100:
                print("Invalid value. Please try again.")

            else:
                return value
            
        except ValueError:
            print("Invalid value. Please try again.")

def get_valid_student_number(students,prompt):
         while True:
           try:
             student_number= int(input(prompt))
             if student_number < 1 or student_number > len(students):
                 print("Invalid number. Please try again.")
             else:
                return student_number - 1
           except ValueError:
              print("Invalid entry. Please try again.")

def save_students_to_file(students, filename="students.txt"):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['score']:.2f}\n")

def print_menu():
    print("1) Add student")
    print("2) Show students")
    print("3) Show summary")
    print("4) Update student score")
    print("5) Delete student")
    print("6) Search student")
    print("7) Sort students")
    print("8) Reset all data")
    print("9) Exit")

def add_student(students):
    student_name= get_non_empty_string(f"Enter the name of student {len(students)+1}: ")
    student_score= get_valid_score(f"Enter the score of student {len(students)+1}: ")
    students.append({"name":student_name,"score":student_score})
    print("Added.")

    save_students_to_file(students)

def show_students(students):
    if students:
        for i,student in enumerate(students, start=1):
              print(f"{i}. {student['name']} - {student['score']:.2f}")
    else:
        print("No students yet.")

def show_summary(students):
    if students:
        average= sum(student['score'] for student in students)/len(students)
        maximum= max(students, key= lambda x: x['score'])
        minimum= min(students, key= lambda x: x['score'])
        max_name,max_score = maximum['name'],maximum['score']
        min_name,min_score = minimum['name'],minimum['score']
        print(f"Count: {len(students)}")
        print(f"Average: {average:.2f}")
        print(f"Top: {max_name} ({max_score:.2f})")
        print(f"Lowest: {min_name} ({min_score:.2f})")
        
    else:
        print("No data to summarize.")

def update_student(students):
    if students:
        show_students(students)
        student_number= get_valid_student_number(students,"Enter student number to update: ")
        updated_score= get_valid_score(f"Enter the updated score of student {student_number + 1}: ")
        old_score=students[student_number]['score']
        students[student_number]['score']=updated_score
        print(f"Student {students[student_number]['name']}'s score was updated from {old_score:.2f} to {updated_score:.2f}.")

        save_students_to_file(students)

    else:
        print("No students to update.")
        
def delete_student(students):
    if students:
        show_students(students)
        student_number= get_valid_student_number(students,"Enter student number to delete: ")
        removed_student=students.pop(student_number)
        print(f"Student {removed_student['name']} with score {removed_student['score']:.2f} was removed.")

        save_students_to_file(students)

    else:
        print("No students to delete.")

def search_students(students):
    if students:
        print("Search type:")
        print("a) Exact name")
        print("b) Partial match")
        choice= get_non_empty_string("Choose a search type: ")
        if choice != 'a' and choice != 'b':
            print("Invalid search type.")
            return
        
        keyword= get_non_empty_string("Enter student name to search: ").lower()
        found = False
        count = 1

        for student in students:
            if choice == 'a':
                if keyword == student['name'].lower():
                     print(f"{count}. {student['name']} - {student['score']:.2f}")
                     count += 1
                     found= True
     
            elif choice == 'b':
                if keyword in student['name'].lower():
                     print(f"{count}. {student['name']} - {student['score']:.2f}")
                     count += 1
                     found= True
                
        if not found:
            print("No Matching students found.")
            
    else:
        print("No students yet.")

def sort_students(students):
    print("a) By score (low to high)")
    print("b) By score (high to low)")
    print("c) By name (A to Z)")
    print()
    option= get_non_empty_string("Choose your choice of sorting: ")

    if option == 'a':
        students.sort(key= lambda x: x['score'])
        save_students_to_file(students)
        show_students(students)

    elif option == 'b':
        students.sort(key= lambda x: x['score'], reverse= True)
        save_students_to_file(students)
        show_students(students)

    elif option == 'c':
        students.sort(key= lambda x: x['name'].lower())
        save_students_to_file(students)
        show_students(students)

    else:
        print("Invalid choice.")

def reset_all_data(students):
    while True:
        if students:
           choice= input("Are you sure you want to reset? (y/n): ").strip().lower()
           if choice == 'y':
               students.clear()
               save_students_to_file(students, "students.txt")
               print("All data cleared.")
               break

           elif choice == 'n':
               print("Canceled.")
               break

           else:
               print("Invalid choice.")
            
        else:
            print("No data to reset.")
            return


def load_students(filename="students.txt"):
    students= []

    if os.path.exists(filename):
       with open(filename,'r') as file:
           for line in file:
              name,score= line.strip().split(",")
              students.append({"name":name,"score":float(score)})

    else:
        print("File does not exist. A new file will be created.")
        open(filename,"w").close()

    return students


import os

students= load_students()

while True:
    print()
    print_menu()
    print()

    choice= get_non_empty_string("Enter your choice from the menu: ")

    if choice == '1':
        add_student(students)

    elif choice == '2':
        show_students(students)

    elif choice == '3':
        show_summary(students)

    elif choice == '4':
        update_student(students)
        
    elif choice == '5':
        delete_student(students)

    elif choice == '6':
        search_students(students)

    elif choice == '7':
        sort_students(students)

    elif choice == '8':
        reset_all_data(students)

    elif choice == '9':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice.")
           