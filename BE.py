from urllib.request import urlopen
import json
from database import AccTable, Table

#region google search api
def get_api_data():
   API_KEY = "AIzaSyDqHulV7W-F9V0Y7-he_xR59gRUZ9Qt8E0"
   SEARCH_ENGINE_ID = "c21ed2c13490b47b0"
   query = "recipe+with+only+beef+cheese+tomato+and+rice"
   page = 1
   start = (page - 1) * 10 + 1

   url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

   with urlopen(url) as response:
      data = response.read()
      # print(data)
      decoded_data = data.decode('utf-8')  # Assuming the encoding is 'utf-8'
      json_data = json.loads(decoded_data)

   items = json_data["items"]
   ls = []
   for item in items:
      title = item['title']
      link = item['link']
      image = item['pagemap']['cse_image']
      dict = { "title": title, "link": link, "image": image}
      ls.append(dict)

   return ls

#endregion


#region userlogin   #TODO after opening database always rmb to .closeConnection() at the end of the code !!!!! for celine

AccountTable = AccTable()
def addnewuser(username, pd):
   global AccountTable
   email = None   # for now
   AccountTable.makeUser(username, pd, email)
   AccountTable.commitChanges()
   return
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


newusername = "tes"
npd = "testtt2"
# addnewuser(newusername, npd)
print(userlogin(newusername, npd))
AccountTable.closeConnection()
#