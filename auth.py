
#Register
import random

def accountNumberGen():
    return random.randrange(1111111111,9999999999)


def registration():
    userName = input('Enter your Name here: \n')
    accessedUsers = {
        'Abdul':'pass1','Aremu':'pass2','Wakil':'pass3'
    }
    # accessedPassword = []
def init():
    print('Access Granted!\n Welcome %s!' % userName)
    print('These are the available Options')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaints')

def login():

    print('######### -Login- #########')
    if(userName in accessedUser):
    passWord = input('Enter your Password: \n')
    userId = accessedUsers.index(userName)

    if (passWord == accessedPassword[userId]):
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




