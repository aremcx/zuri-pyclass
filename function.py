#Time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

import random

def accountNumberGen():
    return random.randrange(1111111111,9999999999)


#Register

def registration():
    _email = input('Enter your email address: \n')
    _firstname = input('Enter your firstname : \n')
    _lastname = input('Enter your lastname : \n')
    _password =  input('Enter your Password: \n')

    _accountNumber = accountNumberGen()

    print(_accountNumber)
    #userName = input('Enter your Name here: \n')
    #accessedUser = ['Abdul':'pass1','Aremu':'pass2','Wakil':'pass3']
    #accessedPassword = ['pass1','pass2','pass3']
    # database[accountNumber] = [ _firstname, _lastname, _email, _password ]

    print("Your Account Has been created")
    print(" ===== ==== ====== ===== ====== ")
    print("Your account number is: %d" % _accountNumber)
    print("Make sure you keep it safe")
    print(" ====== ==== ====== ===== =====")


registration()

login()

    
def init():
    print(f"Access Granted!\n Welcome {_firstname + ' ' +_lastname}! with account number {_accountNumber}")
    print("date and time =", dt_string)
    print('These are the available Options')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaints')
bankOperations()

def login():
    inputtedName = input('Enter your first name')
    if _accountNumber is True and  inputtedName == _firstname:
        print('Login successfully')
login()
        #passWord = input('Enter your Password: \n')
        #userId = accessedUser.index(userName)
init()

    #if (passWord == accessedPassword[userId]):
        #print("date and time =", dt_string)
        #print('Access Granted!\n Welcome %s!' % userName)
        #print('These are the available Options')
        #print('1. Withdrawal')
        #print('2. Cash Deposit')
        #print('3. Complaints')

def bankOperations():
    selectedOption = int(input('Enter your option\n'))
    if(selectedOption == 1):
        print("You've selected %s"% selectedOption)
        withdrawalMoney = int(input('How much would you like to withdraw? \n'))
        if(type(withdrawalMoney)) == int:
            print('Take your cash')
        else:
            print('invalid input!')

    elif(selectedOption == 2):
        print("You've selected %s"% selectedOption)
        depositMoney = int(input('How much would you like to deposit? \n'))
        if(type(depositMoney)) == int:
            oldBal = 0
            currentBal = oldBal + depositMoney 
            print('Current balance %s'%currentBal)
        else:
            print('invalid input!')

    elif(selectedOption == 3):
        print("You've selected %s"% selectedOption)
        reportIssue = str(input('What issue will you like to report? \n'))
        if (type(reportIssue) == str):
            print('Complaints received')
            print('Thank you for contacting us')
        else:
            print('Complaints not recorded')


    else:
        print("Invalid selection, try again")
    exit()
    #else:
        #print('Access Denied, incorrect password!')
#else:
    #print('User not found, Try again!')




