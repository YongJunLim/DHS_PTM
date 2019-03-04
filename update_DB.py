import sqlite3

conn = sqlite3.connect('DHS_PTM.db')

c = conn.cursor()

def update(Name, DETAILS, email):

    data = c.execute("SELECT TimeSlot1, TimeSlot2, TimeSlot3, TimeSlot4, TimeSlot5, TimeSlot6, TimeSlot7, TimeSlot8, TimeSlot9, TimeSlot10, TimeSlot11, TimeSlot12, TimeSlot13, TimeSlot14, TimeSlot15, TimeSlot16, TimeSlot17, TimeSlot18 FROM teacher_detail WHERE Name = '{0}'".format(Name))
    data = data.fetchall()
    data = data[0]

    for i in range(0, len(data)):
        if data[i] != None:
            if data[i] != email:
                DETAILS[i] = data[i]
            else:
                pass
        else:
            pass

    c.execute("UPDATE teacher_detail SET TimeSlot1 = ?, TimeSlot2 = ?, TimeSlot3 = ?, TimeSlot4 = ?, TimeSlot5 = ?, TimeSlot6 = ?, TimeSlot7 = ?, TimeSlot8 = ?, TimeSlot9 = ?, TimeSlot10 = ?, TimeSlot11 = ?, TimeSlot12 = ?, TimeSlot13 = ?, TimeSlot14 = ?, TimeSlot15 = ?, TimeSlot16 = ?, TimeSlot17 = ?, TimeSlot18 = ? WHERE Name = '{0}'".format(Name), DETAILS)

    conn.commit()
