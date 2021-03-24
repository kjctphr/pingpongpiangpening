import time
import os
import glob
from mymodules import *

def report():
    print("")
    print("1.Bar List ")
    print("2.100 % attendance report")
    user_option = input(str("Option : ")).upper()
    if user_option == "1":
        barlist()
    elif user_option == "2":
        full_attendance()
    elif user_option == "Q":
        os.system('cls')
        return False


def barlist():
    course = input("Please enter course:").upper()
    course_list = []
    new_course_list = []
    files = glob.glob(os.path.join("attendance folder", course, "*.txt"))
    for file in files:
        callTXTintoNestedList(file, course_list)
    course_list.sort()
    for x in range(0, len(course_list), len(files)):
        new_course_list.append(course_list[x][0])
        new_course_list.append(course_list[x][1])
        for y in range(len(files)):
            new_course_list.append(course_list[x + y][2])
    new_list = []
    for i in range(0, len(new_course_list), len(files) + 2):
        new_list.append(new_course_list[i:i + len(files) + 2])

    bar_list = []
    for i in new_list:
        if i.count("P") < 0.8 * (len(files)):
            bar_list.append(i)
    print("Bar List")
    print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Attended class/Total classes"))

    for count, i in enumerate(bar_list):
        print('{:<5} | {:<15}| {:<15}| {}/{} '.format(count, i[0], i[1], i.count("P"), len(files)))
    input("Press Enter to clear")
    time.sleep(1)
    os.system('cls')

def full_attendance():
    course = input("Please enter course:").upper()
    course_list = []
    new_course_list = []
    files = glob.glob(os.path.join("attendance folder", course, "*.txt"))
    for file in files:
        callTXTintoNestedList(file, course_list)
    course_list.sort()
    for x in range(0, len(course_list), len(files)):
        new_course_list.append(course_list[x][0])
        new_course_list.append(course_list[x][1])
        for y in range(len(files)):
            new_course_list.append(course_list[x + y][2])
    new_list = []
    for i in range(0, len(new_course_list), len(files) + 2):
        new_list.append(new_course_list[i:i + len(files) + 2])

    fullattendance = []
    for i in new_list:
        if i.count("P") == (len(files)):
            fullattendance.append(i)
    print("100% attendance report")
    print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Attended class/Total classes"))

    for count, i in enumerate(fullattendance):
        print('{:<5} | {:<15}| {:<15}| {}/{} '.format(count, i[0], i[1], i.count("P"), len(files)))
        os.system('cls')

