import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import font
from tkinter.ttk import *
from tkinter.ttk import Progressbar
import webbrowser, functools, sys, time, random

# Backend (uncomment when pushing to github)
import BE
from BE import *

'''
Uncomment areas around lines:
- store_data(self): 267
- save recipe:
- show_page2: 436
- uploads/bookmarked: 516
- sendBEPfP: 613
- login: 733
- create acc: 935
- forget pwd: 810
'''

username1 = None


# IMPORTANT: All images should be placed in the same folder/directory of the .py file
# Main colours: d0b38b, dbc4a5, c69962

# Ace's tkinter references
# https://docs.google.com/document/d/1Bw5Bo-iJwp0QTucnMkPnswHnSbBIMvtjOY5WK25_GR8/edit

class MyNotebookContainer(Canvas):
    def __init__(self, master=None):
        # Set your desired background color
        super().__init__(master, bg='#dbc4a5')  # a4b4eb (nice blue)
        style = ttk.Style()
        ttk.Style().theme_use("clam")
        # style.configure('TNotebook', tabposition='en')
        style.configure('TNotebook.Tab', width=self.winfo_screenmmwidth())
        self.notebook = MyNotebook(self)
        self.create_window((55, 60), window=self.notebook, anchor='nw', width=890, height=590)

        # Create a rounded rectangle underneath the notebook
        CanvasUtils.round_rectangle(self, 50, 21, 950, 660, radius=30, fill="#bb8544")
        CanvasUtils.round_rectangle(self, 50, 24, 950, 660, radius=30, fill="#bf904f")
        CanvasUtils.round_rectangle(self, 50, 27, 950, 660, radius=30, fill="#c29b5b")
        CanvasUtils.round_rectangle(self, 50, 30, 950, 660, radius=30, fill="#c5a666")
        CanvasUtils.round_rectangle(self, 50, 33, 950, 660, radius=30, fill="#c7b172")
        CanvasUtils.round_rectangle(self, 50, 36, 950, 660, radius=30, fill="#c69962")
        # 20, 25 is y distance from top


class MyNotebook(ttk.Notebook):
    def __init__(self, master):
        super().__init__(master, style='TNotebook')
        self.style = ttk.Style()
        self.style.configure('TNotebook', background="#c69962")

        self.style.configure('TNotebook.Tab', font=('Constantia', 12, "bold"), padding=(10, 10), borderwidth=0,
                             highlightthickness=0)
        self.style.configure("TNotebook.Tab", padding=(10, 10), highlightthickness=0)

        # Configure unselected tab color
        self.style.map("TNotebook.Tab", background=[('!selected', '#a87a42'), ('selected', '#d0b38b')])

        self.notebook1 = Notebook1(self)
        self.notebook2 = Notebook2(self)
        self.notebook3 = Notebook3(self)
        self.notebook4 = Notebook4(self)
        self.add(self.notebook1, text="Home", )
        self.add(self.notebook2, text="Create")
        self.add(self.notebook3, text="Cook/Recipe")
        self.add(self.notebook4, text="Profile")


class CanvasUtils:
    @staticmethod
    def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)


class Notebook1(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

    def create_widgets(self):
        self.style = ttk.Style()
        # Styled
        self.style.configure("StyledFrame.TFrame", background="#d0b38b")
        self.configure(style="StyledFrame.TFrame")

        # Custom - change colour back to d0b38b when fixed
        self.style.configure("Custom.TFrame", background="#dbc4a5", font=("Consolas", 12))
        self.style.configure("Bold.TLabel", background="#d0b38b", font=("Consolas", 14, "bold"))
        self.style.configure("Custom.TLabel", background="#d0b38b", font=("Consolas", 12))
        self.style.configure("Logo.TLabel", borderwidth=1, relief="solid", bordercolor="#d0b38b")

        # Logo
        self.Logoimg = PhotoImage(file="logo.png")
        ttk.Label(self, image=self.Logoimg, style="Logo.TLabel").grid(column=0, row=0, padx=5, pady=5, sticky="nw")

        # Header
        Recommended = ttk.Label(self, text="Recommended!", style="Bold.TLabel")
        Recommended.grid(column=0, row=1, sticky="nw", padx=10, pady=10)

        # Image (left)
        self.rec_imgpath = PhotoImage(file="pancake.ppm")
        ttk.Label(self, image=self.rec_imgpath).grid(column=0, row=2, rowspan=2, padx=10, pady=10, sticky="sw")

        # Header (right)
        bp_text = "Banana Vegan Pancakes\n"
        bold_font = ("Consolas", 12, "bold")
        bp = ttk.Label(self, text=bp_text, style="Custom.TLabel", font=bold_font)
        bp.grid(column=1, row=2, sticky="nse", padx=10, pady=5)

        des_text = "<Ingredients>\n- 1 large banana\n- 120g flour\n- 2 tsp baking powder\n- 1/4 tsp salt\n- 2 tbsp sugar\n- 10ml vanilla extract\n- 100ml water"

        # Description (right)
        des = ttk.Label(self, text=des_text, style="Custom.TLabel", wraplength=200)

        # Combine the two texts with only the header bolded
        bp.configure(text=f"{bp_text}\n{des_text}")

    def open_web(self, url):
        new = 1
        webbrowser.open(url, new=new)


class Notebook2(ttk.Frame):  # Create
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Style
        self.style = ttk.Style()
        self.style.configure("StyledFrame.TFrame", background="#c69962")
        self.style.configure("TCheckbutton", background="#d0b38b", font=("Consolas", 11))
        self.style.configure("Custom.TButton", background="#c69962", font=('Constantia', 12))

        # Page 1
        page1 = ttk.Frame(self, style="StyledFrame.TFrame")
        page1.pack(side="top", fill="both", expand=True)

        # Frame
        page1.columnconfigure(0, weight=1)  # padding
        page1.columnconfigure(1, weight=2)  # column 0
        page1.columnconfigure(2, weight=2)  # column 1
        page1.columnconfigure(3, weight=2)  # column 2
        page1.columnconfigure(4, weight=1)  # padding

        page1.rowconfigure(0, weight=4)  # Padding
        page1.rowconfigure(1, weight=3)  # Name
        page1.rowconfigure(2, weight=3)  # URL
        page1.rowconfigure(3, weight=4)  # Spacer
        page1.rowconfigure(4, weight=2)  # Ingredients header
        page1.rowconfigure(5, weight=2)  # 7 rows
        page1.rowconfigure(6, weight=2)
        page1.rowconfigure(7, weight=2)
        page1.rowconfigure(8, weight=2)
        page1.rowconfigure(9, weight=2)
        page1.rowconfigure(10, weight=2)
        page1.rowconfigure(11, weight=2)
        page1.rowconfigure(12, weight=4)  # Spacer
        page1.rowconfigure(13, weight=2)  # Cuisine header
        page1.rowconfigure(14, weight=2)  # 4 rows
        page1.rowconfigure(15, weight=2)
        page1.rowconfigure(16, weight=2)
        page1.rowconfigure(17, weight=2)
        page1.rowconfigure(18, weight=4)  # Spacer
        page1.rowconfigure(19, weight=3)  # Are you vegetarian?
        page1.rowconfigure(20, weight=2)
        page1.rowconfigure(21, weight=1)  # Padding

        # Padding
        ttk.Frame(page1).grid(row=0, column=0, columnspan=5, pady=7)

        # Name
        ttk.Label(page1, text='Name of dish: ', background="#d0b38b").grid(column=1, row=1, sticky="e")
        name = tk.Entry(page1, width=30, bg='#c69962')
        name.focus()
        name.grid(column=2, columnspan=2, row=1, sticky="w")
        self.name = name

        # URL
        ttk.Label(page1, text='URL: ', background="#d0b38b").grid(column=1, row=2, sticky="e")
        urlname = tk.Entry(page1, width=30, bg='#c69962')
        urlname.focus()
        urlname.grid(column=2, columnspan=2, row=2, sticky="w")
        self.urlname = urlname

        # Space
        ttk.Frame(page1).grid(row=3, column=1, columnspan=5, pady=7)

        # Ingredients Section
        ttk.Label(page1, text="Ingredients:", background="#d0b38b", font=("Consolas", 12)).grid(row=4, column=1, padx=15,
                                                                                               pady=5, columnspan=3,
                                                                                               sticky="w")
        ingredients_list = ["Rice", "Noodles", "Pasta", "Potato", "Chicken", "Beef", "Pork", "Fish", "Egg", "Milk",
                            "Cheese", "Yoghurt", "Carrot", "Tomato", "Lettuce", "Brocoli", "Bok Choy", "Soya Sauce",
                            "Chili", "Ketchup", "Fish Sauce"]
        self.ingredients_var = self.create_checkbox_columns(page1, ingredients_list, 3, 1, 5)
        self.ingredients_list = ingredients_list

        # Space
        ttk.Frame(page1).grid(row=12, column=1, columnspan=5, pady=7)

        # Cuisine Section
        ttk.Label(page1, text="Cuisine:", background="#d0b38b", font=("Consolas", 12)).grid(row=13, column=1, padx=15,
                                                                                           pady=5, columnspan=3,
                                                                                           sticky="w")
        cuisine_list = ["Indonesian", "Singaporean", "Chinese", "Malay", "Indian", "Western", "Korean", "Japanese"]
        self.cuisine_var = self.create_checkbox_columns(page1, cuisine_list, 2, 1, 14)
        self.cuisine_list = cuisine_list

        # Space
        ttk.Frame(page1).grid(row=18, column=1, columnspan=5, pady=10)

        # Vegetarian Section
        ttk.Label(page1, text="Are you vegetarian?", background="#d0b38b", font=("Consolas", 12)).grid(row=19, column=1,
                                                                                                       padx=15, pady=5,
                                                                                                       columnspan=3,
                                                                                                       sticky="w")
        self.var = tk.BooleanVar(value=False)
        R1 = tk.Radiobutton(page1, text="Yes", variable=self.var, value=True, bg="#d0b38b", font=('Consolas', 12))
        R1.grid(row=20, column=1)
        R2 = tk.Radiobutton(page1, text="No", variable=self.var, value=False, bg="#d0b38b", font=('Consolas', 12))
        R2.grid(row=20, column=2)

        # Button to send data
        next_button = ttk.Button(page1, text="Create", command=self.send_data, style="Custom.TButton")
        next_button.grid(row=20, column=3, sticky="se")

        # Padding
        ttk.Frame(page1).grid(row=21, column=0, columnspan=5, pady=7)

    def create_checkbox_columns(self, parent, items, num_columns, start_column, start_row):
        vars_list = []
        for i, item in enumerate(items):
            var = tk.BooleanVar(value=False)
            ttk.Checkbutton(parent, text=item, variable=var, style="TCheckbutton").grid(
                row=start_row + i // num_columns, column=start_column + i % num_columns, sticky="w", pady=2)
            vars_list.append(var)
        return vars_list

    def send_data(self):  # Notebook2: create
        # global usernme
        dishName = self.name.get()
        urlLink = self.urlname.get()
        veg_bool = self.var.get()
        selected_ingredients = [item for item, var in zip(self.ingredients_list, self.ingredients_var) if var.get()]
        selected_cuisine = [item for item, var in zip(self.cuisine_list, self.cuisine_var) if var.get()]
        # print(dishName, urlLink, veg_bool, selected_cuisine, selected_ingredients)
        return dishName, urlLink, veg_bool, selected_cuisine, selected_ingredients

    def store_data(self):
        dishName, urlLink, veg_bool, selected_cuisine, selected_ingredients = self.send_data()
        pass
        '''
        try:
            BE.upload(title,it1,it2,it3,cuisine,vegtag,ur)
        except:
            print('Recipe not uploaded')
        '''


# ACELINE: 'back' function for page2 to page1

class Notebook3(ttk.Frame):  # Cook/Recipe
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Style
        self.style = ttk.Style()
        self.style.configure("StyledFrame.TFrame", background="#c69962")
        self.style.configure("TCheckbutton", font=("Consolas", 12))
        self.style.configure("Custom.TButton", background="#c69962", font=('Constantia', 12))

        # Page 1
        page1 = ttk.Frame(self)
        page1.pack(side="top", fill="both", expand=True)
        self.page1 = page1
        self.page1.configure(style="StyledFrame.TFrame")

        # Frame
        page1.columnconfigure(0, weight=1)  # padding
        page1.columnconfigure(1, weight=2)  # column 0
        page1.columnconfigure(2, weight=2)  # column 1
        page1.columnconfigure(3, weight=2)  # column 2
        page1.columnconfigure(4, weight=1)  # padding

        page1.rowconfigure(0, weight=10)  # Padding
        page1.rowconfigure(1, weight=3)  # Ingredients header
        page1.rowconfigure(2, weight=2)  # 7 rows
        page1.rowconfigure(3, weight=2)
        page1.rowconfigure(4, weight=2)
        page1.rowconfigure(5, weight=2)
        page1.rowconfigure(6, weight=2)
        page1.rowconfigure(7, weight=2)
        page1.rowconfigure(8, weight=2)
        page1.rowconfigure(9, weight=4)  # Spacer
        page1.rowconfigure(10, weight=3)  # Cuisine header
        page1.rowconfigure(11, weight=2)  # 4 rows
        page1.rowconfigure(12, weight=2)
        page1.rowconfigure(13, weight=2)
        page1.rowconfigure(14, weight=2)
        page1.rowconfigure(15, weight=4)  # Spacer
        page1.rowconfigure(16, weight=3)  # Are you vegetarian?
        page1.rowconfigure(17, weight=2)
        page1.rowconfigure(18, weight=4)  # Padding

        # Padding
        ttk.Frame(page1).grid(row=0, column=0, columnspan=5, pady=7)

        # Ingredients Section
        ttk.Label(page1, text="Ingredients:", background="#d0b38b", font=("Consolas", 12)).grid(row=1, column=1, padx=15,
                                                                                               pady=5, columnspan=3,
                                                                                               sticky="w")
        ingredients_list = ["Rice", "Noodles", "Pasta", "Potato", "Chicken", "Beef", "Pork", "Fish", "Egg", "Milk",
                            "Cheese", "Yoghurt", "Carrot", "Tomato", "Lettuce", "Brocoli", "Bok Choy", "Soya Sauce",
                            "Chili", "Ketchup", "Fish Sauce"]
        self.ingredients_var = self.create_checkbox_columns(page1, ingredients_list, 3, 1, 2)
        self.ingredients_list = ingredients_list

        # Space
        ttk.Frame(page1).grid(row=9, column=1, columnspan=5, pady=10)

        # Cuisine Section
        ttk.Label(page1, text="Cuisine:", background="#d0b38b", font=("Consolas", 12)).grid(row=10, column=1, padx=15,
                                                                                           pady=5, columnspan=3,
                                                                                           sticky="w")
        cuisine_list = ["Indonesian", "Singaporean", "Chinese", "Malay", "Indian", "Western", "Korean", "Japanese"]
        self.cuisine_var = self.create_checkbox_columns(page1, cuisine_list, 2, 1, 11)
        self.cuisine_list = cuisine_list

        # Space
        ttk.Frame(page1).grid(row=15, column=1, columnspan=5, pady=10)

        # Vegetarian Section
        ttk.Label(page1, text="Are you vegetarian?", background="#d0b38b", font=("Consolas", 12)).grid(row=16, column=1,
                                                                                                       padx=15, pady=5,
                                                                                                       columnspan=3,
                                                                                                       sticky="w")
        self.var = tk.BooleanVar(value=False)

        fs = ("Consolas", 12)
        bgc = "#d0b38b"

        R1 = tk.Radiobutton(page1, text="Yes", variable=self.var, value=True, bg=bgc, font=fs, highlightbackground=bgc,
                            highlightcolor=bgc, selectcolor=bgc)
        R1.grid(row=17, column=1)
        R2 = tk.Radiobutton(page1, text="No", variable=self.var, value=False, bg=bgc, font=fs, highlightbackground=bgc,
                            highlightcolor=bgc, selectcolor=bgc)
        R2.grid(row=17, column=2)

        # Button to Navigate to Page 2
        next_button = ttk.Button(page1, text="Generate Recipes", command=self.btn, style="Custom.TButton")
        next_button.grid(row=17, column=3, sticky="se")

        # Padding
        ttk.Frame(page1).grid(row=18, column=0, columnspan=5, pady=7)

        # Page 2 (Hidden initially)
        self.page2 = ttk.Frame(self)
        self.page2.pack(side="top", fill="both", expand=True)
        self.page2.grid_remove()

        # Results Section in Page 2
        result_frame = ttk.Frame(self.page2, padding=(10, 10, 10, 10))
        result_frame.pack(side="top", fill="both", expand=True)

    def create_checkbox_columns(self, parent, items, num_columns, start_column, start_row):
        vars_list = []
        for i, item in enumerate(items):
            var = tk.BooleanVar(value=False)
            ttk.Checkbutton(parent, text=item, variable=var, style="TCheckbutton").grid(
                row=start_row + i // num_columns, column=start_column + i % num_columns, sticky="w", pady=5)
            vars_list.append(var)
        return vars_list

    def compile_data(self):
        selected_ingredients = [item for item, var in zip(self.ingredients_list, self.ingredients_var) if var.get()]
        selected_cuisine = [item for item, var in zip(self.cuisine_list, self.cuisine_var) if var.get()]
        veg_bool = self.var.get()

        # Do something with the compiled data, for example, print it
        print("Selected Ingredients:", selected_ingredients)
        print("Selected Cuisine:", selected_cuisine)
        print("Vegetarian?", veg_bool)

        return selected_ingredients, selected_cuisine, veg_bool

    def btn(self):  # Notebook3: Cook/Recipe
        selected_ingredients, selected_cuisine, veg_bool = self.compile_data()
        self.show_page2(selected_ingredients, selected_cuisine, veg_bool)

    # Hide Page 1 and Show Page 2
    def show_page2(self, selected_ingredients, selected_cuisine, veg_bool):
        global username1

        # Create a custom style with the desired background color
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#d0b38b", font=("Consolas", 12))
        style.configure("Bold.TLabel", background="#d0b38b", font=("Constantia", 12, "bold", "underline"))

        self.page1.pack_forget()
        self.page2.pack(side="top", fill="both", expand=True)

        # Backend
        text = BE.get_online_recipe(selected_ingredients, selected_cuisine, veg_bool)

        def open_recipe_link(url):
            # Replace with the actual URL based on the selected recipe - link comes from BE
            webbrowser.open(url, new=1)

        '''
        for i in text:
            link = (i.split('\n'))[2]
            print(link)
            ttk.Button(self.page2, text=i, command=lambda link=link: open_recipe_link(link)).pack()
        '''

        # text = [
        #     'Singapore Noodles (星洲炒米粉, Singapore Mei Fun)\nNov 18, 2022 ... Easy Singapore noodles recipe featuring rice vermicelli noodles tossed in a curry sauce with shrimp, BBQ pork, crispy onions and peppers.\nhttps://omnivorescookbook.com/singapore-noodles/',
        #     'Chow Mein | RecipeTin Eats\nOct 26, 2019 ... This real Chicken Chow Mein recipe really is restaurant quality. It ... Pad Thai, Pad See Ew (Thai Stir Fried Noodles), Singapore Noodles,\xa0...\nhttps://www.recipetineats.com/chicken-chow-mein/',
        #     "Singapore Noodles (星洲炒米粉) | Made With Lau\nA recipe by Daddy Lau. My dad's been cooking Chinese food for over 50 years - as a kid fending for himself in Guangzhou, as the head chef\xa0...\nhttps://www.madewithlau.com/recipes/singapore-noodles",
        #     "Chinese Crispy Noodles (Chow Mein) | RecipeTin Eats\nSep 2, 2019 ... Vegetable options for topping – there's really no rules here. Just use around 4 to 5 cups of any vegetables you want. Ingredients in Chinese\xa0...\nhttps://www.recipetineats.com/crispy-noodles-with-chicken/",
        #     'Singapore-style Curry Chicken Noodles – Monsoon Table\nFeb 17, 2019 ... I used low-sodium Swanson stock which is available at any Asian supermarket and is more suited for Chinese food. Plunging the cooked chicken in\xa0...\nhttps://monsoontable.wordpress.com/2019/02/17/singapore-style-curry-chicken-noodles/',
        #     'Singapore Rice Noodles - EverydayMaven™\nAug 2, 2019 ... This version is gluten-free and tastes like it came from a restaurant! Course: Mains. Cuisine: Asian. Keyword: copycat chinese recipes,\xa0...\nhttps://www.everydaymaven.com/singapore-rice-noodles-with-chicken/',
        #     'Singapore Mei Fun (Singapore Rice Noodles, 星洲米粉) - Red ...\nOct 17, 2020 ... Have a look at these recipes: Hearty and flavourful, Zha Jiang Noodles is a signature dish of Beijing cuisine. One of the most loved noodle\xa0...\nhttps://redhousespice.com/singapore-mei-fun/',
        #     'Singapore Noodles Recipe | Feasting At Home\nDec 28, 2018 ... Ingredients · 8–10 ounces chicken or tofu cut into 3/4 inch cubes ( or whole raw shrimp) · 1/4 teaspoon salt · 1–2 tablespoons wok oil – a high\xa0...\nhttps://www.feastingathome.com/singapore-noodles/',
        #     'Singapore Noodles\nthat chicken rice is all about the rice and the chicken, but this sauce is what ties everything together. Third, the chicken in these recipes never ever had\xa0...\nhttps://www.facebook.com/sgpnoodles/',
        #     "Genio Ng (@geniuseatss) • Instagram photos and videos\nBased in Sydney Flipping crepes at @kurepucrepes : genio@gushcloudtalent.com. geniuseatss.com + 1. Seoul's profile picture. Seoul. Singapore's\xa0...\nhttps://www.instagram.com/geniuseatss/?hl=en"]

        for i in text:
            username = username1  # todo change to username1 afterwards
            title = (i.split('\n'))[0]
            discription = (i.split('\n'))[1]
            link = (i.split('\n'))[2]

            frame = ttk.Frame(self.page2, style="Custom.TFrame")
            frame.pack(fill="both", expand=True)

            # Spacer
            ttk.Frame(frame).grid(row=0, column=0, columnspan=2, pady=5)

            title_label = ttk.Label(frame, text=title, style="Bold.TLabel", cursor="hand2", foreground="blue")
            title_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=(10, 0))
            title_label.bind("<Button-1>", lambda event, link=link: open_recipe_link(link))

            descrip_label = ttk.Label(frame, text=discription, wraplength=800, background="#d0b38b")
            descrip_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=(10, 0))

            button = ttk.Button(frame, text="bookmark", command=lambda u=username, r=i: BE.bookmark(u, r))
            button.grid(row=2, column=1, sticky="e", padx=(800, 0))


class Notebook4(ttk.Frame):
    def __init__(self, master=None, bottom_frame=None, rectangle_frame=None):
        super().__init__(master)
        self.bottom_frame = bottom_frame
        self.rectangle_frame = rectangle_frame
        self.create_widgets()

    def create_widgets(self):
        username = username1
        # Style
        self.style = ttk.Style()
        self.style.configure("Styled.TFrame", background="#d0b38b")
        self.configure(style="Styled.TFrame")
        self.style.configure("StyledFrame.TFrame", background="#c5a16f")
        self.style.configure("TLabel", background="#d0b38b", font=("Consolas", 12))
        self.style.configure("inner.TLabel", background="#dbc4a5", font=("Consolas", 12))

        # Top half
        top_frame = ttk.Frame(self, style="Styled.TFrame")
        top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Profile Image
        profile_image = tk.Canvas(top_frame, width=100, height=100, bg="gray")
        profile_image.create_oval(10, 10, 90, 90, fill="#a4b4eb")  # Placeholder circle
        profile_image.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="e")

        # Account Details
        account_details = ttk.Label(top_frame, text="Lorem Ipsum\nProfile Details\nMore Details", style="TLabel")
        account_details.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # New pfp btn
        details = tk.Button(top_frame, text="Edit Profile Picture", command=lambda: self.openMoreDetails(root))
        details.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Bottom half
        self.bottom_frame = ttk.Frame(self, style="StyledFrame.TFrame")
        self.bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Rectangle with Tabs
        self.rectangle_frame = ttk.Frame(self.bottom_frame, relief="solid", borderwidth=1, style="StyledFrame.TFrame")
        self.rectangle_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Tabs in the Rectangle
        # inner_tab_style = ttk.Style(self.tab_control)
        # inner_tab_style.configure('inner_tab.TNotebook', background="#d0b38b")
        tab_control = ttk.Notebook(self.rectangle_frame, style='inner_tab.TNotebook')
        tab_control.configure(style='inner_tab.TNotebook')

        # Uploads Tab
        uploads_tab = ttk.Frame(tab_control)
        ttk.Label(uploads_tab, text="Content of Uploads Tab", style="inner.TLabel").pack(pady=10)
        tab_control.add(uploads_tab, text='Uploads')

        def open_recipe_link(url):
            # Replace with the actual URL based on the selected recipe - link comes from BE
            webbrowser.open(url, new=1)

            # Bookmarked Tab

        bookmarked_tab = ttk.Frame(tab_control)
        content_bookmarked = BE.pull_bookmarked(username)

        # myscrollbar = Scrollbar(bookmarked_tab, orient="vertical")
        # myscrollbar.pack(side="right", fill="y")

        for i in content_bookmarked:
            title = (i.split('\n'))[0]
            link = (i.split('\n'))[1]

            frame = tk.Frame(bookmarked_tab, bg="#c5a16f")
            frame.pack(fill="both", expand=True)

            # Spacer
            ttk.Frame(frame).grid(row=0, column=0, columnspan=2, pady=5)

            title_label = tk.Label(frame, text=title, bg="#c5a16f", cursor="hand2", foreground="blue")
            title_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=(10, 0))
            title_label.bind("<Button-1>", lambda event, link=link: open_recipe_link(link))

        # print(content_bookmarked)
        # ttk.Label(bookmarked_tab, text=content_bookmarked, style="TLabel").pack(pady=10)
        tab_control.add(bookmarked_tab, text='Bookmarked')

        # Apply a specific style for the inner notebook
        inner_tab_style = ttk.Style()
        inner_tab_style.configure('inner_tab.TNotebook', background="#d0b38b")
        inner_tab_style.configure('inner_tab.TNotebook.Tab', width=self.rectangle_frame.winfo_screenwidth(),
                                  relief='flat', background="#d0b38b", font=("Consolas", 12))
        inner_tab_style.map('inner_tab.TNotebook.Tab', background=[('!selected', '#a87a42'), ('selected', '#c5a16f')])

        # Pack the Notebook (Tabs)
        tab_control.pack(expand=1, fill="both")

        # Configure row and column weights for proper resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.rectangle_frame.grid_rowconfigure(0, weight=1)
        self.rectangle_frame.grid_columnconfigure(0, weight=1)

    def openMoreDetails(self, root):
        # Create a new Toplevel window
        more_details_window = tk.Toplevel(root)

        # Adjust size
        more_details_window.geometry("750x525")
        # set minimum window size value
        more_details_window.minsize(750, 525)
        # set maximum window size value
        more_details_window.maxsize(750, 525)

        # Title
        more_details_window.title("Select a new Profile Picture")

        # Celine's content code
        l1 = tk.Label(more_details_window, text='Choose a new Profile Picture :DD', width=30)
        l1.grid(row=1, column=1)

        pfpimg1 = PhotoImage(file="profilePicture/1.png")
        b1 = tk.Button(more_details_window, image=pfpimg1, command=lambda: self.sendBEPfP(1, more_details_window))
        b1.image = pfpimg1
        b1.grid(row=2, column=1)

        pfpimg2 = PhotoImage(file="profilePicture/2.png")
        b2 = tk.Button(more_details_window, image=pfpimg2, command=lambda: self.sendBEPfP(2, more_details_window))
        b2.image = pfpimg2
        b2.grid(row=2, column=2)

        pfpimg3 = PhotoImage(file="profilePicture/3.png")
        b3 = tk.Button(more_details_window, image=pfpimg3, command=lambda: self.sendBEPfP(3, more_details_window))
        b3.image = pfpimg3
        b3.grid(row=2, column=3)

        pfpimg4 = PhotoImage(file="profilePicture/4.png")
        b4 = tk.Button(more_details_window, image=pfpimg4, command=lambda: self.sendBEPfP(4, more_details_window))
        b4.image = pfpimg4
        b4.grid(row=3, column=1)

        pfpimg5 = PhotoImage(file="profilePicture/5.png")
        b5 = tk.Button(more_details_window, image=pfpimg5, command=lambda: self.sendBEPfP(5, more_details_window))
        b5.image = pfpimg5
        b5.grid(row=3, column=2)

        pfpimg6 = PhotoImage(file="profilePicture/6.png")
        b6 = tk.Button(more_details_window, image=pfpimg6, command=lambda: self.sendBEPfP(6, more_details_window))
        b6.image = pfpimg6
        b6.grid(row=3, column=3)

    def sendBEPfP(self, num, window):
        global username1
        print(num)
        BE.changePFP(username1, num)
        window.destroy()


# General Layout + Login Page
class MYGUI:
    def __init__(self, root, recLogin=None):
        self.initLoadingPage(root)
        self.recLogin = recLogin

    def initLoadingPage(self, root):

        progress_var = IntVar()

        ttk.Style().configure("TLabel", background="#dbc4a5", foreground="#000000", font=("Consolas", 15, "bold"))
        ttk.Style().configure("QLabel", background="#dbc4a5", foreground="#000000", font=("Consolas", 10, "bold"))

        root.geometry("1000x700")  # window size
        # set minimum window size value
        root.minsize(1000, 700)
        # set maximum window size value
        root.maxsize(1000, 700)

        root.configure(bg="#dbc4a5")  # window settings
        # Complimentary color: #96BAEA

        # Title
        root.title("BURP")

        dots = [ttk.Label(text='.', style="TLabel") for _ in range(3)]  # dot settings

        def update_loading_dots(count=0):
            if root.winfo_exists():
                if count < 3:
                    dots[count].place(x=515 + count * 10, y=470)
                    # used place instead of destroy bc destroy destroyed my code, my hope and my dreams
                    root.after(1000, update_loading_dots, count + 1)
                elif count == 3:
                    for dot in dots:
                        dot.place_forget()  # Hide the dots
                    root.after(1000, move_loading_dots)

        def move_loading_dots():  # loops dot movement
            update_loading_dots()

        loading_title = ttk.Label(text='loading', style="TLabel")  # loading text format
        loading_title.place(x=440, y=469)  # 'loading' text position

        progress = ttk.Progressbar(root, orient=HORIZONTAL, mode='determinate', length=280,
                                   variable=progress_var)  # progressbar shape
        progress.place(x=360, y=420)  # progressbar position

        images = [PhotoImage(file="25% (1).png"), PhotoImage(file="50% (1).png"), PhotoImage(file="75% (1).png"),
                  PhotoImage(file="100% (1).png"), ]
        # list of images for each part of progress bar

        i = [0]  # using a list to hold the value of i
        load_completed = False

        canvas = Canvas(root, width=200, height=200, bg="#DBC4A5", borderwidth=0, highlightthickness=0)
        # last 2 elements eliminated ugly white border
        canvas.place(x=400, y=150)  # position canvas on window
        image_item = canvas.create_image(0, 0, image=images[0], anchor="nw")

        def load():
            nonlocal load_completed
            progress.after(1500, load)
            progress['value'] = 25 * i[0]
            i[0] += 1
            if i[0] <= 4:
                if progress['value'] == 0:
                    canvas.itemconfig(image_item, image=images[0])  # change pic
                elif progress['value'] == 25:
                    canvas.itemconfig(image_item, image=images[1])
                elif progress['value'] == 50:
                    canvas.itemconfig(image_item, image=images[2])
                elif progress['value'] == 75:
                    canvas.itemconfig(image_item, image=images[3])
            if i[0] > 4:
                load_completed = True
                progress.stop()
                self.openLoginPage(root)

        load()
        move_loading_dots()  # Call the function to show the dots

        basequotelist = ["Bread puns happen when you yeast expect them",
                         "Tough cookies don't crumble",
                         "This might sound cheesy... but I think you're really grate",
                         "Have an egg-cellent day",
                         "You don't need a silver fork to eat good food",
                         "You are one in a melon",
                         "And you became like the coffee, in the deliciousness, and the biterness and the addiction",
                         "You're the apple of my eye",
                         "We make a nice pear",
                         "Donut kill my vibe",
                         "WTF wheres the food"]

        quote = Label(text="", style="quote.TLabel", wraplength=400)  # loading text format
        quote.place(x=505, y=644, anchor="center")  # quote position

        # function to pick a random quote from the list above and insert it into the label

        def randomquote():
            if root.winfo_exists():
                quotelist = basequotelist.copy()  # creates copy of list
                random.shuffle(quotelist)
                new_text = quotelist.pop(0)  # picks first quote from list
                quote.config(text=new_text)  # updates text in quote label
                quotelist.append(new_text)  # put used quote at back of list
                root.after(3000, randomquote)  # scheule it to change after 3s

        if root.winfo_exists():
            randomquote()

    def _from_rgb(self, rgb):
        # translates an rgb tuple of int to a tkinter friendly color code
        return "#%02x%02x%02x" % rgb

    def openLoginPage(self, root):
        # Create a custom style with the desired background color
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#dbc4a5", font=("Consolas", 12))

        # Clear existing widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Adjust size
        root.geometry("1000x700")
        # set minimum window size value
        root.minsize(1000, 700)
        # set maximum window size value
        root.maxsize(1000, 700)

        # Title
        root.title("BURP Login Page")

        # recLogin
        recLogin = ttk.Frame(root, style="Custom.TFrame", relief="flat", borderwidth=0)
        recLogin.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Configure rows and columns to center widgets
        recLogin.columnconfigure(0, weight=1)
        recLogin.columnconfigure(1, weight=1)

        # Username label and text entry box
        usernameLabel = Label(recLogin, text="Username: ", font=("Consolas", 12)).grid(row=0, column=0, sticky="e")
        username = StringVar()
        usernameEntry = tk.Entry(recLogin, textvariable=username, bg='#c69962').grid(row=0, column=1, sticky="w")

        # Password label and password entry box
        passwordLabel = Label(recLogin, text="Password: ", font=("Consolas", 12)).grid(row=1, column=0, sticky="e")
        password = StringVar()
        passwordEntry = tk.Entry(recLogin, textvariable=password, bg='#c69962', show='*').grid(row=1, column=1,
                                                                                               sticky="w")

        # Space
        ttk.Frame(recLogin).grid(row=2, column=0, columnspan=2, pady=0)

        validateLogin = functools.partial(self.validateLogin, root, username, password)

        # Login Btn
        Btn = tk.Button(recLogin, text="Login", font=("Constantia", 10), command=validateLogin).grid(row=3, column=0,
                                                                                                     columnspan=2,
                                                                                                     sticky="n",
                                                                                                     ipady=5, pady=0)

        # Space
        ttk.Frame(recLogin).grid(row=4, column=0, columnspan=2, pady=0)

        # Create Acc Btn
        Btn2 = tk.Button(recLogin, text="Create Account :D", font=("Constantia", 10),
                         command=lambda: self.CreateAccount(root)).grid(row=5, column=0, columnspan=2, sticky="n",
                                                                        ipady=5, pady=0)

        # Space
        ttk.Frame(recLogin).grid(row=6, column=0, columnspan=2, pady=0)

        # Forget Pwd Btn
        Btn2 = tk.Button(recLogin, text="Forget Password :<", font=("Constantia", 10),
                         command=lambda: self.jokes_on_you(root)).grid(row=7, column=0, columnspan=2, sticky="n",
                                                                       ipady=5, pady=0)

        for widget in recLogin.winfo_children():
            widget.grid(padx=5, pady=5)

    def validateLogin(self, root, username, password):
        global username1
        print("username entered :", username.get())
        print("password entered :", password.get())

        # Backend
        r = BE.userlogin(username.get(), password.get())

        # if username.get() == "username" and password.get() == "password":
        #     username1 = username.get()
        #     self.openMainNotebooks(root)
        # else:
        #     messagebox.showerror(title="Error", message="Invalid login.")

        # Backend
        if r == 'Login successfully':
            self.openMainNotebooks(root)
        else:
            messagebox.showerror(title="Error", message=r)

    def CreateAccount(self, root):
        # Clear existing widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Adjust size
        root.geometry("1000x700")
        # set minimum window size value
        root.minsize(1000, 700)
        # set maximum window size value
        root.maxsize(1000, 700)

        # Title
        root.title("BURP Create Account")

        recCreateAcc = ttk.Frame(root, style="Custom.TFrame", relief="flat", borderwidth=0)
        recCreateAcc.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Configure rows and columns to center widgets
        recCreateAcc.columnconfigure(0, weight=1)
        recCreateAcc.columnconfigure(1, weight=1)
        recCreateAcc.columnconfigure(2, weight=1)

        # Username label and text entry box
        usernameLabel = Label(recCreateAcc, text="Username: ", font=("Constantia", 12)).grid(row=0, column=0,
                                                                                             sticky="e")
        username = StringVar()
        usernameEntry = tk.Entry(recCreateAcc, textvariable=username, bg='#c69962').grid(row=0, column=1, sticky="w")

        # Password label and password entry box
        passwordLabel = Label(recCreateAcc, text="Password: ", font=("Constantia", 12)).grid(row=1, column=0,
                                                                                             sticky="e")
        password = StringVar()
        passwordEntry = tk.Entry(recCreateAcc, textvariable=password, bg='#c69962').grid(row=1, column=1, sticky="w")

        # Email label and email entry box
        emailLabel = Label(recCreateAcc, text="Email (opt): ", font=("Constantia", 12)).grid(row=2, column=0,
                                                                                             sticky="e")
        email = StringVar()
        emailLabel = tk.Entry(recCreateAcc, textvariable=email, bg='#c69962').grid(row=2, column=1, sticky="w")

        # Create Account: Add account to database? and then return to login page
        CBtn = tk.Button(recCreateAcc, text="Create", font=("Constantia", 10), command=lambda: self.openLoginPage(root))
        CBtn.grid(row=3, column=0, columnspan=2, sticky="n", ipady=5, pady=0)

        for widget in recCreateAcc.winfo_children():
            widget.grid(padx=5, pady=5)

    # Backend
    '''
    def create_and_return(self, root, username, password, email):
        print({"username": username.get(), "pw": password.get(), "email": email.get()})
        BE.addnewuser(username.get(), password.get(), email.get())
        self.openLoginPage(root)
    '''

    def jokes_on_you(self, root):
        # Clear existing widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Adjust size
        root.geometry("1000x700")
        # set minimum window size value
        root.minsize(1000, 700)
        # set maximum window size value
        root.maxsize(1000, 700)

        # Title
        root.title("lololololololololololol")

        # Label
        lbl2 = tk.Label(root, text="Skill Issue", background="#dbc4a5", font=("Constantia", 12), anchor="center")
        lbl2.pack(expand=True)

        # Call ForgetPassword after a delay
        root.after(1000, lambda: self.ForgetPassword(root))

    def ForgetPassword(self, root):
        # Clear existing widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Adjust size
        root.geometry("1000x700")
        # set minimum window size value
        root.minsize(1000, 700)
        # set maximum window size value
        root.maxsize(1000, 700)

        # Title
        root.title("BURP Forget Password")

        recFP = ttk.Frame(root, style="Custom.TFrame", relief="flat", borderwidth=0)
        recFP.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Configure rows and columns to center widgets
        recFP.columnconfigure(0, weight=1)
        recFP.columnconfigure(1, weight=1)

        # Username label and text entry box
        usernameLabel = Label(recFP, text="Username: ", font=("Consolas", 12))
        usernameLabel.grid(row=0, column=0, sticky="e")

        username = StringVar()
        usernameEntry = tk.Entry(recFP, textvariable=username, bg='#c69962')
        usernameEntry.grid(row=0, column=1, sticky="w")

        # Ok
        okBtn = tk.Button(recFP, text="ok", font=("Constantia", 10), command=lambda: self.changePwd(root))
        okBtn.grid(row=1, column=0, columnspan=2, sticky="n", ipady=5, pady=0)

        # Back
        backBtn = tk.Button(recFP, text="Back", font=("Constantia", 10), command=lambda: self.openLoginPage(root))
        backBtn.grid(row=2, column=0, columnspan=2, sticky="n", ipady=5, pady=0)

        for widget in recFP.winfo_children():
            widget.grid(padx=5, pady=5)

    def changePwd(self, root, username):
        print("username entered :", username.get())

        # Backend
        r = BE.userlogin(username.get())

        if username.get() == username:
            self.openMainNotebooks(root)
        else:
            messagebox.showerror(title="Error", message="User does not exist.")

    def openMainNotebooks(self, root):
        # Clear existing widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Adjust size
        root.geometry("1000x700")
        # set minimum window size value
        root.minsize(1000, 700)
        # set maximum window size value
        root.maxsize(1000, 700)

        # Title
        root.title("BURP")

        # Create the container frame with padding background
        container = MyNotebookContainer(root)
        container.pack(expand=True, fill="both")

        # Create widgets for Notebook1
        container.notebook.notebook1.create_widgets()


if __name__ == "__main__":
    root = tk.Tk()

    # Create an instance of MYGUI with only the root window
    app = MYGUI(root)

    # Start the Tkinter event loop
    root.mainloop()

