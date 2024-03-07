import time
from userControl import *
from user import *

def welcome():
    print("\n\n---------------------------------------------------")
    print("\t\tSystem Main Menu")
    print("---------------------------------------------------\n")


def options():    
    print("(1) Login\t(2) Register\t(3) Reset Password")   
    
    if getCurrentUser() != None and getCurrentUser().isLoggedIn() == True and getCurrentUser().getUsername() != "admin":
        print("(4) Change Password\t\t(6) Exit" )        
    elif getCurrentUser() != None and getCurrentUser().isLoggedIn() == True and getCurrentUser().getUsername() == "admin":
        print("(4) Change Password\t\t(5) View Accounts\n(6) Exit" )
    else:
        print("(6) Exit")
    
    print("---------------------------------------------------")
    return input("Enter your choice: ")
    
def totalTime():
    systemRunTime = time.time() - startTime    
    minutes = int(systemRunTime / 60)
    seconds =  int(systemRunTime % 60)
    return minutes, seconds

clearScreen()
startTime = time.time()
users = loadData()

menuInput = ""
while menuInput != "6":
    welcome()
    menuInput = options()
    
    match menuInput:
        case "1":
            login()
        case "2":            
            registerUser()
        case "3":
            resetPassword()
        case "4":
            if getCurrentUser() == None:
                print("\nInvalid choice")   
            else:
                changePassword(getCurrentUser())            
        case "5":
            if getCurrentUser() != None and getCurrentUser().isLoggedIn() == True and getCurrentUser().getUsername() == "admin":
                viewAccounts()
            else:
                print("\nInvalid choice")   

        case "6":
            print("\n\nGoodbye...")
        case _:
            print("\nInvalid choice")


time.sleep(2)
minutes, seconds = totalTime()
print("Total system run time", minutes, "minutes and", seconds, "seconds\n")
