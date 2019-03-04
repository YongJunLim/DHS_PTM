#The input will be a 2D array which contain x,y coor of green slots
#2D_array[i][j] where i is row number from top and j is column number from left.
#2D_array[i][0] will the be the teacher name of the row

#stuff in DB

import sqlite3
from display import display_DB
from update_DB import update

conn = sqlite3.connect('DHS_PTM.db')

c = conn.cursor()

def remove(s_array, email, outTeachers): #s_array for 2D array from HTML

    if len(s_array) == 1 and len(s_array[0]) == 1:
        data1 = c.execute("SELECT Name FROM Teacher_Detail")
        data1 = data1.fetchall()
        for i in range(0, len(data1)):
            NAME = data1[i][0]
            data = c.execute("SELECT TimeSlot1, TimeSlot2, TimeSlot3, TimeSlot4, TimeSlot5, TimeSlot6, TimeSlot7, TimeSlot8, TimeSlot9, TimeSlot10, TimeSlot11, TimeSlot12, TimeSlot13, TimeSlot14, TimeSlot15, TimeSlot16, TimeSlot17, TimeSlot18 FROM Teacher_Detail WHERE Name = '{0}'".format(NAME))
            data = data.fetchall()
            SLOTS = data[0]
            NEW_SLOTS = []
            for j in range(len(SLOTS)):
                if SLOTS[j] == email:
                    NEW_SLOTS.append(None)
                else:
                    NEW_SLOTS.append(SLOTS[j])

            update(NAME, NEW_SLOTS, email)

    else:
        NAMES = []
        for i in range(len(s_array)):
            NAME = s_array[i][0]
            NAMES.append(NAME)
            DB_data = display_DB(NAME) #DB_data is from DB

            for j in range(len(DB_data)):
                if DB_data[j] == email: #If Database slot is email value
                    if j+1 in s_array[i]:
                        pass
                    else:
                        DB_data[j] = None
                else:
                    if j+1 in s_array[i]:
                        DB_data[j] = email
                    pass

            update(NAME, DB_data, email)

        for i in range(len(outTeachers)):
            if outTeachers[i] in NAMES:
                pass
            else:
                NAME = outTeachers[i]
                data = c.execute("SELECT TimeSlot1, TimeSlot2, TimeSlot3, TimeSlot4, TimeSlot5, TimeSlot6, TimeSlot7, TimeSlot8, TimeSlot9, TimeSlot10, TimeSlot11, TimeSlot12, TimeSlot13, TimeSlot14, TimeSlot15, TimeSlot16, TimeSlot17, TimeSlot18 FROM Teacher_Detail WHERE Name = '{0}'".format(NAME))
                data = data.fetchall()
                SLOTS = data[0]
                NEW_SLOTS = []
                for j in range(len(SLOTS)):
                    if SLOTS[j] == email:
                        NEW_SLOTS.append(None)
                    else:
                        NEW_SLOTS.append(SLOTS[j])

                update(NAME, NEW_SLOTS, email)