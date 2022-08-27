#pass mycursor as argument

def show_tables(abc,l):           # show tables (FOR ADMIN) 
    abc.execute("show tables;")
    for x in abc:
        for j in x:
            if j not in l:
                l.append(j)
    
def select_table(abc,name):          #display contents of table (for USER and ADMIN)
    word="select * from "+name+";"
    abc.execute(word)
    print("Name   Street_name   Pin_code   Month   Phone   Consume   Bill")
    for i in abc:
        print(i)
    
