def useradmin():                  #Selection Admin/User
    name=input("Enter whether user or admin: ")
    name=name.lower()
    if name in ["user","admin","Admin","User"]:
        return name
    else:
        print("Wrong input")
        useradmin()

def adminverify(dict):             #Verfiy if admin or not
    User=input("Enter your username: ")
    pin=int(input("Enter the pin: "))
    if User not in dict:
        print("Wrong username or PIN")
        adminverify(dict)
    elif dict[User]==pin:
        return True
    else:
        print("Wrong username or PIN")
        adminverify(dict)
        

def wish():                         #Internal while loop(FOR ADMIN)
    wish=input("Do you wish to end the session(Y/N): ")
    if wish=="Y":
        return True
    elif wish=="N":
        return False
    else:
        print("Wrong input")
        wish()
