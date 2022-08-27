detail1="(Name char(50),Street_name char(50),Pin_code int,Month varchar(5),Phone int,Consume int,bill int);"
detail2="(Name ,Street_name ,Pin_code ,Month ,Phone ,Consume ,bill)"
rate=50

def entry(abc,customer):                #Entering new records FOR ADMIN 
    global rate
    global detail2
    name=input("Enter the name:")
    street=input("Enter the street name:")
    pin=int(input("Enter the PIN code:"))
    month=input("Enter the month:")
    phone=int(input("Enter the phone number:"))
    consume=int(input("Enter electricity consumed:"))
    bill=rate*consume
    value="("+'"'+name+'"'+","+'"'+street+'"'+","+str(pin)+","+'"'+str(month)+'"'+","+str(phone)+","+str(consume)+","+str(bill)+')'
    word="insert into "+str(customer)+detail2+" values "+value+";"
    abc.execute(word)
    
def create_table(abc):      #New table creation (FOR ADMIN)
    global detail1
    name=input("Enter customer ID:")
    word="create table "+name+" "+detail1
    word=str(word)
    abc.execute(word)

def del_table(abc):         #Deleting a table (For ADMIN)
    name=input("Enter the customer ID to be deleted: ")
    word="drop table "+name+";"
    abc.execute(word)
    
