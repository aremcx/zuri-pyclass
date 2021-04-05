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