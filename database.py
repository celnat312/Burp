from sqlite3 import * 

# Creating the table

class Table():
    def __init__(self):
        # Opening and accessing the database alongside initialising cursor
        open('CTD.db', 'w')
        self.db = connect("CTD.db")
        self.cursor = self.db.cursor()

    def commitChanges(self):
        # Committing the changes
        self.db.commit()
    
    def closeConnection(self):
        # Closing the database
        self.db.close()

class AccTable(Table):
    def __init__(self):
        try: 
            self.cursor.execute("CREATE TABLE AccountDetails(\
                    Username TEXT NOT NULL ,\
                    Password TEXT NOT NULL ,\
                    ProfilePicture BLOB,\
                    Email TEXT,\
                    PRIMARY KEY(Username));")
            print("Account Table created")
        except:
            print("Table was not created.")

    def getUserExists(self, uName):
        try:
            # Fetches the Account Details for the specified username
            self.cursor.execute("SELECT * FROM AccountDetails WHERE Username = ?", (uName))
            data = self.cursor.fetchone()
            if data:
                return True
            return False
        except:
            return False
    
    def getPassword(self, uName):
        if self.getUserExists(uName):
            self.cursor.execute("SELECT Password FROM AccountDetails WHERE Username = ?", (uName))
            return self.cursor.fetchone()[0]
        
    def getEmail(self, uName):
        if self.getUserExists(uName):
            self.cursor.execute("SELECT Email FROM AccountDetails WHERE Username = ?", (uName))
            return self.cursor.fetchone()[0]
        
    def getProfilePicture(self, uName):
        if self.getUserExists(uName):
            self.cursor.execute("SELECT ProfilePicture FROM AccountDetails WHERE Username = ?", (uName))
            return self.cursor.fetchone()[0]

    def makeUser(self, uName, pw, email):
        if not self.getUserExists(uName):
            self.cursor.execute("INSERT INTO AccountDetails(Username, Password, Email)\
                                VALUES(?,?,?)", (uName, pw, email))
            print("Account successfully created!")
        else:
            print("Account creation was not successful, this username is already taken.")

    def forgotPassword(self, uName, newpw):
        if not self.getUserExists(uName):
            self.cursor.execute("UPDATE AccountDetails\
                                SET Password = ?\
                                WHERE Username = ?", (newpw, uName))
            print("Password successfully changed.")
        else:
            print("Password was not changed.")
            
class Recipe(Table):
    def __init__(self):
        try:
            self.cursor.execute("CREATE TABLE Recipe(\
                    ID INTEGER NOT NULL UNIQUE ,\
                    Name TEXT NOT NULL,\
                    Details TEXT, \
                    IngredTag1 TEXT NOT NULL,\
                    IngredTag2 TEXT,\
                    IngredTag3 TEXT,\
                    CuisineTag TEXT NOT NULL,\
                    VegTag NUMERIC NOT NULL,\
                    PRIMARY KEY(ID));")
            print("Recipe Table is successively created.")
        except:
            print("Table was not created.")

    def addRecipe(self, rid, name, details, uploaded, IngredTag1, IngredTag2 = None, IngredTag3 = None, cuisine, veg):
        self.cursor.execute("INSERT INTO Recipe(ID, Name, Details, Uploaded, IngredTag1, IngredTag2, IngredTag3, CuisineTag, VegTag)\
                            VALUES (?,?,?,?,?,?)", (rid, name, details, uploaded, IngredTag1, IngredTag2, IngredTag3, cuisine, veg))
        print("Recipe successfully added! ")

    def doesIdExist(self, rid):
        self.cursor.execute("SELECT DISTINCT * FROM Recipe WHERE ID = ?", (rid))
        return self.cursor.fetchone()[0] == True

    def getName(self, rid):
        self.cursor.execute("SELECT Name FROM Recipe WHERE ID = ?", (rid))
        return self.cursor.fetchone()[0]
    
    def getDetails(self, rid):
        self.cursor.execute("SELECT Details FROM Recipe WHERE ID = ?", (rid))
        return self.cursor.fetchall()[0]

    def getAllIngredTag(self, rid):
        self.cursor.execute("SELECT IngredTag1, IngredTag2, IngredTag3 FROM Recipe WHERE ID = ?", (rid))
        return self.cursor.fetchall()[0]
    
    def getCuisine(self, rid):
        self.cursor.execute("SELECT Cuisine FROM Recipe WHERE ID = ?", (rid))
        return self.cursor.fetchone()[0]
    
    def isVegetarian(self, rid):
        self.cursor.execute("SELECT VegTag FROM Recipe WHERE ID = ?", (rid))
        bool = self.cursor.fetchone()[0]
        if bool == 1:
            return True
        return False

    def addIngredTag(self, rid, tag):
        result = self.getAllIngredTag(rid)
        if result[0] != None and result[1] != None and result[2] != None:
            print("Unable to add ingredient tag.")
        else:
            if result[1] == None:
                self.cursor.execute("UPDATE Recipe \
                                    SET IngredTag2 = ? \
                                    WHERE ID = ?", (tag, rid))
                
            else:
                self.cursor.execute("UPDATE Recipe \
                                    SET IngredTag3 = ? \
                                    WHERE ID = ?", (tag, rid))
            print(str(tag), "Tag successfully added!")
    
    def changeCuisineTag(self, rid, cuisine):
        self.cursor.execute("UPDATE Recipe \
                             SET CuisineTag = ? \
                             WHERE ID = ?", (cuisine, rid))
        print("Cuisine Tag has been successfully changed to", str(cuisine))

    def changeVegTag(self, rid):
        curr = self.isVegetarian(rid)
        self.cursor.execute("UPDATE Recipe \
                             SET VegTag = ? \
                             WHERE ID = ?", (not curr, rid))
        print("Vegetarian Tag has been successfully changed to", str(curr))

class PulledRecipe(Table):
    def __init__(self):
        try: 
            self.cursor.execute("CREATE TABLE PulledRecipe(\
                    QNum INTEGER NOT NULL UNIQUE AUTOINCREMENT,\
                    Name TEXT NOT NULL,\
                    Details TEXT,\
                    File BLOB, \
                    URL TEXT NOT NULL,\
                    PRIMARY KEY(QNum));")
            print("Pulled Recipe Table successfully created.")
        except:  
            print("Pulled Recipe Table was not created.")

    def getQnum(self, name):
        self.cursor.execute("SELECT QNum FROM PulledRecipe WHERE Name = ?", (name))
        return self.cursor.fetchone()

    def getName(self, qnum):
        self.cursor.execute("SELECT Name FROM PulledRecipe WHERE QNum = ?", qnum)
        return self.cursor.fetchone()
    
    def getDetails(self, qnum):
        self.cursor.execute("SELECT Details FROM PulledRecipe WHERE QNum = ?", qnum)
        return self.cursor.fetchall()
    
    def getFile(self, qnum):
        self.cursor.execute("SELECT File FROM PulledRecipe WHERE QNum = ?", qnum)
        return self.cursor.fetchall()
    
    def getURL(self, qnum):
        self.cursor.execute("SELECT URL FROM PulledRecipe WHERE QNum = ?", qnum)
        return self.cursor.fetchone()
    
    def addIntoPulled(self, name, details, file = None, urlink):
        self.cursor.execute("INSERT INTO PulledRecipe(Name, Details, File, URL)\
                            VALUES(?,?,?,?)", (name, details, file, urlink))
        print("Recipe successfully added into Pulled Recipe Table.")
        
    def viewAllPulled(self):
        self.cursor.execute("SELECT * FROM PulledRecipe\
                            ORDER BY QNum ASC")
        return self.cursor.fetchall()

    def clearTable(self):
        self.cursor.execute("DELETE FROM PulledRecipe")
        print("Pulled Recipe Table has been successfully cleared.")

    def clearSpecificQNum(self, qnum):
        self.cursor.execute("DELETE FROM PulledRecipe\
                            WHERE QNum = ?", (qnum))
        print("QNum ", qnum, "has been successfully removed from the Table.")
    
    def clearSpecificRecipe(self, name):
        qnum = self.getQnum(name)
        self.cursor.execute("DELETE FROM PulledRecipe \
                            WHERE Qnum = ?", (qnum))
        
class AccountRecipe(Table):
    def __init__(self):
        try:
            self.cursor.execute("CREATE TABLE AccountRecipe(\
                    Username TEXT NOT NULL ,\
                    RecipeID INTEGER NOT NULL UNIQUE,\
                    FOREIGN KEY(Username) REFERENCES AccountDetails(Username),\
                    FOREIGN KEY(RecipeID) REFERENCES Recipe(ID),\
                    PRIMARY KEY(Username, RecipeID));")
            print("Account Recipe Table successfully created.")
        except:
            print("Account Recipe Table was not created.")

    def getAllRecipeID(self, uname):
        self.cursor.execute("SELECT * FROM AccountRecipe WHERE Username = ?", (uname))
        return self.cursor.fetchall()

    def deleteFromAcc(self, uname, rid):
        self.cursor.execute("DELETE FROM AccountRecipe WHERE Username = ? AND RecipeID = ?", (uname, rid))
        print(rid, "has been successfully removed from ", uname + "'s saved recipes")

    def addToAcc(self, uname, rid):
        self.cursor.execute("INSERT INTO AccountRecipe(Username, RecipeID)\
                            VALUES (?,?)", (uname, rid))
        print(rid, "has been successfully added into ", uname, "'s saved recipes.")

class 

'''  self.cursor.execute("CREATE TABLE AccountDetails(\
                    Username TEXT NOT NULL ,\
                    Password TEXT NOT NULL ,\
                    ProfilePicture BLOB,\
                    Email TEXT,\
                    PRIMARY KEY(Username));")

    self.cursor.execute("CREATE TABLE Recipe(\
                    ID INTEGER NOT NULL UNIQUE,\
                    Uploaded NUMERIC NOT NULL,\
                    IngredTag1 TEXT NOT NULL,\
                    IngredTag2 TEXT,\
                    IngredTag3 TEXT,\
                    CuisineTag TEXT NOT NULL,\
                    VegTag NUMERIC NOT NULL,\
                    PRIMARY KEY(ID));")

    self.cursor.execute("CREATE TABLE AccountRecipe(\
                    Username TEXT NOT NULL ,\
                    RecipeID INTEGER NOT NULL UNIQUE,\
                    FOREIGN KEY(Username) REFERENCES AccountDetails(Username),\
                    FOREIGN KEY(RecipeID) REFERENCES Recipe(ID),\
                    PRIMARY KEY(Username, RecipeID));")

    self.cursor.execute("CREATE TABLE UploadedRecipe(\
                    ID INTEGER NOT NULL UNIQUE,\
                    Name TEXT,\
                    Details TEXT,\
                    Author TEXT NOT NULL,\
                    File BLOB, \
                    Likes INTEGER, \
                    FOREIGN KEY(ID) REFERENCES Recipe(ID),\
                    FOREIGN KEY(Author) REFERENCES AccountDetails(Username),\
                    PRIMARY KEY(ID));")

    self.cursor.execute("CREATE TABLE InternetRecipe(\
                    ID INTEGER NOT NULL UNIQUE,\
                    Name TEXT,\
                    Details TEXT,\
                    URL TEXT NOT NULL,\
                    File BLOB, \
                    FOREIGN KEY(ID) REFERENCES Recipe(ID),\
                    PRIMARY KEY(ID));")

    self.cursor.execute("CREATE TABLE PulledRecipe(\
                    QNum INTEGER NOT NULL UNIQUE,\
                    Name TEXT,\
                    Details TEXT,\
                    File BLOB, \
                    URL TEXT NOT NULL,\
                    PRIMARY KEY(QNum));") '''
