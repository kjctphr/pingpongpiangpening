from mymodules import *
import os
import shutil

def course_data():
    print("""
1.Create a course
2.Show course list
3.Delete a course
\n""")
    user_option = input(str("Option : ")).upper()
    if user_option == "1":
        create_course()
    elif user_option == "2":
        course_list()
    elif user_option == "3":
        delete_course()
    elif user_option == "Q":
        pass
    else:
        print("No valid option was selected")
        os.system('cls')


def create_course():
    course_name = input("New course name:").upper()
    while True:
        try:
            os.makedirs(os.path.join("attendance folder", course_name))
        except:
            print("Course file existed")
            print("Please enter another course code")
            course_name = input("\nNew course code:").upper()
        else:
            break
    print("\nThank You!\n")
    print(f"The course {course_name} has been added to the system\n")
    input("Press Enter to continue")
    os.system('cls')

def course_list():
    course_list = os.listdir("attendance folder")
    print('{:<5} | {:<15}'.format("No.", "Course"))
    for count, line in enumerate(course_list, start=1):
        print('{:<5} | {:<15}|'.format(count, line))
    print("")
    input("Press Enter to continue")
    os.system('cls')

def delete_course():
    course_list = os.listdir("attendance folder")
    print('{:<5} | {:<15}'.format("No.", "Course"))
    for count, line in enumerate(course_list, start=1):
        print('{:<5} | {:<15}|'.format(count, line))
    print("")
    course_name = input("""
Please take note that all the attendance files in it will be deleted altogether
You may enter [Q]uit....
Please Enter the course that you want to delete...
""").upper()

    while True:
        try:
            if course_name == "Q":
                break
            shutil.rmtree(os.path.join("attendance folder", course_name))
        except:
            print("Course does not exist")
            course_name = input("Please Enter the course again!:").upper()
            if course_name == "Q":
                break

        else:
            break
    input("\nPress Enter to continue")
    os.system('cls')
