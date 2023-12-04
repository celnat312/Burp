from sqlite3 import * 
import os.path

class Table():
    def __init__(self):
        # Connecting and Accessing database in the "database" folder
        curr_directory = os.path.dirname(os.path.abspath(__file__))
        db_folder = "database"
        db_path = os.path.join(curr_directory, db_folder)
        os.makedirs(db_path, exist_ok = True)
        db_file_path = os.path.join(db_path, "CTD.db")
        self.db = connect(db_file_path) # to connect
        self.cursor = self.db.cursor() # cursor

    def commitChanges(self):
        # Committing the changes
        self.db.commit()
    
    def closeConnection(self):
        # Closing the database
        self.db.close()

class AccTable(Table):
    def __init__(self):
        # Inheriting the methods and properties from parent class Table
        super().__init__()

        # Creates the table if it does not exist in the database
        self.cursor.execute("CREATE TABLE IF NOT EXISTS AccountDetails(\
                Username TEXT NOT NULL ,\
                Password TEXT NOT NULL ,\
                ProfilePicture BLOB,\
                Email TEXT,\
                PRIMARY KEY(Username));")

    def getUserExists(self, uName):
        # Checks if the username exists in the AccountDetails Table
        try:
            # Fetches the Account Details for the specified username
            self.cursor.execute("SELECT * FROM AccountDetails WHERE Username = ?", (uName,))
            data = self.cursor.fetchone()
            if data:
                return True
            return False
        except:
            return False
    
    def getPassword(self, uName):
        if self.getUserExists(uName):
            self.cursor.execute("SELECT Password FROM AccountDetails WHERE Username = ?", (uName,))
            return self.cursor.fetchone()[0]
        
    def getEmail(self, uName):
        if self.getUserExists(uName):
            self.cursor.execute("SELECT Email FROM AccountDetails WHERE Username = ?", (uName,))
            return self.cursor.fetchone()[0]
        
    def getProfilePicture(self, uName):
        if self.getUserExists(uName):
            self.cursor.execute("SELECT ProfilePicture FROM AccountDetails WHERE Username = ?", (uName,))
            return self.cursor.fetchone()[0]

    def makeUser(self, uName, pw, email):
        # Performing a validation check if the Username is taken (since Username MUST be unique.)
        if not self.getUserExists(uName):
            # Adds the information to the table to store
            self.cursor.execute("INSERT INTO AccountDetails(Username, Password, Email)\
                                VALUES(?,?,?)", (uName, pw, email))
            return True
        else:
            return False

    def forgotPassword(self, uName, newpw):
        # Changes the password of an account of a given username
        if self.getUserExists(uName):
            self.cursor.execute("UPDATE AccountDetails\
                                SET Password = ?\
                                WHERE Username = ?", (newpw, uName))
            print("Password successfully changed.")
        else:
            print("Password was not changed.")

class Recipe(Table):
    def __init__(self):
        # Inherits methods and properties from the parent class Table
        super().__init__()

        # Creates the table if it does not exist in the database
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Recipe(\
                ID INTEGER NOT NULL UNIQUE ,\
                Name TEXT NOT NULL,\
                Details TEXT, \
                Uploaded TEXT,\
                IngredTag1 TEXT NOT NULL,\
                IngredTag2 TEXT,\
                IngredTag3 TEXT,\
                CuisineTag TEXT NOT NULL,\
                VegTag NUMERIC NOT NULL,\
                File BLOB,\
                Author TEXT,\
                Likes INTEGER,\
                URL TEXT,\
                PRIMARY KEY(ID)\
                FOREIGN KEY(Author) REFERENCES AccTable(Username));")

    def addRecipe(self, rid, name, details, uploaded, IngredTag1, Cuisine, veg, author, likes, ur, IngredTag2=None, IngredTag3=None):
        # Adds a recipe into the database if the RecipeID given is not taken
        if not self.doesIdExist(rid):
            self.cursor.execute("INSERT INTO Recipe(ID, Name, Details,Uploaded, IngredTag1, IngredTag2, IngredTag3, CuisineTag, VegTag)\
                                VALUES (?,?,?,?,?,?)", (rid, name, details, uploaded, IngredTag1, IngredTag2, IngredTag3, Cuisine, veg))
        print("Recipe successfully added! ")

    def addManyRecipes(self, rids, recipes):
        # Adds a recipe into the database if the RecipeID given is not taken
        if not self.doesIdListExist(rids):
            self.cursor.executemany("INSERT INTO Recipe(ID, Name, Details, IngredTag1, IngredTag2, IngredTag3, CuisineTag, VegTag, File, url)\
                                VALUES (?,?,?,?,?,?,?,?,?,?)", recipes)
            print("Recipe successfully added! ")

    def doesIdListExist(self, rids):
        # Checks if all rid in the list exist in the database
        placeholders = ",".join(["?" for _ in range(len(rids))])
        self.cursor.execute("SELECT COUNT(*) FROM Recipe WHERE ID IN ({})".format(placeholders), tuple(rids))
        a = self.cursor.fetchone()[0]
        print(a)
        return a == len(rids)

    def doesIdExist(self, rid):
        # Checks if the RecipeID already exists in the database (i.e. if the RecipeID is already taken)
        self.cursor.execute("SELECT DISTINCT * FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchone()[0] == True

    def getName(self, rid):
        self.cursor.execute("SELECT Name FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchone()[0]

    def getNames(self, rids):
        placeholders = ', '.join(['?' for _ in rids])
        self.cursor.execute("SELECT Name FROM Recipe WHERE ID in ({})".format(placeholders), tuple(rids))
        return self.cursor.fetchall()
    
    def getDetails(self, rid):
        self.cursor.execute("SELECT Details FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchall()[0]

    def getAllIngredTag(self, rid):
        # Fetches a list of tuples of all the Ingredient Tags for the specified RecipeID
        self.cursor.execute("SELECT IngredTag1, IngredTag2, IngredTag3 FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchall()[0]
    
    def getCuisine(self, rid):
        self.cursor.execute("SELECT Cuisine FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchone()[0]
    
    def isVegetarian(self, rid):
        self.cursor.execute("SELECT VegTag FROM Recipe WHERE ID = ?", (rid,))
        bool = self.cursor.fetchone()[0]
        if bool == 1:
            return True
        return False

    def getFile(self, rid):
        self.cursor.execute("SELECT File FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchone()[0]
    
    def getURL(self, rid):
        self.cursor.execute("SELECT URL FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchone()[0]

    def getURLs(self, rids):
        placeholders = ', '.join(['?' for _ in rids])
        self.cursor.execute("SELECT URL FROM Recipe WHERE ID in ({})".format(placeholders), tuple(rids))
        return self.cursor.fetchall()

    def getIDbyUrl(self, url):
        self.cursor.execute("SELECT ID FROM Recipe WHERE URL = ?", (url,))
        return self.cursor.fetchone()[0]
    
    def getLikes(self, rid):
        self.cursor.execute("SELECT Likes FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchone()[0]
    
    def getAuthor(self, rid):
        self.cursor.execute("SELECT Author FROM Recipe WHERE ID = ?", (rid,))
        return self.cursor.fetchone()[0]
    
    def updateLikes(self, rid, newnum):
        # Updates the number of likes a specified recipe has
        self.cursor.execute("UPDATE Recipe\
                            SET Likes = ?\
                            WHERE ID = ? ", (newnum, rid))
        print("Likes have been successfully updated.")

    def updateAuthor(self, rid, author):
        # Updates the author of an uploaded recipe
        self.cursor.execute("UPDATE Recipe\
                            SET Author = ?\
                            WHERE ID = ? ", (author, rid))
        print("Author have been successfully updated.")

    def updateFiles(self, rid, file):
        self.cursor.execute("UPDATE Recipe\
                            SET File = ?\
                            WHERE ID = ? ", (file, rid))
        print("Files have been successfully updated.")

    def updateURL(self, rid, newUrl):
        # Updates the URL of an uploaded recipe
        self.cursor.execute("UPDATE Recipe\
                            SET URL = ?\
                            WHERE ID = ? ", (newUrl, rid))
        print("URL have been successfully updated.")

    def addIngredTag(self, rid, tag):
        result = self.getAllIngredTag(rid)

        # Checks if the List of Ingredient Tags is already fully populated
        if result[0] != None and result[1] != None and result[2] != None:
            print("Unable to add ingredient tag.")
        else:
            # If the second Ingredient Tag is null, add new Ingredient Tag here
            if result[1] == None:
                self.cursor.execute("UPDATE Recipe \
                                    SET IngredTag2 = ? \
                                    WHERE ID = ?", (tag, rid))
                
            # If the third Ingredient Tag is null, add new Ingredient Tag here    
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

    def clearTable(self):
        # Clears all entries stored into the PulledRecipe table
        self.cursor.execute("DELETE FROM Recipe where ID <= 220332320")
        print("Pulled Recipe Table has been successfully cleared.")

class PulledRecipe(Table):
    def __init__(self):
        # Inherits the methods and properties of the parent class Table
        super().__init__()

        # Creates the table if it does not exist in the database
        self.cursor.execute("CREATE TABLE IF NOT EXISTS PulledRecipe(\
                QNum INTEGER NOT NULL UNIQUE AUTOINCREMENT,\
                Name TEXT NOT NULL,\
                Details TEXT,\
                File BLOB, \
                URL TEXT NOT NULL,\
                PRIMARY KEY(QNum));")

    def getQnum(self, name):
        self.cursor.execute("SELECT QNum FROM PulledRecipe WHERE Name = ?", (name,))
        return self.cursor.fetchone()

    def getName(self, qnum):
        self.cursor.execute("SELECT Name FROM PulledRecipe WHERE QNum = ?", (qnum,))
        return self.cursor.fetchone()
    
    def getDetails(self, qnum):
        self.cursor.execute("SELECT Details FROM PulledRecipe WHERE QNum = ?", (qnum,))
        return self.cursor.fetchall()
    
    def getFile(self, qnum):
        self.cursor.execute("SELECT File FROM PulledRecipe WHERE QNum = ?", (qnum,))
        return self.cursor.fetchall()
    
    def getURL(self, qnum):
        self.cursor.execute("SELECT URL FROM PulledRecipe WHERE QNum = ?", (qnum,))
        return self.cursor.fetchone()
    
    def addIntoPulled(self, name, details, urlink, file = None):
        # Adds a log of data into the PulledRecipe table
        self.cursor.execute("INSERT INTO PulledRecipe(Name, Details, File, URL)\
                            VALUES(?,?,?,?)", (name, details, file, urlink))
        print("Recipe successfully added into Pulled Recipe Table.")
        
    def viewAllPulled(self):
        # Returns all the data stored into the PulledRecipe table
        self.cursor.execute("SELECT * FROM PulledRecipe\
                            ORDER BY QNum ASC")
        return self.cursor.fetchall()

    def clearTable(self):
        # Clears all entries stored into the PulledRecipe table
        self.cursor.execute("DELETE FROM PulledRecipe")
        print("Pulled Recipe Table has been successfully cleared.")

    def clearSpecificQNum(self, qnum):
        # Clears the entry of a specific recipe based on the Queue Number
        self.cursor.execute("DELETE FROM PulledRecipe\
                            WHERE QNum = ?", (qnum,))
        print("QNum ", qnum, "has been successfully removed from the Table.")
    
    def clearSpecificRecipe(self, name):
        # Clears the entry of a specific recipe based on the Recipe Name
        qnum = self.getQnum(name)
        self.cursor.execute("DELETE FROM PulledRecipe \
                            WHERE Qnum = ?", (qnum,))
        
class AccountRecipe(Table):
    def __init__(self):
        # Inherit methods and properties from the parent class Table
        super().__init__()

        # Creates the table if it does not exist in the database
        self.cursor.execute("CREATE TABLE IF NOT EXISTS AccountRecipe(\
                Username TEXT NOT NULL ,\
                RecipeID INTEGER NOT NULL UNIQUE,\
                FOREIGN KEY(Username) REFERENCES AccountDetails(Username),\
                FOREIGN KEY(RecipeID) REFERENCES Recipe(ID),\
                PRIMARY KEY(Username, RecipeID));")


    def getAllRecipeID(self, uname):
        # Fetches all the Bookmarked Recipes of a specific user
        self.cursor.execute("SELECT * FROM AccountRecipe WHERE Username = ?", (uname,))
        return self.cursor.fetchall()

    def deleteFromAcc(self, uname, rid):
        # Removes a specific Bookmarked Recipe of a specific user
        self.cursor.execute("DELETE FROM AccountRecipe WHERE Username = ? AND RecipeID = ?", (uname, rid))
        print(rid, "has been successfully removed from ", uname + "'s saved recipes")

    def addToAcc(self, uname, rid):
        # Adds a recipe into the Bookmarked Recipes of a specific user
        self.cursor.execute("INSERT INTO AccountRecipe(Username, RecipeID)\
                            VALUES (?,?)", (uname, rid))
        print(rid, "has been successfully added into ", uname, "'s saved recipes.")

