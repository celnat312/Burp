from urllib.request import urlopen
import json

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

print(ls)