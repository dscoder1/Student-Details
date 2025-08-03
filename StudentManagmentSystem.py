import mysql
import mysql.connector
from tkinter.messagebox import *
import datetime
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)
cur=db.cursor()
databaseflag=False
tableflag=False
cur.execute("show databases;")
databases=cur.fetchall()
for database in databases:
    if(database[0]=='pythonpart2'):
        databaseflag=True

if(databaseflag==False):
    cur.execute("create database if not exists PythonPart2")
    showinfo("Info","Database Created")
    db.commit()
else :
    print("Database Already Created")

cur.execute("use PythonPart2")
cur.execute("show tables;")
tables=cur.fetchall()
for table in tables:
    if(table[0]=="student"):
        tableflag=True

if(tableflag==False):
    cur.execute("create table if not exists Student(Roll int primary  key,FirstName varchar(20),LastName varchar(20),FullName varchar(30),Age int,Course varchar(20),Session varchar(20),EntryDate Date,EntryTime Time)")
    showinfo("Info","Table Created")
    db.commit()
else:
    print("Table Already Created")
class Student:
    def __init__(self,Roll,FirstName,LastName,Age,Course,Session):
        self.__Roll=Roll
        self.__FirstName=FirstName
        self.__LastName=LastName
        self.__Age=Age
        self.__Course=Course
        self.__Session=Session
        try:
            cur.execute("select * from student where Roll={}".format(self.__Roll))
            rollData=cur.fetchone()
            if(rollData==None):
                cur.execute("insert into student values({},'{}','{}','{}',{},'{}','{}','{}','{}')".format(self.__Roll,self.__FirstName, self.__LastName,(self.__FirstName+" "+self.__LastName),self.__Age ,self.__Course,self.__Session,datetime.datetime.now(),datetime.datetime.now()))
                db.commit()
                print("Info","Student Data Inserted Into Database")
                #showinfo("Info","Student Data Inserted Into Database")
            else:
                print("Error","Student Roll Number Is Already Present In DataBase")
                #showerror("Error","Student Roll Number Is Already Present In DataBase")
        except:
            print("Any Error In Insertion")

    def displayInfo(self):
        print("\nStudent Information")
        print("\nStudent Roll Number: ",self.__Roll)
        print("\nStudent First Name: ",self.__FirstName)
        print("\nStudent Last Name: ",self.__LastName)
        print("\nStudent FullName Name: ",(self.__FirstName+" "+self.__LastName))
        print("\nStudent Age: ",self.__Age)
        print("\nStudent Course: ",self.__Course)
        print("\nStudent Session: ",self.__Session)

    def getRoll(self):
        return self.__Roll

    def getFirstName(self):
        return self.__FirstName
    
    def getLastName(self):
        return self.__LastName
    
    def getFullName(self):
        return (self.__FirstName+self.__LastName)
    
    def getAge(self):
        return self.__Age
    
    def getCourse(self):
        return self.__Course
    
    def getSession(self):
        return self.__Session

    def deleteStudent(self,RollNumber):
        cur.execute("select * from student where Roll={}".format(RollNumber))
        stdData=cur.fetchone()
        print(stdData)
        if(stdData!=None):
            cur.execute("delete from student where Roll={}".format( RollNumber))
            db.commit()
            print("Info","Student Deleted From Database..\nStudent Roll--> "+str(stdData[0])+"\nStudent Name--> "+stdData[3])
            #showinfo("Info","Student Deleted From Database..\nStudent Roll--> "+str(stdData[0])+"\nStudent Name--> "+stdData[3])
        else:
            print("Warning","Student Details Not Found")
            #showwarning("Warning","Student Details Not Found")

    def searchStudent(self,RollNumber):
        cur.execute("select * from student where Roll={}".format(RollNumber))
        stdData=cur.fetchone()
        print(stdData)
        if(stdData!=None):
            print("Student Data From Database..\n\nStudent Roll  | "+str(stdData[0])+"\n\nStudent Name  | "+stdData[3]+"\n\nStudent Age  | "+str(stdData[4])+"\n\nStudent Course  | "+stdData[5]+"\n\nStudent Session  | "+stdData[6]+"\n\nStudent Entry Date  | "+str(stdData[7])+"\n\nStudent Entry Time  | "+str(stdData[8]))
            #showinfo("Info","Student Data From Database..\n\nStudent Roll  | "+str(stdData[0])+"\n\nStudent Name  | "+stdData[3]+"\n\nStudent Age  | "+str(stdData[4])+"\n\nStudent Course  | "+stdData[5]+"\n\nStudent Session  | "+stdData[6]+"\n\nStudent Entry Date  | "+str(stdData[7])+"\n\nStudent Entry Time  | "+str(stdData[8]))
        else:
            print("Warning","Student Details Not Found")
            #showwarning("Warning","Student Details Not Found")
    def updateStudent(self,RollNumber,UpdField,Values):
        cur.execute("select * from student where Roll={}".format(RollNumber))
        stdData=cur.fetchone()
        print(stdData)
        if(stdData!=None):
            #showinfo("Info","Student Data Present..")
            if(UpdField=="Age"):
                cur.execute("update student set Age={} where Roll={}".format(Values,RollNumber))
                db.commit()
                print("Info","Student Age Updated..")
                #showinfo("Info","Student Age Updated..")
            elif(UpdField=="FirstName"):
                cur.execute("update student set FirstName='{}',FullName='{}' where Roll={}".format(Values,(Values+" "+stdData[2]),RollNumber))
                db.commit()
                print("Info","Student FirstName Updated..")
                #showinfo("Info","Student FirstName Updated..")
            elif(UpdField=="LastName"):
                cur.execute("update student set LastName='{}',FullName='{}' where Roll={}".format(Values,(stdData[1]+" "+Values),RollNumber))
                db.commit()
                print("Info","Student LastName Updated..")
                #showinfo("Info","Student LastName Updated..")
            elif(UpdField=="Course"):
                cur.execute("update student set Course='{}' where Roll={}".format(Values,RollNumber))
                db.commit()
                print("Info","Student Course Updated..")
                #showinfo("Info","Student Course Updated..")
            elif(UpdField=="Session"):
                cur.execute("update student set Session='{}' where Roll={}".format(Values,RollNumber))
                db.commit()
                print("Info","Student Session Updated..")
                #showinfo("Info","Student Session Updated..")
        else:
            print("Warning","Student Details Not Found")
            #showwarning("Warning","Student Details Not Found")

student=Student(236017,"Divya","Shakti",18,"BCA","2023-26")
Choice=int(input("\n1.Add New Student\n2.Delete Student Through Roll Number\n3.Search Student Through Roll Number\n4.Update Student Details From Any Detail Of That Particular Student\n5.Exit From Application\n\nEnter Your Choice From Above(1-5): "))
while(Choice!=5):
    if(Choice==1):
        roll=int(input("Enter Roll Number: "))
        firstname=input("Enter First Name: ")
        lastname=input("Enter Last Name: ")
        age=int(input("Enter Age: "))
        course=input("Enter Course: ")
        session= input("Enter Session: ")
        newStudent=Student(roll,firstname,lastname,age,course,session)
        #showinfo("Info","Inserted")
    elif(Choice==2):
        roll=int(input("Enter Roll Number Want To Delete: "))
        student.deleteStudent(roll)  
    elif(Choice==3):
        roll=int(input("Enter Roll Number Want To Search: "))
        student.searchStudent(roll)
    elif(Choice==4):
        updfield=int(input("\n1.Age\n2.FirstName\n2.LastName\n4.Course\n5.Session\n6.Exited From Updation Page\n\nEnter Updation Field From Above(1-5): "))
        while(updfield!=6):
            if(updfield==1):
                roll=int(input("Enter Roll Number Want To Update: "))
                value=int(input("Enter Updated Age: "))
                student.updateStudent(roll,"Age",value)
                updfield=int(input("\n1.Age\n2.FirstName\n2.LastName\n4.Course\n5.Session\n6.Exited From Updation Page\n\nEnter Updation Field From Above(1-5): "))
            elif(updfield==2):
                roll=int(input("Enter Roll Number Want To Update: "))
                value=input("Enter Updated First Name: ")
                student.updateStudent(roll,"FirstName",value)
                updfield=int(input("\n1.Age\n2.FirstName\n2.LastName\n4.Course\n5.Session\n6.Exited From Updation Page\n\nEnter Updation Field From Above(1-5): "))
            elif(updfield==3):
                roll=int(input("Enter Roll Number Want To Update: "))
                value=input("Enter Updated Last Name: ")
                student.updateStudent(roll,"LastName",value)
                updfield=int(input("\n1.Age\n2.FirstName\n2.LastName\n4.Course\n5.Session\n6.Exited From Updation Page\n\nEnter Updation Field From Above(1-5): "))
            elif(updfield==4):
                roll=int(input("Enter Roll Number Want To Update: "))
                value=input("Enter Updated Course: ")
                student.updateStudent(roll,"Course",value)
                updfield=int(input("\n1.Age\n2.FirstName\n2.LastName\n4.Course\n5.Session\n6.Exited From Updation Page\n\nEnter Updation Field From Above(1-5): "))
            elif(updfield==5):
                roll=int(input("Enter Roll Number Want To Update: "))
                value=input("Enter Updated Session: ")
                student.updateStudent(roll,"Session",value)
                updfield=int(input("\n1.Age\n2.FirstName\n2.LastName\n4.Course\n5.Session\n6.Exited From Updation Page\n\nEnter Updation Field From Above(1-5): "))
            elif(updfield==6):
                print("\nExited From Updation Page")
            else:
                print("\nInvalid Updation Field\nTry Again\n")
                updfield=int(input("\n1.Age\n2.FirstName\n2.LastName\n4.Course\n5.Session\n\nEnter Updation Field From Above(1-5): "))
    elif(Choice==5):
        print("Info","Exited From Application\n")
        #showinfo("Info","Exited From Application")
    else:
        print("Invalid Choice-->Try Again\n")
    Choice=int(input("\n1.Add New Student\n2.Delete Student Through Roll Number\n3.Search Student Through Roll Number\n4.Update Student Details From Any Detail Of That Particular Student\n5.Exit From Application\n\nEnter Your Choice From Above(1-5): "))
#One=Student(236017,"Aniket","Kumar",20,"BCA","2023-26") 
#One.updateStudent(236017,"Course","Samrati")