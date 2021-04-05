#Time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#user credentialsA
userName = input('Enter your Name here: \n')
accessedUser = ['Abdul','Aremu','Wakil']
accessedPassword = ['pass1','pass2','pass3']

if(userName in accessedUser):
    passWord = input('Enter your Password: \n')
    userId = accessedUser.index(userName)

    if (passWord == accessedPassword[userId]):
        print("date and time =", dt_string)
        print('Access Granted!\n Welcome %s!' % userName)
        print('These are the available Options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaints')

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
    else:
        print('Access Denied, incorrect password!')
else:
    print('User not found, Try again!')



