accessedUsers = {
        'Abdul':'pass1','Aremu':'pass2','Wakil':'pass3'
    
    }
print(accessedUsers)

accessedUsers['ola']='pass4'
print(accessedUsers)
accessedUsers.pop('ola')
print(accessedUsers)

def textRepeater(name):
    return name + ' called something inside a function \n'


print(textRepeater('Abdul') * 4)
import random

def accountNumberGen():
    return random.randrange(1111111111,9999999999)


def registration():
    _email = input('Enter your email address: \n')
    _first_name = input('Enter your firstname : \n')
    _last_name = input('Enter your lastname : \n')
    _password =  input('Enter your Password: \n')

    _accountNumber = accountNumberGen()

    print(_accountNumber)

    database[accountNumber] = [ _first_name, _last_name, _email, _password ]

    print("Your Account Has been created")
    print(" ===== ==== ====== ===== ====== ")
    print("Your account number is: %d" % _accountNumber)
    print("Make sure you keep it safe")
    print(" ==== ==== ====== ===== =====")


registration()

    #login()
