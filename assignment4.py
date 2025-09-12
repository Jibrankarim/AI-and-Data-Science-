
student_records = []

## 1 add student
def add_student():
    name = input("Enter student name : ")
    roll_no =input ("Ente student roll no : ")
    course = input("Enter student course :")
    marks = int (input ("Enter student marks : "))
    student_records.append([name, roll_no, course, marks])
    print("student added successfully...")

## 2 display students
def display_record():
    if student_records:
        print("student records")

        for student in student_records:
            print(f"name: {student[0]}")
            print(f"roll_no: {student[1]}")
            print(f"course: {student[2]}")
            print(f"marks: {student[3]}")
            print("********************")
    else:
        print("sorry No record found. Enter records")


##3 search student
        
def search_student():

    if student_records:
        roll_no = input("Enter roll no of student: ")

        for index, student in enumerate (student_records):

            return student, index

        return None, None

    else:
        print ("unable to search Please enter records ")
        return None, None

## 4 update marks
def update_marks():
    student_found, index = search_student()
    if student_found is not None:
        ## update marks
        
        print("Record Found")
        print("---------------")
        print(f"Name: {student_found[0]}")
        print(f"Roll No: {student_found[1]}")
        print(f"Course: {student_found[2]}")
        print(f"Marks: {student_found[3]}")
        print("---------------")

        ## get new marks to update
        update_marks = int(input("Enter marks to update:"))
        ##update marks in record
        student_records[index][3] = update_marks
        print("Record Successfully updated")
    else:
        print("Record not Found!")

## 5 delete record by  marks
        
def delete_record():
    student_found, _ = search_student()
    if student_found is not None:
        # delete record i.e. remove found student record from the records list
        student_records.remove(student_found)
        print("Deleted Record successfully")
    else:
        print("Record not found! \nUnable to delete")
        
## 6 sort record by marks
    
def sort_records():
    if student_records:
        # sort by marks [marks are saved at 3rd index of nested student record list]
        student_records.sort(key=lambda x:x[3], reverse=True)     
        print("Records sorted by Marks successfully....")
        
    else:
        print("Empty Records!!! \nUnable to Sort")
        

while True :
    print("****************************")
    print("1. Add Student Record.")
    print("2. Display Student Records.")
    print("3. Search Student Record.")
    print("4. Update Student Record.")
    print("5. Delete Student Record.")
    print("6. Sort Records")
    print("7. Exit")
    print("*****************************")

    Option = input("Enter your option: ")

    if Option == "1":

        ## Add Student 
        add_student()

    elif Option == "2":
        ## Display student records

        display_record()

    elif Option == "3":
        ## search student record

        student_ , _ = search_student()

        if student_ is not None:
            print("---student found---")
            print(f"Name:{student_[0]}")
            print(f"roll_no:{student_[1]}")
            print(f"course:{student_[2]}")
            print(f"marks:{student_[3]}")

        else:
            print("record not found.....!!")

    elif Option == '4':

        ##update marks        

        update_marks()

    elif Option == '5':
        # Delete student record
        delete_record()
    elif Option == '6':
        # sort records
        sort_records()
    elif Option == '7':
        # Exit
        break
    else:
        print("Invalid Choice!!!")


            
        
























        
        
