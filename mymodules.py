from datetime import datetime
import os
import glob


def callTXTintoNestedList(file,list):
    with open(file, "r") as file:
        for row in file:
            x = row.split("|")
            list.append(x)

def find_element(element, list):
    x = 0
    while x < len(list):
        y = 0
        while y < len(list[x]):
            if list[x][y] == element:
                return x
            y = y + 1
        x = x + 1

def replace_element(file_name,old_string,new_string):
    with open(file_name, "r") as reading_file:
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip("|")
            new_line = stripped_line.replace(old_string, new_string)
            new_file_content += new_line + "\n"

    writing_file = open(file_name, "w")
    writing_file.write(new_file_content)
    writing_file.close()

def delete_a_line(file_name,name):
    removed_lines = 0
    with open(file_name, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if not line.startswith(name):
                f.write(line)
        f.truncate()

def attendance_status(session_start,session_end , login_time):
    session_start = datetime.strptime(session_start, '%H:%M')
    session_end = datetime.strptime(session_end, '%H:%M')
    session_duration = session_end - session_start
    login_time = datetime.strptime(login_time, '%H:%M')
    leave_time = session_end
    std_duration = leave_time - login_time
    if std_duration <  0.8 * session_duration :
        attendance = 'Late'
    else :
        attendance = "Present"
    return attendance

def callATTENDANCEtoNestedList(course,course_list):
    files = glob.glob(os.path.join("attendance folder", course, "*.txt"))
    for file in files:
        callTXTintoNestedList(file, course_list)
    course_list.sort()
    return course_list
