from mymodules import *
import os
import time


def student_data():
    print("""
1.Create a student
2.Show student list
3.Change student login password
4.Delete a student
""")
    user_option = input(str("Option : "))
    if user_option == "1":
        create_std()
    elif user_option == "2":
        std_list()
    elif user_option == "3":
        change_pwd()
    elif user_option == "4":
        dlt_std()
    elif user_option == "Q":
        os.system('cls')
        return False
    else:
        print("No valid option was selected")
        time.sleep(1)
        os.system('cls')


def create_std():
    student_list = []
    callTXTintoNestedList("student.txt", student_list)
    name = input("Student name:").upper()
    while find_element(name,student_list) != None:
        print("Student already existed!")
        name = input("Please submit another student:").upper()
    std_id = str(int(student_list[-1][1]) + 1)
    pwd = "admin123"
    data = (name, std_id, pwd)
    with open("student.txt", "r+") as f:
        if not f.read().endswith('\n'):
            f.write("\n")#to avoid blank line while adding new student
        f.write("|".join(data)+"|")
    print("\nThank You!\n")
    print("The student has been added to the system")
    print(f"Name : {name}")
    print(f"Student id  : {std_id}")
    print(f"Default password : admin123")
    input("Press Enter to continue")
    time.sleep(1)
    os.system('cls')


def std_list():
    student_list = []
    callTXTintoNestedList("student.txt", student_list)
    print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
    for count, line in enumerate(student_list, start=1):
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
    print("")
    input("Press Enter to continue")
    time.sleep(1)
    os.system('cls')

def change_pwd():
    student_list = []
    callTXTintoNestedList("student.txt", student_list)
    print("Change password")
    print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
    for count, line in enumerate(student_list, start=1):
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
    print("")
    name = input("Please Enter the student name that you want to update...\nNAME: ").upper()
    std_valid = find_element(name, student_list)
    while std_valid is None:
        print("Student not found")
        name = input("Please enter again!:")
        std_valid = find_element(name, student_list)

    print(f"\nStudent {name} is found")
    old_pwd = input("Please enter the old password for the student:")
    new_pwd = input("Please enter the new password for the student:")
    if old_pwd != student_list[std_valid][2]:
        print("Old password entered is wrong")
        old_pwd = input("Please enter again!:")
    elif old_pwd == "Q":
        os.system('cls')
        return False
    elif new_pwd == "Q":
        os.system('cls')
        return False
    student_list[std_valid][2] = new_pwd
    with open('student.txt', 'w') as file:
        for item in student_list:
            file.write("|".join(map(str, item)))
    print(f"\nStudent {name} 's login password has successfully updated.")
    input("\nPress Enter to continue")
    time.sleep(1)
    os.system('cls')

def dlt_std():
    student_list = []
    callTXTintoNestedList("student.txt", student_list)
    print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
    for count, line in enumerate(student_list, start=1):
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
    print("")
    name = input("Please Enter the student name that you want to delete...").upper()
    std_valid = find_element(name, student_list)
    while std_valid is None:
        print("Student not found")
        name = input("Please enter again!:")
        if name == "Q":
            return
        std_valid = find_element(name, student_list)
    print(f"\nStudent {name} is found")
    delete_a_line("student.txt", name)
    print(f"Student {name} has been deleted from system.")

    input("\nPress Enter to continue")
    time.sleep(1)
    os.system('cls')


