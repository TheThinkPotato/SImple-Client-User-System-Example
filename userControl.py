import random
import os
from user import *

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')        

def changePassword(user): 
    print(user.getUsername() + ' changing password')
    while True:   
        newPassword = input('Enter new password: ')    
        if passwordRules(newPassword):
            break
    user.setPassword(newPassword)
    user.updateUserToFile()
    print('\n\nPassword changed successfully')

def resetPassword():
    userName = input("Enter username: ")            
    success = False
    for user in users:
        if user.getUsername() == userName:                                              
            success = resetPasswordUser(user)
            break
    if(not success):
        print("\nUser not found or invalid answer to security question.")
    return

def resetPasswordUser(user):   
    inputAnswer = input(user.getQuestion() + "?: ")    
    if inputAnswer != user.getAnswer().strip():
        print('\n\nIncorrect answer.')
        return False
    changePassword(user)
    return True

def usernameRules(password):            
    if len(password) < 6:
        print("\nUsername must be at least 6 characters")
        return False
    if len(password) > 12:
        print("\nUsername must be at most 12 characters") 
        return False
    return True


def passwordRules(password):            
    if len(password) < 6:
        print("\nPassword must be at least 6 characters")
        return False
    if len(password) > 12:
        print("\nPassword must be at most 12 characters")
        return False
    return True

def setSecurityQuestion(user):
    print("\n\nPlease set your security question")
    question = input("Enter your question: ")
    answer = input("Enter your answer: ")
    user.setQuestion(question)
    user.setAnswer(answer)
    return
    

def registerUser():
    
    def registerUserOptions():
        print("\n\n(1) Create Password\t(2) Generate Password")
        print("----------------------------------------")
        return input("Enter your choice: ")
    
    def generatePassword():
        i = 0        
        passwordChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"        
        password = str()
        while i <= 12:
            password = password + random.choice(passwordChars)        
            i+=1
        
        return password

    clearScreen()

    while True:
        username = input('\n\nEnter username: ')
        if usernameRules(username):
            break    

    for user in users:
        if user.getUsername() == username:
            print('\n\nUser already exists!')
            return
    
    selection = registerUserOptions()    
    newPassword = None

    if selection == "1":
        while True:
            password = input('Enter password: ')
            if passwordRules(password):                                            
                newPassword = password
                break
    
    elif selection == "2":
        password = generatePassword()
        print('\n\nYour generated password: ', password)
        newPassword = password
    
    newUser = User(username, newPassword, None, None)
    setSecurityQuestion(newUser)        
    users.append(newUser)
    newUser.saveUserToFile()
    print('\nUser registered successfully')


def login():
    clearScreen() 
    global users
    passwordTries = 3
    passwordTriesCount = 0    
    username = input('Enter username: ')
    
    while passwordTries > 0:        
        password = input('Enter password: ')    
    
        for user in users:
            if user.getUsername() == username and user.getPassword() == password:
                setCurrentUser(user)
                user.setLoggedIn(True)
                print('\n\nWelcome, ' + username)
                print(getCurrentUser().getUsername() + ' logged in')
                return
        else:
            passwordTriesCount += 1
            print('Login fail attempt', passwordTriesCount)
            if passwordTries == 1:
                print("\nPlease contact the system administrator!")
            passwordTries -= 1
