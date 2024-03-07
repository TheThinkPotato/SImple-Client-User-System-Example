import userControl
import os

currentUser = None
accountsFile = 'accounts.txt'

class User:
    def __init__(self, username, password, question, answer):
        global id
        self.username = username
        self.password = password
        self.question = question
        self.answer = answer
        self.loggedIn = False 
        
    def isLoggedIn(self):
        return self.loggedIn

    def setLoggedIn(self, loggedIn):
        self.loggedIn = loggedIn

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def getQuestion(self):
        return self.question
    
    def getAnswer(self):
        return self.answer
    
    def setPassword(self, password):
        self.password = password
    
    def setQuestion(self, question):
        self.question = question

    def setAnswer(self, answer):
        self.answer = answer

    def getId(self):
        return self.id

    def saveUserToFile(self):        
        with open(accountsFile, 'a') as file:
            file.write(self.username + ',' + self.password + ',' + self.question + ',' + self.answer + '\n')
    
    def updateUserToFile(self):
        with open(accountsFile, 'r') as file:
            lines = file.readlines()
        with open(accountsFile, 'w') as file:
            for line in lines:
                if line.strip() and line.split(',')[0] != self.username:
                    file.write(line)
            file.write(self.username + ',' + self.password + ',' + self.question + ',' + self.answer + '\n')              

def viewAccounts():
    userControl.clearScreen()
    print("\n\n System User Details")    
    print("----------------------------------------------------------")
    for user in users:
        print("Username:",user.getUsername() , "\t Password:", user.getPassword() + "\nQuesiton:" , user.getQuestion() , "\nAnswer:" , user.getAnswer())
        print("----------------------------------------------------------")
    print("\n\n")

def setCurrentUser(user):
    global currentUser
    currentUser = user

def getCurrentUser():
    global currentUser
    return currentUser

def loadData():
    users = []

    #if accounts file does not exist return empty data
    if not os.path.exists(accountsFile):
        User("admin", "admin", "What is your favorite color?", "blue")
        users.append(User("admin", "admin", "What is your favorite color?", "blue"))
        users[0].saveUserToFile()
        return users
    
    with open(accountsFile, 'r') as file:
        for line in file:
            if line.strip() != "":                
                username, password, question, answer = line.split(',')                         
                users.append(User(username, password, question, answer))
    
    return users

users = loadData()

