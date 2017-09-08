# creating a database

import sqlite3


class DBconnect:
    def __init__(self):
        self._db = sqlite3.connect('Reservation.db')
        self._db.row_factory = sqlite3.Row
        self._db.execute('create table if not exists Ticket(ID integer PRIMARY KEY AUTOINCREMENT, Name text, Gender text, Comment text)')
        self._db.commit()

    def Add(self, Name,Gender,Comments):
        self._db.row_factory = sqlite3.Row
        self._db.execute("insert into Ticket(Name, Gender, Comment) values(?,?,?)", (Name,Gender, Comments))
        self._db.commit()
        return ("Record is added")

    def ListAdmins(self):
        cursor = self._db.execute("select * from Ticket")
        for row in cursor:
            print("ID:{}, Name:{}, Gender:{}, Comment:{}".format(row["ID"], row["Name"],row["Gender"], row['Comment']))

    def DeleteRecord(self,ID):
        self._db.row_factory = sqlite3.Row
        self._db.execute("delete from Ticket where ID={}".format(ID))
        self._db.commit()
        return ("Record is deleted")

    def UpdateRecord(self,ID, Comment):
        self._db.row_factory = sqlite3.Row
        self._db.execute("update Ticket set Comment=? where ID=?",(Comment, ID))
        self._db.commit()
        return ("Record is updated")

def main():
    dbconnect = DBconnect()
    while 1:
        IndexOp = int(input("select operation," "\n 1- Add \n 2- List Admins \n 3- Delete record \n 4- Update Age \n 0 - Exit \n ===== \n Index number:"))
        if(IndexOp==0):
            break;
        elif(IndexOp==1):
            Name = input("Enter name:")
            Age = int(input("Enter age:"))
            dbconnect.Add(Name,Age)
        elif(IndexOp==2):
            dbconnect.ListAdmins()
        elif(IndexOp == 3):
            ID = input("Enter ID to delete:")
            dbconnect.DeleteRecord(ID)
        elif (IndexOp == 4):
            ID = input("Enter person ID:")
            Age = int(input("Enter new age:"))
            dbconnect.UpdateRecord(ID, Age)

if __name__ == '__main__':
    main()


