#Time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Generating random number for Account Number
import random
database = {} #database dict
def accountNumberGen():
    return random.randrange(1111111111,9999999999)


def init():
    print('Welcome PyBank!!!')
    print('Here we show you Snake Banking......$$$$$')
    checkedAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(checkedAccount == 1):
        
        login()
    elif(checkedAccount == 2):
        
        registration()
    else:
        print("You have selected invalid option")
        init()

def login():
    print('######### -Login- #########')
    inputtedAccNumber = int(input("What is your account number? \n"))
    password = input("Enter your created password \n")

    for _accountNumber,userDetails in database.items():
        if(_accountNumber == inputtedAccNumber):
            if(userDetails[3] == password):
                bankOperations(userDetails)
               
                
    print('Invalid account or password')
    login()


def registration():
    _email = input('Enter your email address: \n')
    _firstname = input('Enter your firstname : \n')
    _lastname = input('Enter your lastname : \n')
    _password =  input('Enter your Password: \n')

    _accountNumber = accountNumberGen()

    database[_accountNumber] = [ _email, _firstname, _lastname, _password,_accountNumber ]

    print("Your Account Has been created")
    print(" ===== ==== ====== ===== ====== ")
    print("Your account number is: %d" % _accountNumber)
    print("Make sure you keep it safe")
    print(" ==== ==== ====== ===== =====")

    login()







def bankOperations(accessedUser):
    print("date and time =", dt_string)
    print(f"Access Granted!\n Welcome {accessedUser[1], accessedUser[2]}! with account number {accessedUser[4]}")
    #print(f"Access Granted!\n Welcome {_firstname + ' ' +_lastname}! with account number {_accountNumber}")
    #print(f"Welcome {_lastname} with Account number {_accountNumber}")
    selectedOption = int(input('What would you like to do? (1) Withdrawal (2) Deposite (3) Report Issues (4) logout\n'))
    if(selectedOption == 1):
        print("You've selected %s"% selectedOption)
        withdrawalMoney()
    elif(selectedOption == 2):
        print("You've selected %s"% selectedOption)
        depositMoney()
    elif(selectedOption == 3):
        print("You've selected %s"% selectedOption)
        reportIssue()
    
    elif(selectedOption==4):
        logout()
        
    else:
        print("Invalid selection, try again")
        bankOperations(accessedUser)
    #else:
        #print('Access Denied, incorrect password!')
        #init()
#else:
    #print('User not found, Try again!')
    #logout()












def withdrawalMoney():
    withdrawalMoney = int(input('How much would you like to withdraw? \n'))
    if(type(withdrawalMoney)) == int:
        print('Take your cash')
    else:
        print('invalid input!')

def depositMoney():
    depositMoney = int(input('How much would you like to deposit? \n'))
    if(type(depositMoney)) == int:
        oldBal = 0
        currentBal = oldBal + depositMoney 
        print('Current balance %s'%currentBal)
    else:
        print('invalid input!')

def reportIssue():
    reportIssue = str(input('What issue will you like to report? \n'))
    if (type(reportIssue) == str):
        print('Complaints received')
        print('Thank you for contacting us')
    else:
        print('Complaints not recorded')



def logout():
    exit()

#### ACTUAL BANKING SYSTEM #####

init()




