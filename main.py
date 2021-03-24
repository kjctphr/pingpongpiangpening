from student_data import *
from attendance import *
from mymodules import *
from student_entry import *
from report import *
from course_data import *
import os
import time


def main():
    while 1:
        print("Welcome to the UTAR SMART Student Management & Attendance Registration Technology")
        print("Enter [Q] whenever you would like to quit the program")
        print("")
        print("1. Login as student")
        print("2. Login as admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_admin()
        elif user_option == "Q":
            print("You are going to quit the program.\nDo you sure?")
            user_option2 = input(str("ENTER to quit the program and NO return to main.\nOption:"))
            if user_option2 == "NO":
                os.system('cls')
                main()
            else:
                exit()
        else:
            print("No valid option was selected")
            time.sleep(1)
            os.system('cls')
            

def auth_student():#login verification
    global id_no , pwd
    student_list = []
    print("")
    print("Student's Login")
    print("")
    id_no = input("Id_no:")
    pwd = input("Password:")
    callTXTintoNestedList("student.txt",student_list)
    std_valid = find_element(id_no,student_list)
    if std_valid != None and student_list[std_valid][2] == pwd:
        student_session()
    elif id_no == "Q":
        os.system('cls')
        return
    elif pwd == "Q":
        os.system('cls')
        return
    else:
        print("\nUser doesn't exist or wrong password!\n")
        time.sleep(1)
        os.system('cls')

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin":
        if password == "password":
            admin_session()
        elif password == "Q":
            os.system('cls')
            return
        else:
            print("Incorrect password !")
            time.sleep(1)
            os.system('cls')
    elif username == "Q":
        os.system('cls')
        return
    else:
        print("Login details not recognised")
        time.sleep(1)
        os.system('cls')

def student_session():
    print("")
    print("1. View attendance")
    print("2. Change password")
    user_option = input("Option : ")
    if user_option == "1":
        view_attendance(id_no)
    elif user_option == "2":
        change_password(id_no,pwd)
    elif user_option == "Q":
        os.system('cls')
        return
    else:
        print("No valid option was selected")
        time.sleep(1)
        os.system('cls')


def admin_session():
    print("")
    print("1.CRUD Student data")
    print("2.CRUD course")
    print("3.CRUD Student Attendance")
    print("4.Generate report")
    user_option = input("Option : ")
    if user_option == "1":
        student_data()
    elif user_option == "2":
        course_data()
    elif user_option == "3":
        attendance()
    elif user_option == "4":
        report()
    elif user_option == "Q":
        os.system('cls')
        return
    else:
        print("No valid option was selected")
        time.sleep(1)
        os.system('cls')


main()

