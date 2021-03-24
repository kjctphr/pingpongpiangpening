from mymodules import *
import os

student_list = []
callTXTintoNestedList("student.txt", student_list)

def view_attendance(id_no):
    student_index = find_element(id_no,student_list)
    name = student_list[student_index][0]
    files = []
    list = []
    new_list = []
    course_list = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(os.path.join("attendance folder")):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    for f in files:
        callTXTintoNestedList(f, list)
        course_list.append(f.split("/"))
    for i in list:
        if name in i:
            new_list.append(i)
    print("Attendance for", name)
    print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Course", "Classes", "Attendance Status"))
    for count, (i,j) in enumerate(zip(course_list,new_list), start=1):
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, i[1], i[2][0:2], j[2]))
    input("ENTER to continue")
    os.system('cls')

def change_password(id_no,pwd):
    student_list = []
    callTXTintoNestedList("student.txt", student_list)

    print("Change password")
    print("")
    old_pwd = input("Please enter the old password for the student:")
    if old_pwd == "Q":
        os.system('cls')
        return False
    else:
        pass
    while old_pwd != pwd:
        print("Old password entered is wrong")
        old_pwd = input("Please enter again!:")
    new_pwd = input("Please enter the new password for the student:")
    if new_pwd == "Q":
        os.system('cls')
        return False
    else:
        pass
    while len(new_pwd) < 4:
        print("The minimum length of the new password is 4.")
        print("Please reenter.")
    student_index = find_element(id_no,student_list)
    student_list[student_index][2] = new_pwd
    with open('student.txt', 'w') as file:
        for item in student_list:
            file.write("|".join(map(str, item)))
    print(f"\nYour login password has successfully updated.")
    input("\nPress Enter to continue")
    os.system('cls')

