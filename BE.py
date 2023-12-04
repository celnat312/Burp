from urllib.request import urlopen
import json
from database import AccTable, AccountRecipe, Recipe
#from credential.api_key import API_KEY, SEARCH_ENGINE_ID
import tkinter as tk
import http.client



AccountTable = AccTable()
Recipe = Recipe()
AccountRecipe = AccountRecipe()

#region helper function
def cnvrt_alphabet_to_val(a):

   # Convert letter to uppercase
   letter = a.upper()

   # Calculate the value assigned to the letter by subtracting the ASCII value of 'A' and adding 1
   value = ord(letter) - ord('A') + 1

   return value

#endregion

#region google search api
def get_online_recipe(ingredient, cuisine, veg):
   global Recipe
   # Recipe.clearTable()
   query = "recipe+for+"
   node = ''
   for i in ingredient:
      query += "+" + i
      node += str(cnvrt_alphabet_to_val(i[0])) #+ str(cnvrt_alphabet_to_val(i[1]))

   # query += "+" + str(veg)
   # node += str(cnvrt_alphabet_to_val(veg[0])) #+ str(cnvrt_alphabet_to_val(v[1]))
   query = query + f'in+{cuisine[0]}+cusine'
   node += str(cnvrt_alphabet_to_val(cuisine[0][0]))


   # assign first 3 ingred tag
   if len(ingredient) < 3:
      ingredient.append(None)
   ingredTag1 = ingredient[0]
   ingredTag2 = ingredient[1]
   ingredTag3 = ingredient[2]

   # assign cuisine tag
   cuisTag = None
   if len(cuisine) != 0:
      cuisTag = cuisine[0]

   # assign veg tag if veg is not null
   vegTag = veg


   pages_to_query = 1  # Set the number of pages you want to query
   items = []

   for page in range(1, pages_to_query + 1):
      start = (page - 1) * 10 + 1
      url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

      with urlopen(url) as response:
         data = response.read()
         # print(data)
         decoded_data = data.decode('utf-8')  # Assuming the encoding is 'utf-8'
         json_data = json.loads(decoded_data)
         items.extend(json_data["items"])

   dbls = []
   FEoutput= []
   i = 1
   uidlist = []
   image_list = []
   for item in items:
      Name = item['title']
      link = item['link']
      description = item['snippet']
      id = node + str(i)
      uploaded = "None"
      # image = None
      # if 'cse_image' in item['pagemap']:
      #    image = item['pagemap']['cse_image'][0]['src']
      # elif 'megatags' in item['pagemap']:
      #    image = item['pagemap']['megatags'][0]['og:image']
      # image_list.append(image)
      stri = f"{Name}\n{description}\n{link}"
      FEoutput.append(stri)
      tupl = (int(id), Name, description, ingredTag1, ingredTag2, ingredTag3, cuisTag, vegTag, link)
      uidlist.append(id)
      i += 1
      dbls.append(tupl)

   # print(image_list)
   #
   # print(uidlist, dbls, FEoutput)
   # Recipe.addManyRecipes(uidlist, dbls)
   # Recipe.commitChanges()
   # Recipe.closeConnection()

   return FEoutput

#endregion


#region userlogin

def addnewuser(username, pd, email):
   global AccountTable
   # email = None   # for now
   result = AccountTable.makeUser(username, pd, email)
   if result == 1:
      AccountTable.commitChanges()
      print("Account successfully created")
   else:
      print("Account Creation was not successful, this username is already taken")
   return result

def userlogin(username, pd):
   global AccountTable
   a = AccountTable.getUserExists(username)
   b = AccountTable.getPassword(username)
   r = 'Login successfully'
   if a == False:
      r = "Invalid Username"
   elif b != pd:
      r = "Invalid password"

   return r



#endregion

#region bookmark function
def bookmark(username, stri):
   global AccountRecipe
   global Recipe

   items = stri.split('\n')
   url = items[2]

   rid = Recipe.getIDbyUrl(url)
   AccountRecipe.addToAcc(username, rid)
   AccountRecipe.commitChanges()

   return "added to bookmark"

def remove(username, stri):
   global AccountRecipe
   global Recipe

   items = stri.split('\n')
   url = items[2]

   rid = Recipe.getIDbyUrl(url)
   AccountRecipe.deleteFromAcc(username, rid)
   AccountRecipe.commitChanges()
   return "removed from bookmark"

def pull_bookmarked(username):
   global AccountRecipe
   global Recipe

   items = AccountRecipe.getAllRecipeID(username)
   uid = []
   for i in items:
      uid.append(i[1])

   name = Recipe.getNames(uid)
   link = Recipe.getURLs(uid)
   i = 0
   lst = []
   while i < len(name):
      str = name[i][0] + '\n' + link[i][0]
      lst.append(str)
      i += 1

   return lst


#endregion


# region Account Changes

def changePFP(uName,num):
      global AccountTable
      AccountTable.updateProfilePicture(uName, num)
      AccountTable.commitChanges()
      print("Profile Picture updated.")

def displayPFP(uName):
   global AccountTable
   img = AccountTable.getProfilePicture(uName)
   print(img)
   return img

#endregion