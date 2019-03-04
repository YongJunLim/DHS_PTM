import sqlite3

conn = sqlite3.connect('DHS_PTM.db')

c = conn.cursor()

def student_subjects(EMAIL):
    data = c.execute("SELECT Student_Subject_Index FROM student_detail WHERE Email = '{0}'".format(EMAIL.lower()))
    data = data.fetchall()
    for i in range(0, len(data)):
        data[i] = str(data[i]).strip('(,)')
    Student_Subject_Index = data[0]
    
    Student_Detail = []
    
    data = c.execute("SELECT Class FROM student_detail WHERE Email = '{0}'".format(EMAIL))
    data = data.fetchall()
    Class = (data[0][0]).strip('""')
    Student_Detail.append(Class)
    for i in range(1, len(data)):
        Student_Detail.append(str(data[i]).strip('(,)'))
    data = c.execute("SELECT Subject1, Subject2, Subject3, Subject4, Subject5, Subject6, Subject7, Subject8, Subject9 FROM student_subject WHERE Student_Subject_Index = '{0}'".format(Student_Subject_Index))
    data = data.fetchall()
    for i in range(0, len(data[0])):
        Student_Detail.append(data[0][i])

    Teachers = []
        
    for i in range(0, len(Student_Detail)):
        if Student_Detail[i] == "NULL":
            i = i + 1
        else:
            data = c.execute("SELECT Teacher_Subject_Index FROM teacher_subject WHERE Subject2 = '{0}' OR Subject1 = '{0}' AND S1C1 = '{1}' OR Subject1 = '{0}' AND S1C2 = '{1}' OR Subject1 = '{0}' AND S1C3 = '{1}' OR Subject1 = '{0}' AND S1C4 = '{1}' OR Subject1 = '{0}' AND S1C5 = '{1}' OR Subject1 = '{0}' AND S1C6 = '{1}' OR Subject1 = '{0}' AND S1C7 = '{1}' OR Subject1 = '{0}' AND S1C8 = '{1}' OR Subject1 = '{0}' AND S1C9 = '{1}' OR Subject1 = '{0}' AND S1C10 = '{1}'".format(Student_Detail[i], Class))
            data = data.fetchall()
        
            for i in range(0, len(data)):
                for j in range(0, len(data[i])):
                    Teachers.append(data[i][j])

    data = c.execute("SELECT Teacher_Subject_Index FROM teacher_subject WHERE CT_Class = '{0}'".format(Class))
    data = data.fetchall()
        
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            Teachers.append(data[i][j])

    Teachers_Name = []

    for i in range(0, len(Teachers)):
        data = c.execute("SELECT Name FROM teacher_detail WHERE Teacher_Subject_Index = '{0}'".format(Teachers[i]))
        data = data.fetchall()

        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                Teachers_Name.append(data[i][j])
    
    Teacher_Subject = []
    
    for i in range(0, len(Teachers_Name) - 2):
        Teacher_Subject.append(Student_Detail[i+1])

    Teacher_Subject.append("CT")
    Teacher_Subject.append("CT")

    return Teachers_Name, Teacher_Subject

a, b = student_subjects("poh.saykeong@dhs.sg")
print(a)
#PE, H1 not reflected
