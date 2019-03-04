import sqlite3

conn = sqlite3.connect('DHS_PTM.db')

c = conn.cursor()

def teacher_checker(EMAIL):
    data = c.execute("SELECT Name FROM student_detail WHERE Email = '{0}'".format(EMAIL.lower()))
    data = data.fetchall()

    account = None
    
    student = True
    if len(data) == 0:
        student = False
    else:
        student = True
        
    data = c.execute("SELECT Name FROM teacher_detail WHERE Email = '{0}'".format(EMAIL.lower()))
    data = data.fetchall()

    teacher = True
    if len(data) == 0:
        teacher = False
    else:
        teacher = True

    if student == True and teacher == False:
        account = "Student"
        
    elif student == False and teacher == True:
        account = "Teacher"
        
    else:
        account = "Error"

    return account
    
