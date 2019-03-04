import sqlite3

conn = sqlite3.connect('DHS_PTM.db')

c = conn.cursor()
def display_DB(Name):
    data = c.execute("SELECT TimeSlot1, TimeSlot2, TimeSlot3, TimeSlot4, TimeSlot5, TimeSlot6, TimeSlot7, TimeSlot8, TimeSlot9, TimeSlot10, TimeSlot11, TimeSlot12, TimeSlot13, TimeSlot14, TimeSlot15, TimeSlot16, TimeSlot17, TimeSlot18 FROM Teacher_Detail WHERE Name = '{0}'".format(Name))
    data = data.fetchall()

    slots = []
    
    for i in range(0, len(data[0])):
        slots.append(data[0][i])

    return slots
