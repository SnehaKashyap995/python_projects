master_pwd=input("What is the master password? ")

def view():
    with open('Password.txt', 'r') as f:      #using 'with' means that the file will be closed on its own
        for line in f.readlines():
            data=line.rstrip()          #rstrip() will remove the extra line space
            user,passw=data.split(" | ")
            print("Account:",user,"\tPassword:",passw)

def add():
    name=input("Account name:")
    pwd=input("Password:")

    with open('Password.txt', 'a') as f:
        f.write(name+" | "+pwd+"\n")

while True:
    mode=input("Press 'q' to quit\nWould you like to add a new password or view the existing ones? (view/add): ").lower()
    if mode=='q':
        quit()
    if mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print("Not a valid input!")
    
    