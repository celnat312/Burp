from sqlite3 import *

class Account():
    def __init__(self, uname = '', pw = '', pfp = None, email = ""):
        self.uname = uname
        self.pw = pw
        self.pfp = pfp
        self.email = email

    def getUname(self):
        return self.uname
    
    def getPw(self):
        return self.pw
    
    def getPfp(self):
        return self.pfp
    
    def getEmail(self):
        return self.email
    
    