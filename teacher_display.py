import sqlite3

conn = sqlite3.connect('DHS_PTM.db')

c = conn.cursor()
def t_display_DB(Name):
    data = c.execute("SELECT TimeSlot1, TimeSlot2, TimeSlot3, TimeSlot4, TimeSlot5, TimeSlot6, TimeSlot7, TimeSlot8, TimeSlot9, TimeSlot10, TimeSlot11, TimeSlot12, TimeSlot13, TimeSlot14, TimeSlot15, TimeSlot16, TimeSlot17, TimeSlot18 FROM Teacher_Detail WHERE Name = '{0}'".format(Name))
    data = data.fetchall()

    slots = [] #Email

    for i in range(0, len(data[0])):
        slots.append(data[0][i])

    timeslots = ["17:00-17:10", "17:10-17:20", "17:20-17:30", "17:30-17:40", "17:40-17:50", "17:50-18:00", "18:00-18:10", "18:10-18:20", "18:20-18:30", "18:30-18:40", "18:40-18:50", "18:50-19:00", "19:00-19:10", "19:10-19:20", "19:20-19:30", "19:30-19:40", "19:40-19:50", "19:50-20:00"]

    temp = [] #Names

    for i in range(len(timeslots)):
        if len(slots[i]) > 0:
            data = c.execute("SELECT Name FROM Student_Detail WHERE Email = '{0}'".format(slots[i]))
            data = data.fetchall()
            temp.append(data[0][i])
        else:
            temp.append("No student")

    for i in range(len(slots)):
        print(timeslots[i])
        print(temp[i])
        print(slots[i])

    return timeslots, temp, slots

t_display_DB("Gi Soong Chee")

