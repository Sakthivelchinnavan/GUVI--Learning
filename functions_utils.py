import re
import csv
import getpass
def get():
    Password=input()
    if (len(Password)<8 and len(Password)>16):
        print("Password length should be from 8 to 16 characters. Please enter a valid Password")
        print("Do you want to enter correct password now? press (Y/y)")
        ch=input()
        if ch == 'Y' or ch == 'y':
            print("Please enter your Password: ")
            get()
    elif not re.search("[A-Z]",Password):
        print("Invalid Password. Please enter a valid Password")
        get()
    elif not re.search("[a-z]",Password):
        print("Invalid Password. Please enter a valid Password")
        get()
    elif not re.search("[0-9]",Password):
        print("Invalid Password. Please enter a valid Password")
        get()
    elif not re.search("[@$!#]",Password):
        print("Invalid Password. Please enter a valid Password")
        get()
    else:
        print("Password is valid and Updated successfully\n")
        return Password
def getpwd():
    print("Have you forgotten your Password? Type Y/y to retrieve or N/n to create a new password")
    F = input()

    if F == 'Y' or F == 'y':
        f2 = open("Login.csv", "r")

        rows = csv.reader(f2)

        userId = input("Enter the user-id: ")
        flag = True
        for record in rows:
            #print(record)
            if record[0] == userId:
                print("The password is: ", record[1])
            #else:
                #print("No user registered !!!!")
    elif F == 'N' or F == 'n':

        updatefunc()

def updatefunc():
    new_rows = []
    stid= input("Enter your emailId : ")
    fieldnames = ["EmailId", 'Password']
    with open('Login.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if stid == row['EmailId']:
                print("Type your new Password")
                password = get()
                row['Password'] = password
            new_rows.append({'EmailId': row['EmailId'], 'Password': row['Password']})

    with open('Login.csv', 'w') as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames,lineterminator='\n')
        writer.writerows(new_rows)

def login():
    f2 = open("Login.csv", "r")
    rows = csv.reader(f2)
    userId = input("Enter the user-id: ")
    Pwd = input("Enter the Password: ")
    #Pwd= getpass.getpass("Enter the Password: ")
    flag = True
    for record in rows:
        if record:
            if record[0] == userId and record[1] == Pwd:
                print("You are now logged in")
                flag = False
                break
    if flag:
        print("Invalid Credentials")
        #getpwd()


def fcheck():
    print("Please provide your username. We need to verify whether it is registered!")
    Username = input("Enter your Username : ")
    with open("Login.csv", "r") as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row:
                if row[0] == Username:
                    log = True
                else:
                    log = False

        if log == False:
            print("Username does not exists")
            #exit()
            #print("Please create a new user id :")
            Email = input("Enter your email id to register:  ")
            check(Email)
            print("Please enter your Password: ")
            Password = get()
            login()

        else:
            print("User Name exists! You may now proceed to login!")
            login()
def check(Email):
    if re.search("^1",Email):
        print("Invalid email")
    else:
        if(re.fullmatch('[A-Za-z]+[A-Za-z0-9_+*]+@[A-Za-z0-9]+\.[A-Za-z]{2,}',Email)):
            print("Valid email\n")
        else:
            print("Invalid email-Id")
            Email=input("Enter your Email id:  ")
            check(Email)  # recursive function
