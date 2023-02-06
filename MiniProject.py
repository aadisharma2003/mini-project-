#RECORDEX
#CODE WRITTEN AND DESIGNED BY UDIT SHARMA AND TISHA DEELWAL

from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import webbrowser
import time
import mysql.connector
import MySQLdb

def program() :
    a=Tk()
    a.geometry("650x650")
    a.resizable(0,0)
    a.title("RECORDEX")
    a.title("WELCOME TO ABES ENGINEERING COLLEGE ")
    tkinter.messagebox.showinfo("RECORDEX", "EASE YOUR WAY FOR DATA MANAGEMENT !")

    def q0():
        new=2;
        url="http://erp.abes.ac.in/Login.aspx"
        webbrowser.open(url,new=new);
    def q1():
        new=2;
        url="https://www.abes.ac.in/courses-offered.php"
        webbrowser.open(url,new=new);
    def q2():                   
        new=2;
        url="https://abes.edu.in/"
        webbrowser.open(url,new=new);                  

    def q3():
        new=2;
        url="https://www.abes.ac.in/placement.php"
        webbrowser.open(url,new=new);

    def q4():
        new=2;
        url="https://www.abes.ac.in/life@abes_new.php"
        webbrowser.open(url,new=new);

    def q5():
        new=2;
        url="https://abes.edu.in/"
        webbrowser.open(url,new=new);
    def q7():
        exit()
        
    def q8():
        exit()
        
    def q9():
        exit()
        
    def q10():
        exit()
        
    def q11():
        exit()
        
    def q12():
        exit()
        
    def q13():    
        exit()
        
    def q6():
        b=Tk()
        b.geometry("650x450")
        b.resizable(0,0)
        b.title("DATA MANAGEMENT SYSTEM")
        b.title("MANAGE YOUR DATA")
        
        def a1():
            name=str(input("ENTER YOUR NAME : "))
            password=str(input("ENTER THE PASSWORD :"))
            if name== 'demouser' and password=='demouser':
                time.sleep(1)
                print("HELLO DEMO USER !!")
                time.sleep(2)
                print("you have following lists :")
                time.sleep(1)
                print("CLASS 1")
                time.sleep(0.5)
                print("Please wait till we open the Students list...")
                time.sleep(2)
                import MySQLdb
                import mysql.connector
                mydb = mysql.connector.connect(host="localhost",\
                                              user="root",\
                                              passwd="Mysql@123",\
                                              database="abes")
                mycursor=mydb.cursor()
                mycursor.execute("select * from class1_studentlist1 order by roll_no")
                myrecords=mycursor.fetchall()
                print(":    ROLL NO.    :ADMISSION NUMBER:      NAME       : CONTACT NUMBER :")

                for x in myrecords:
                    print(":",x[0]," "*(13-len(str(x[0]))),":",
                          x[1]," "*(13-len(str(x[1]))),":",
                          x[2]," "*(14-len(str(x[2]))),":",
                          x[3]," "*(13-len(str(x[3]))),":")
                time.sleep(3)
                print("""1. DO YOU WANT TO ADD THE STUDENT NAME 
2. DO YOU WANT TO DELETE ANY STUDENT DATA
3. DO YOU WANT TO SEARCH FOR STUDENT DETAILS BY THEIR NAME """)
                time.sleep(2)
                print("")
                insert1=int(input("ENTER THE NUMBER : "))
                if insert1== 1 :
                    import MySQLdb
                    import mysql.connector
                    print("PLEASE FILL THE FOLLOWING DATA :")
                    print("")
                    time.sleep(1)
                    rollno=input("ENTER THE ROLL NUMBER OF THE STUDENT ")
                    print("")
                    time.sleep(1)
                    admnno1=input("ENTER THE ADMISSION NUMBER OF THE STUDENT : ")
                    print("")
                    time.sleep(1)
                    name1=input("ENTER THE NAME OF THE STUDENT : ")
                    print("")
                    time.sleep(1)
                    contact1=input("ENTER THE CONTACT NUMBER OF THE STUDENT : ")
                    time.sleep(1)
                    print("")
                    print("PLEASE WAIT TILL WE ARE UPDATING YOUR STUDENT LIST")
                    mydb = mysql.connector.connect(host="localhost",\
                                              user="root",\
                                              passwd="Mysql@123",\
                                              database="abes")
                    mycursor=mydb.cursor()
                    mycursor.execute("insert into class1_studentlist1 values (%s,%s,%s,%s)",(rollno,admnno1,name1,contact1))
                    mydb.commit()
                    import MySQLdb
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",\
                                                  user="root",\
                                                  passwd="Mysql@123",\
                                                  database="abes")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from class1_studentlist1 order by Roll_no ")
                    myrecords=mycursor.fetchall()
                    print(":    ROLL NO.    :ADMISSION NUMBER:      NAME       : CONTACT NUMBER :")
                    for x in myrecords:
                        print(":",x[0]," "*(13-len(str(x[0]))),":",
                          x[1]," "*(13-len(str(x[1]))),":",
                          x[2]," "*(14-len(str(x[2]))),":",
                          x[3]," "*(13-len(str(x[3]))),":")
                    
                elif insert1== 2 :
                    print("")
                    time.sleep(1)
                    name2=input("ENTER THE STUDENT NAME YOU WANT TO DELETE FROM DATA : ")
                    mydb = mysql.connector.connect(host="localhost",\
                                              user="root",\
                                              passwd="Mysql@123",\
                                              database="abes")
                    mycursor=mydb.cursor()
                    statement1="DELETE FROM class1_studentlist1 WHERE name= %s"
                    mycursor.execute(statement1,(name2,))
                    mydb.commit()
                    import MySQLdb
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",\
                                                  user="root",\
                                                  passwd="Mysql@123",\
                                                  database="abes")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from class1_studentlist1 order by roll_no ")
                    myrecords=mycursor.fetchall()
                    print(":    ROLL NO.    :ADMISSION NUMBER:      NAME       : CONTACT NUMBER :")
                    for x in myrecords:
                        print(":",x[0]," "*(13-len(str(x[0]))),":",
                          x[1]," "*(13-len(str(x[1]))),":",
                          x[2]," "*(14-len(str(x[2]))),":",
                          x[3]," "*(13-len(str(x[3]))),":")
                elif insert1== 3:
                    print("")
                    time.sleep(1)
                    name3=input("ENTER THE NAME OF THE STUDENT YOU WANT TO SEARCH : ")
                    mydb = mysql.connector.connect(host="localhost",\
                                              user="root",\
                                              passwd="Mysql@123",\
                                              database="abes")
                    mycursor=mydb.cursor()
                    statement2="select * from class1_studentlist1 where name=%s"
                    mycursor.execute(statement2,(name3,))
                    myrecords=mycursor.fetchall()
                    print(":    ROLL NO.    :ADMISSION NUMBER:      NAME       : CONTACT NUMBER :")
                    for x in myrecords:
                        print(":",x[0]," "*(13-len(str(x[0]))),":",
                          x[1]," "*(13-len(str(x[1]))),":",
                          x[2]," "*(14-len(str(x[2]))),":",
                          x[3]," "*(13-len(str(x[3]))),":")
                else:
                    exit()
                          
            else:
                time.sleep(1)

                

                window = Tk()
                window.eval('tk::PlaceWindow %s center' %window.winfo_toplevel())
                window.withdraw()
                messagebox.showinfo('ERROR','Invalid username or password')

                
                ask1=input("Do you want  to try once again : ")
                if ask1== 'yes' :
                    a1()
                else:
                    exit()
                    
                    
        def a2():
            c=Tk()
            c.geometry("600x450")
            c.resizable(0,0)
            c.title("ATTENDANCE MANAGEMENT SYSTEM")
            c.title("ATTENDANCE ")
            def c1():
                username=input("ENTER THE USERNAME : ")
                time.sleep(1.5)
                password=input("ENTER THE PASSWORD : ")
                if username=='demouser' and password=='demouser' :
                    time.sleep(1)
                    print("1.DO YOU WANT TO SEE WHOLE ATTENDANCE LIST ?")
                    time.sleep(1)
                    print("2.DO YOU WANT TO SEE ATTENDANCE OF A PARTICULAR STUDENT ?")
                    time.sleep(2)
                    print("")
                    input1=input("ENTER THE FEATURE YOU WANT TO ACCESS : ")
                    if input1=='1' :
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                      user="root",\
                                                      passwd="Mysql@123",\
                                                      database="abes")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from class1_studentattendancelist1  ")
                        myrecords=mycursor.fetchall()
                        print(": ROLL NO. :     STUDENT NAME      : 06-02-2023 :")
                        for x in myrecords:
                            print(":",x[0]," "*(7-len(str(x[0]))),":",
                                  x[1]," "*(20-len(x[1])),":",
                                  x[2]," "*(9-len(str(x[2]))),":",)
                    if input1=='2':
                        time.sleep(1)
                        name_1=input("Enter the student name : ")
                        print("")
                        time.sleep(1)
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                       user="root",\
                                                       passwd="Mysql@123",\
                                                       database="abes")
                        mycursor=mydb.cursor()
                        statement3="select * from class1_studentattendancelist1 where name=%s"
                        mycursor.execute(statement3,(name_1,))
                        myrecords=mycursor.fetchall()
                        print(": ROLL NO. :     STUDENT NAME      : 06-02-2023 ")
                        for x in myrecords:
                           print(":",x[0]," "*(7-len(str(x[0]))),":",
                                  x[1]," "*(20-len(x[1])),":",
                                  x[2]," "*(9-len(str(x[2]))),":",)
                    
                else:
                    time.sleep(1)

                

                    window = Tk()
                    window.eval('tk::PlaceWindow %s center' %window.winfo_toplevel())
                    window.withdraw()
                    messagebox.showinfo('ERROR','Invalid username or password')

                
                    ask1=input("Do you want  to try once again : ")
                    if ask1== 'yes' :
                        a1()
                    else:
                        exit()
            
            def c3():
                exit()
            def c2():
                exit()
            clabel=Label(c,text="ATTENDANCE MANAGEMENT SYSTEM",fg="black",relief="raised",font=("aeiral",15,"bold")).place(x=125,y=100)
            m1=Label(c,text="1.DO YOU WANT TO SEE ATTENDANCE LIST ?").place(x=20,y=200)
            m3=Label(c,text="EXIT!!").place(x=200,y=400)

            m_1=Button(c,text="YES",fg="black",bg="light blue",relief="raised",command=c1).place(x=400,y=200)
            m_a=Button(c,text="NO",fg="black",bg="light blue",relief="raised",command=c2).place(x=500,y=200)
            m_3=Button(c,text="YES",fg="black",bg="light blue",relief="raised",command=c3).place(x=300,y=400)
            c.mainloop()
            
        def a3():
            username2=input("ENTER THE USERNAME : ")
            password2=input("ENTER THE PASSWORD : ")
            if username2=='demouser' and password2=='demouser' :
                time.sleep(1)
                print("1.DO YOU WANT TO SEE MARKS OF THE STUDENTS ? ")
                time.sleep(1)
                print("2.DO YOU WANT TO SEE MARKS OF A PARTICULAR STUDENT ? ")
                time.sleep(1)
                print("3.DO YOU WANT TO GIVE MARKS ?")
                time.sleep(1)
                print("")
                input2=input("ENTER THE FEATURE YOU WANT TO ACCESS : ")
                if input2=='1' :
                    import MySQLdb
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",\
                                                   user="root",\
                                                   passwd="Mysql@123",\
                                                   database="abes")
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from class1_markslist1 ")
                    myrecords=mycursor.fetchall()
                    print(": ROLL NO  :     STUDENT NAME      :  ST1  :    ST2    : PUE :")
                    for x in myrecords:
                        print(":",x[0]," "*(7-len(str(x[0]))),":",
                                  x[1]," "*(20-len(str(x[1]))),":",
                                  x[2]," "*(4-len(str(x[2]))),":",
                                  x[3]," "*(8-len(str(x[3]))),":",
                                  x[4]," "*(2-len(str(x[4]))),":",)
                if input2=='2' :
                    time.sleep(1)
                    name_3=input("Enter the student name : ")
                    print("")
                    time.sleep(1)
                    import MySQLdb
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",\
                                                   user="root",\
                                                   passwd="Mysql@123",\
                                                   database="abes")
                    mycursor=mydb.cursor()
                    statement6="select * from class1_markslist1 where name=%s"
                    mycursor.execute(statement6,(name_3,))
                    myrecords=mycursor.fetchall()
                    print(": ROLL NO  :     STUDENT NAME      :  ST1  :    ST2    : PUE :")
                    for x in myrecords:
                        print(":",x[0]," "*(7-len(str(x[0]))),":",
                                  x[1]," "*(20-len(str(x[1]))),":",
                                  x[2]," "*(4-len(str(x[2]))),":",
                                  x[3]," "*(8-len(str(x[3]))),":",
                                  x[4]," "*(2-len(str(x[4]))),":",)
                if input2=='3':
                    student_name=input("ENTER THE NAME OF THE STUDENT YOU WANT TO GIVE MARKS : ")
                    term=input("ENTER THE TERM YOU WANT TO GIVE MARKS FOR  : ")
                    marks_1=input("ENTER THE MARKS OF THE STUDENT : ")
                    if term== 'ST1' :
                        
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                       user="root",\
                                                       passwd="Mysql@123",\
                                                       database="abes")
                        mycursor=mydb.cursor()
                        execute1="update class1_markslist1 set ST1 =%s where name=%s"
                        mycursor.execute(execute1,(marks_1,student_name))
                        mydb.commit()
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                       user="root",\
                                                       passwd="Mysql@123",\
                                                       database="abes")
                        mycursor=mydb.cursor()
                        statement6="select * from class1_markslist1 "
                        mycursor.execute(statement6)
                        myrecords=mycursor.fetchall()
                        print(": ROLL NO  :     STUDENT NAME      :  ST1  :    ST2    : PUE :")
                        for x in myrecords:
                            print(":",x[0]," "*(7-len(str(x[0]))),":",
                                  x[1]," "*(20-len(str(x[1]))),":",
                                  x[2]," "*(4-len(str(x[2]))),":",
                                  x[3]," "*(8-len(str(x[3]))),":",
                                  x[4]," "*(2-len(str(x[4]))),":",)
                    if term== 'ST2' :
                        
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                       user="root",\
                                                       passwd="Mysql@123",\
                                                       database="abes")
                        mycursor=mydb.cursor()
                        execute1="update class1_markslist1 set ST2 =%s where name=%s"
                        mycursor.execute(execute1,(marks_1,student_name))
                        mydb.commit()
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                       user="root",\
                                                       passwd="Mysql@123",\
                                                       database="abes")
                        mycursor=mydb.cursor()
                        statement6="select * from class1_markslist1 "
                        mycursor.execute(statement6)
                        myrecords=mycursor.fetchall()
                        print(": ROLL NO  :     STUDENT NAME      :  ST1  :    ST2    : PUE :")
                        for x in myrecords:
                            print(":",x[0]," "*(7-len(str(x[0]))),":",
                                  x[1]," "*(20-len(str(x[1]))),":",
                                  x[2]," "*(4-len(str(x[2]))),":",
                                  x[3]," "*(8-len(str(x[3]))),":",
                                  x[4]," "*(2-len(str(x[4]))),":",)
                    if term== 'PUE' :
                        
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                       user="root",\
                                                       passwd="Mysql@123",\
                                                       database="abes")
                        mycursor=mydb.cursor()
                        execute1="update class1_markslist1 set PUE =%s where name=%s"
                        mycursor.execute(execute1,(marks_1,student_name))
                        mydb.commit()
                        import MySQLdb
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",\
                                                       user="root",\
                                                       passwd="Mysql@123",\
                                                       database="abes")
                        mycursor=mydb.cursor()
                        statement6="select * from class1_markslist1 "
                        mycursor.execute(statement6)
                        myrecords=mycursor.fetchall()
                        print(": ROLL NO  :     STUDENT NAME      :  ST1  :    ST2    : PUE :")
                        for x in myrecords:
                            print(":",x[0]," "*(7-len(str(x[0]))),":",
                                  x[1]," "*(20-len(str(x[1]))),":",
                                  x[2]," "*(4-len(str(x[2]))),":",
                                  x[3]," "*(8-len(str(x[3]))),":",
                                  x[4]," "*(2-len(str(x[4]))),":",)
            else:
                        time.sleep(1)

                

                        window = Tk()
                        window.eval('tk::PlaceWindow %s center' %window.winfo_toplevel())
                        window.withdraw()
                        messagebox.showinfo('ERROR','Invalid username or password')

                
                        ask1=input("Do you want  to try once again : ")
                        if ask1== 'yes' :
                            a1()
                        else:
                            exit()    

                        
        def a4():
            exit()
            
        def a5():
            exit()
            
        def a6():
            exit()
            
        def a7():
            exit()
            
        def a8():
            exit()
       
        c1=Label(b,text="DATA MANAGEMENT SYSTEM",fg="black",relief="raised",font=("aerial",15,"bold")).place(x=180,y=100)
        n1=Label(b,text="1. DO YOU WANT TO SEE STUDENTS LIST ?").place(x=20,y=250)
        n2=Label(b,text="2. DO YOU WANT TO GIVE ATTENDANCE?").place(x=20,y=300)
        n3=Label(b,text="3. DO YOU WANT TO GIVE MARKS ?").place(x=20,y=350)
        n4=Label(b,text="EXIT!!").place(x=250,y=600)

        c_2=Button(b,text="YES",fg="black",bg="light blue",relief="raised",command=a1).place(x=400,y=250)
        c2=Button(b,text="NO",fg="black",bg="light blue",relief="raised",command=a5).place(x=500,y=250)
        c_3=Button(b,text="YES",fg="black",bg="light blue",relief="raised",command=a2).place(x=400,y=300)
        c3=Button(b,text="NO",fg="black",bg="light blue",relief="raised",command=a6).place(x=500,y=300)
        c_4=Button(b,text="YES",fg="black",bg="light blue",relief="raised",command=a3).place(x=400,y=350)
        c4=Button(b,text="NO",fg="black",bg="light blue",relief="raised",command=a7).place(x=500,y=350)
        c_5=Button(b,text="YES",fg="black",bg="light blue",relief="raised",command=a4).place(x=300,y=600)
        c5=Button(b,text="NO",fg="black",bg="light blue",relief="raised",command=a8).place(x=350,y=600)
        b.mainloop()

    l=Label(a,text="RECORDEX",fg="black",bg="blue",relief="raised",font=("aerial",15,"bold")).place(x=250,y=100)
    l1=Label(a,text="DO YOU WANT TO LOGIN IN OUR ONLINE PORTAL ?").place(x=20,y=200)
    l2=Label(a,text="DO YOU WANT TO TAKE ADMISSION IN BTECH ?").place(x=20,y=250)
    l3=Label(a,text="DO YOU WANT TO TAKE ADMISSION IN MBA ?").place(x=20,y=300)
    l4=Label(a,text="DO YOU WANT TO SEE OUR PLACEMENT RECORDS ?").place(x=20,y=350)
    l5=Label(a,text="DO YOU WANT TO SEE LIFE@ABES?").place(x=20,y=400)
    l6=Label(a,text="DO YOU WANT TO SEE ABES BUSINESS SCHOOL PORTAL ?").place(x=20,y=450)
    l7=Label(a,text="DO YOU WANT ACCESS OUR DATA MANAGEMENT SYSTEM ?").place(x=20,y=500)
    b_1=Button(a,text="YES",fg="black",bg="light blue",relief="raised",command=q0).place(x=400,y=200)
    b1=Button(a,text="NO",fg="black",bg="light blue",relief="raised",command=q7).place(x=500,y=200)

    b_2=Button(a,text="YES",fg="black",bg="light blue",relief="raised",command=q1).place(x=400,y=250)
    b2=Button(a,text="NO",fg="black",bg="light blue",relief="raised",command=q8).place(x=500,y=250)

    b_3=Button(a,text="YES",fg="black",bg="light blue",relief="raised",command=q2).place(x=400,y=300)
    b3=Button(a,text="NO",fg="black",bg="light blue",relief="raised",command=q9).place(x=500,y=300)

    b_4=Button(a,text="YES",fg="black",bg="light blue",relief="raised",command=q3).place(x=400,y=350)
    b4=Button(a,text="NO",fg="black",bg="light blue",relief="raised",command=q10).place(x=500,y=350)

    b_5=Button(a,text="YES",fg="black",bg="light blue",relief="raised",command=q4).place(x=400,y=400)
    b5=Button(a,text="NO",fg="black",bg="light blue",relief="raised",command=q11).place(x=500,y=400)

    b_6=Button(a,text="YES",fg="black",bg="light blue",relief="raised",command=q5).place(x=400,y=450)
    b6=Button(a,text="NO",fg="black",bg="light blue",relief="raised",command=q12).place(x=500,y=450)

    b_7=Button(a,text="YES",fg="black",bg="light blue",relief="raised",command=q6).place(x=400,y=500)
    b7=Button(a,text="NO",fg="black",bg="light blue",relief="raised",command=q13).place(x=500,y=500)



    a.mainloop()
program()
