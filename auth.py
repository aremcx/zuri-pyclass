
# Generating random number for Account Number
import random

def accountNumberGen():
    return random.randrange(1111111111,9999999999)


def registration():
    _email = input('Enter your email address: \n')
    _first_name = input('Enter your firstname : \n')
    _last_name = input('Enter your lastname : \n')
    _password =  input('Enter your Password: \n')

    _accountNumber = accountNumberGen()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" ===== ==== ====== ===== ====== ")
    print("Your account number is: %d" % _accountNumber)
    print("Make sure you keep it safe")
    print(" ==== ==== ====== ===== =====")

    login()

    
def init():
    print('Access Granted!\n Welcome %s!' % userName)
    print('These are the available Options')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaints')

def login():
    print('######### -Login- #########')
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in da1tabase.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               
                
    print('Invalid account or password')
    login()



















    userName = input('Enter your Name here: \n')
    accessedUsers = {
        'Abdul':'pass1','Aremu':'pass2','Wakil':'pass3'
    }
    # accessedPassword = []


    if(userName in accessedUser):
    passWord = input('Enter your Password: \n')
    userId = accessedUsers.index(userName)

    if(passWord == accessedPassword[userId]):
        print("date and time =", dt_string)
        print('Access Granted!\n Welcome %s!' % userName)
        print('These are the available Options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaints')

def bankOperations():
    selectedOption = int(input('Enter your option\n'))
        if(selectedOption == 1):
            print("You've selected %s"% selectedOption)
            def withdrawalMoney():
                withdrawalMoney = int(input('How much would you like to withdraw? \n'))
                if(type(withdrawalMoney)) == int:
                    print('Take your cash')
                else:
                    print('invalid input!')

                elif(selectedOption == 2):
                    print("You've selected %s"% selectedOption)
                    def depositMoney():
                        depositMoney = int(input('How much would you like to deposit? \n'))
                        if(type(depositMoney)) == int:
                            oldBal = 0
                            currentBal = oldBal + depositMoney 
                        print('Current balance %s'%currentBal)
                        else:
                            print('invalid input!')

                elif(selectedOption == 3):
                    print("You've selected %s"% selectedOption)
                    def reportIssue():
                        reportIssue = str(input('What issue will you like to report? \n'))
                        if (type(reportIssue) == str):
                        print('Complaints received')
                        print('Thank you for contacting us')
                        else:
                            print('Complaints not recorded')


        else:
            print("Invalid selection, try again")
    else:
        print('Access Denied, incorrect password!')
else:
    print('User not found, Try again!')
    def logout():
        #exit

#### ACTUAL BANKING SYSTEM #####

init()




