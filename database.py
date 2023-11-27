from sqlite3 import * 

# Opening and accessing the database alongside initialising cursor
open('CTD.db', 'w').close()
db = connect("CTD.db")
cursor = db.cursor()


class DataBase():
    # Creating the table
    def __init__(self):
        cursor.execute("CREATE TABLE AccountDetails(\
                    Username TEXT NOT NULL ,\
                    Password TEXT NOT NULL ,\
                    ProfilePicture BLOB,\
                    Email TEXT,\
                    PRIMARY KEY(Username));")

        cursor.execute("CREATE TABLE Recipe(\
                    ID INTEGER NOT NULL UNIQUE,\
                    Uploaded NUMERIC NOT NULL,\
                    IngredTag1 TEXT NOT NULL,\
                    IngredTag2 TEXT,\
                    IngredTag3 TEXT,\
                    CuisineTag TEXT NOT NULL,\
                    VegTag NUMERIC NOT NULL,\
                    PRIMARY KEY(ID, Uploaded));")

        cursor.execute("CREATE TABLE AccountRecipe(\
                    Username TEXT NOT NULL ,\
                    RecipeID INTEGER NOT NULL UNIQUE,\
                    FOREIGN KEY(Username) REFERENCES AccountDetails(Username),\
                    FOREIGN KEY(RecipeID) REFERENCES Recipe(ID),\
                    PRIMARY KEY(Username, RecipeID));")

        cursor.execute("CREATE TABLE UploadedRecipe(\
                    ID INTEGER NOT NULL UNIQUE,\
                    Name TEXT,\
                    Details TEXT,\
                    Author TEXT NOT NULL,\
                    File BLOB, \
                    Likes INTEGER, \
                    FOREIGN KEY(ID) REFERENCES Recipe(ID),\
                    FOREIGN KEY(Author) REFERENCES AccountDetails(Username),\
                    PRIMARY KEY(ID));")

        cursor.execute("CREATE TABLE InternetRecipe(\
                    ID INTEGER NOT NULL UNIQUE,\
                    Name TEXT,\
                    Details TEXT,\
                    URL TEXT NOT NULL,\
                    File BLOB, \
                    FOREIGN KEY(ID) REFERENCES Recipe(ID),\
                    PRIMARY KEY(ID));")

        cursor.execute("CREATE TABLE PulledRecipe(\
                    QNum INTEGER NOT NULL UNIQUE,\
                    Name TEXT,\
                    Details TEXT,\
                    File BLOB, \
                    URL TEXT NOT NULL,\
                    PRIMARY KEY(QNum));")
        
    def 


# Committing the changes
db.commit()

# Closing the database
db.close()