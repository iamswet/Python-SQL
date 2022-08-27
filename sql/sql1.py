from pack import datastr
from pack import show
from pack import usad
import mysql.connector

admin={"Tarun":2255,"Karan":1616}

mydb=mysql.connector.connect(host="localhost",user="root",passwd="MySQL123!")
mycursor=mydb.cursor()
mycursor.execute("use elecbill")
l_customer=list()

name=usad.useradmin()
if name=="user":
    ID=input("Enter your customer ID: ")
    show.select_table(mycursor,ID)
elif name=="admin":
    usad.adminverify(admin)
    while True:
        print("Enter 1 to see all customer IDs")
        print("Enter 2 to see customer's bill")
        print("Enter 3 to delete a customer ID")
        print("Enter 4 to create new customer ID")
        print("Enter 5 to enter new record(s) in a customer account")
        
        choice=int(input("Enter choice: "))
        
        if choice==1:
            show.show_tables(mycursor,l_customer)
            print(l_customer)    
        
        elif choice==2:
            ID=input("Enter the customer ID: ")
            show.select_table(mycursor,ID)
            
        elif choice==3:
            datastr.del_table(mycursor)
            mydb.commit()
            
        elif choice==4:
            datastr.create_table(mycursor)
            mydb.commit()
        
        elif choice==5:
            customer=input("Enter the customer ID: ")
            c="Y"
            while c=="Y":
                datastr.entry(mycursor,customer)
                c=input("Do you wish to enter more records(Y/N) : ")
            mydb.commit()

        else:
            print("Wrong input")
        cont=usad.wish()
        if cont==True:
            break
        elif cont==False:
            pass
