import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import *
import webbrowser
import functools
import BE

# https://docs.google.com/document/d/1Bw5Bo-iJwp0QTucnMkPnswHnSbBIMvtjOY5WK25_GR8/edit

class MyNotebookContainer(Canvas):
    def __init__(self, master=None):
        # Set your desired background color
        super().__init__(master, bg='#a4b4eb')
        style = ttk.Style()
        style.configure('righttab.TNotebook', tabposition='en')  
        self.notebook = MyNotebook(self)
        self.create_window((55, 50), window=self.notebook, anchor='nw', width=890, height=600)
        
        # Create a rounded rectangle underneath the notebook
        CanvasUtils.round_rectangle(self, 50, 20, 950, 665, radius=30, fill="blue")
        CanvasUtils.round_rectangle(self, 50, 25, 950, 665, radius=30, fill="red")
        CanvasUtils.round_rectangle(self, 50, 30, 950, 665, radius=30, fill="green")
        # 20, 25 is y distance from top


class MyNotebook(ttk.Notebook):
    def __init__(self, master):
        super().__init__(master, style='righttab.TNotebook')
        self.notebook1 = Notebook1(self)
        self.notebook2 = Notebook2(self)
        self.notebook3 = Notebook3(self)
        self.notebook4 = Notebook4(self)
        self.add(self.notebook1, text="Home")
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
    def init(self, master=None):
        super().init(master)

    def create_widgets(self):
        # Frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=1)

        # 0,0 : Logo
        ttk.Label(self, text="Logo", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=10, pady=10, sticky='w')

        # 1,0 : Recommended header
        ttk.Label(self, text="Recommended!", font=("Helvetica", 12, "bold")).grid(column=1, row=0, sticky='w', pady=(10, 0))

        # 1,1 : Recommended Image on the left
        recommended_canvas = tk.Canvas(self, width=150, height=150)
        recommended_canvas.grid(column=1, row=1, padx=10, pady=10, sticky='w')

        # Placeholder for recommended image
        recommended_image_path = "pic1.jpeg"
        img = tk.PhotoImage(recommended_image_path)
        recommended_image_button = ttk.Button(recommended_canvas, image=img,
                                              command=lambda path=recommended_image_path: self.open_web(path))
        recommended_image_button.grid(column=0, row=0)

        # 1,2 : Recommended Description on the right
        ttk.Label(self, text="Recommended Recipe Description").grid(column=2, row=1, padx=10, pady=10, sticky='w')

        # 1,3 : Recent header
        ttk.Label(self, text="Recent", font=("Helvetica", 12, "bold")).grid(column=1, row=2, sticky='w', pady=(10, 0))

        # 1,4 : Horizontal slider for Recent images
        recent_frame = ttk.Frame(self)
        recent_frame.grid(column=1, row=3, sticky='w', pady=(0, 10))

        # Simulating 9 squares in the slider for Recent images
        for i in range(9):
            recent_image_path = f"path_to_recent_image_{i + 1}.png"  # Replace with actual paths
            ttk.Button(recent_frame, text=str(i + 1), command=lambda path=recent_image_path: self.open_web(path)).grid(column=i % 3, row=i // 3, padx=5)

    def open_web(self, url):
        new = 1
        webbrowser.open(url, new=new)

class Notebook2(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Page 1
        page1 = ttk.Frame(self)
        page1.pack(side="top", fill="both", expand=True)
        self.page1 = page1

        # Frame
        page1.columnconfigure(0, weight=1) # padding
        page1.columnconfigure(1, weight=2) # column 0
        page1.columnconfigure(2, weight=2) # column 1
        page1.columnconfigure(3, weight=2) # column 2
        page1.columnconfigure(4, weight=1) # padding

        page1.rowconfigure(0, weight=4) # Padding
        page1.rowconfigure(1, weight=3) # Name
        page1.rowconfigure(2, weight=3) # URL
        page1.rowconfigure(3, weight=4) # Spacer
        page1.rowconfigure(4, weight=2) # Ingredients header
        page1.rowconfigure(5, weight=2) # 7 rows
        page1.rowconfigure(6, weight=2)
        page1.rowconfigure(7, weight=2)
        page1.rowconfigure(8, weight=2) 
        page1.rowconfigure(9, weight=2) 
        page1.rowconfigure(10, weight=2) 
        page1.rowconfigure(11, weight=2) 
        page1.rowconfigure(12, weight=4) # Spacer
        page1.rowconfigure(13, weight=2) # Cuisine header
        page1.rowconfigure(14, weight=2) # 4 rows
        page1.rowconfigure(15, weight=2) 
        page1.rowconfigure(16, weight=2) 
        page1.rowconfigure(17, weight=2) 
        page1.rowconfigure(18, weight=4) # Spacer
        page1.rowconfigure(19, weight=3)  # Are you vegetarian?
        page1.rowconfigure(20, weight=2)

        # Space
        ttk.Frame(page1).grid(row=0, column=1, columnspan=5, pady=7)

        # Name
        ttk.Label(page1, text='Name of dish:').grid(column=1, row=1)
        name = ttk.Entry(page1, width=30)
        name.focus()
        name.grid(column=2, columnspan=2, row=1, sticky=tk.W)
        self.name = name

        # URL
        ttk.Label(page1, text='URL:').grid(column=1, row=2)
        urlname = ttk.Entry(page1, width=30)
        urlname.focus()
        urlname.grid(column=2, columnspan=2, row=2, sticky=tk.W)
        self.urlname = urlname

        # Space
        ttk.Frame(page1).grid(row=3, column=1, columnspan=5, pady=7)

        # Ingredients Section
        ttk.Label(page1, text="Ingredients").grid(row=4, column=1, padx=15, pady=5, columnspan=3, sticky="w")
        ingredients_list = ["Rice", "Noodles", "Pasta", "Potato", "Chicken", "Beef", "Pork", "Fish", "Egg", "Milk", "Cheese", "Yoghurt", "Carrot", "Tomato", "Lettuce", "Brocoli", "Bok Choy", "Soya Sauce", "Chili", "Ketchup", "Fish Sauce"] 
        self.ingredients_var = self.create_checkbox_columns(page1, ingredients_list, 3, 1, 5)
        self.ingredients_list = ingredients_list

        # Space
        ttk.Frame(page1).grid(row=12, column=1, columnspan=5, pady=7)

        # Cuisine Section
        ttk.Label(page1, text="Cuisine").grid(row=13, column=1, padx=15, pady=5, columnspan=3, sticky="w")
        cuisine_list = ["Indonesian", "Singaporean", "Chinese", "Malay", "Indian", "Western", "Korean", "Japanese"]
        self.cuisine_var = self.create_checkbox_columns(page1, cuisine_list, 2, 1, 14)
        self.cuisine_list = cuisine_list

        # Space
        ttk.Frame(page1).grid(row=18, column=1, columnspan=5, pady=10)

        # Vegetarian Section
        ttk.Label(page1, text="Are you vegetarian?").grid(row=19, column=1, padx=15, pady=5, columnspan=3, sticky="w")
        self.var = tk.BooleanVar(value=False)
        R1 = Radiobutton(page1, text="Yes", variable=self.var, value=True)
        R1.grid(row=20, column=1)
        R2 = Radiobutton(page1, text="No", variable=self.var, value=False)
        R2.grid(row=20, column=2)

        # Button to send data
        next_button = ttk.Button(page1, text="Create", command=self.send_data)
        next_button.grid(row=20, column=3, sticky="se")

    def create_checkbox_columns(self, parent, items, num_columns, start_column, start_row):
        vars_list = []
        for i, item in enumerate(items):
            var = tk.BooleanVar(value=False)
            ttk.Checkbutton(parent, text=item, variable=var).grid(row=start_row + i // num_columns, column=start_column + i % num_columns, sticky="w", pady=5)
            vars_list.append(var)
        return vars_list
    
    
    def send_data(self): # Notebook2: create
        # global usernme
        dishName = self.name.get()
        urlLink = self.urlname.get()
        veg_bool = self.var.get()
        selected_ingredients = [item for item, var in zip(self.ingredients_list, self.ingredients_var) if var.get()]
        selected_cuisine = [item for item, var in zip(self.cuisine_list, self.cuisine_var) if var.get()]
        print(dishName, urlLink, veg_bool, selected_cuisine, selected_ingredients)
        return dishName, urlLink, veg_bool, selected_cuisine, selected_ingredients

    def store_data(self):
        dishName,urlLink,veg_bool,selected_cuisine,selected_ingredients = self.send_data()
        try:
            BE.upload(title,it1,it2,it3,cuisine,vegtag,ur)
        except:
            print('Recipe not uploaded')





class Notebook3(ttk.Frame): # Cook/Recipe
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Page 1
        page1 = ttk.Frame(self)
        page1.pack(side="top", fill="both", expand=True)
        self.page1 = page1

        # Frame
        page1.columnconfigure(0, weight=1) # padding
        page1.columnconfigure(1, weight=2) # column 0
        page1.columnconfigure(2, weight=2) # column 1
        page1.columnconfigure(3, weight=2) # column 2
        page1.columnconfigure(4, weight=1) # padding
        page1.rowconfigure(0, weight=15) # Padding
        page1.rowconfigure(1, weight=3) # Ingredients header
        page1.rowconfigure(2, weight=2) # 7 rows
        page1.rowconfigure(3, weight=2) 
        page1.rowconfigure(4, weight=2)
        page1.rowconfigure(5, weight=2)
        page1.rowconfigure(6, weight=2)
        page1.rowconfigure(7, weight=2)
        page1.rowconfigure(8, weight=2) 
        page1.rowconfigure(9, weight=4) # Spacer
        page1.rowconfigure(10, weight=3) # Cuisine header
        page1.rowconfigure(11, weight=2) # 4 rows
        page1.rowconfigure(12, weight=2) 
        page1.rowconfigure(13, weight=2)
        page1.rowconfigure(14, weight=2)
        page1.rowconfigure(15, weight=4) # Spacer
        page1.rowconfigure(16, weight=3) # Are you vegetarian?
        page1.rowconfigure(17, weight=2)


        # Ingredients Section
        ttk.Label(page1, text="Ingredients").grid(row=1, column=1, padx=15, pady=5, columnspan=3, sticky="w")
        ingredients_list = ["Rice", "Noodles", "Pasta", "Potato", "Chicken", "Beef", "Pork", "Fish", "Egg", "Milk", "Cheese", "Yoghurt", "Carrot", "Tomato", "Lettuce", "Brocoli", "Bok Choy", "Soya Sauce", "Chili", "Ketchup", "Fish Sauce"] 
        self.ingredients_var = self.create_checkbox_columns(page1, ingredients_list, 3, 1, 2)
        self.ingredients_list = ingredients_list

        # Space
        ttk.Frame(page1).grid(row=9, column=1, columnspan=5, pady=10)

        # Cuisine Section
        ttk.Label(page1, text="Cuisine").grid(row=10, column=1, padx=15, pady=5, columnspan=3, sticky="w")
        cuisine_list = ["Indonesian", "Singaporean", "Chinese", "Malay", "Indian", "Western", "Korean", "Japanese"]
        self.cuisine_var = self.create_checkbox_columns(page1, cuisine_list, 2, 1, 11)
        self.cuisine_list = cuisine_list

        # Space
        ttk.Frame(page1).grid(row=15, column=1, columnspan=5, pady=10)

        # Vegetarian Section
        ttk.Label(page1, text="Are you vegetarian?").grid(row=16, column=1, padx=15, pady=5, columnspan=3, sticky="w")
        self.var = tk.BooleanVar(value=False)
        R1 = Radiobutton(page1, text="Yes", variable=self.var, value=True)
        R1.grid(row=17, column=1)
        R2 = Radiobutton(page1, text="No", variable=self.var, value=False)
        R2.grid(row=17, column=2)

        # Button to Navigate to Page 2
        next_button = ttk.Button(page1, text="Generate Recipes", command=self.btn)
        next_button.grid(row=17, column=3, sticky="se")

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
            ttk.Checkbutton(parent, text=item, variable=var).grid(row=start_row + i // num_columns, column=start_column + i % num_columns, sticky="w", pady=5)
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

    def btn(self): # Notebook3: Cook/Recipe
        selected_ingredients, selected_cuisine, veg_bool = self.compile_data()
        self.show_page2(selected_ingredients, selected_cuisine, veg_bool)
    
    # Hide Page 1 and Show Page 2
    def show_page2(self, selected_ingredients, selected_cuisine, veg_bool): 
        self.page1.pack_forget()
        self.page2.pack(side="top", fill="both", expand=True)
        # text = BE.get_oline_recipe(selected_ingredients, selected_cuisine, veg_bool)

        def open_recipe_link(self):
            # Replace with the actual URL based on the selected recipe
            url = f"https://www.recipetineats.com/baked-ziti/"
            webbrowser.open(url, new=1)

# Wen Xin section
        

class Notebook4(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
    
    def create_widgets(self):
        # Top half
        top_frame = ttk.Frame(self)
        top_frame.pack(side="top", fill="both", expand=True)

        # Profile Image
        profile_image = tk.Canvas(top_frame, width=100, height=100, bg="gray")
        profile_image.create_oval(10, 10, 90, 90, fill="blue")  # Placeholder circle
        profile_image.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Account Details
        account_details = ttk.Label(top_frame, text="Lorem Ipsum\nProfile Details\nMore Details")
        account_details.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Bottom half
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(side="bottom", fill="both", expand=True)

        # Rectangle with Tabs
        rectangle_frame = ttk.Frame(bottom_frame, relief="solid", borderwidth=1)
        rectangle_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Tabs in the Rectangle
        tab_control = ttk.Notebook(rectangle_frame)

        # Uploads Tab
        uploads_tab = ttk.Frame(tab_control)
        ttk.Label(uploads_tab, text="Content of Uploads Tab").pack(pady=10)
        tab_control.add(uploads_tab, text='Uploads')

        # Bookmarked Tab
        bookmarked_tab = ttk.Frame(tab_control)
        ttk.Label(bookmarked_tab, text="Content of Bookmarked Tab").pack(pady=10)
        tab_control.add(bookmarked_tab, text='Bookmarked')

        # Pack the Notebook (Tabs)
        tab_control.pack(expand=1, fill="both")


class MYGUI:
    def __init__(self, root):
        self.initLoadingPage(root)

    def initLoadingPage(self, root):
        # Adjust size
        root.geometry("1000x700")
        # set minimum window size value
        root.minsize(1000, 700)
        # set maximum window size value
        root.maxsize(1000, 700)

        # Title
        root.title("BURP")

        # Center the loading text and button
        loading_label = ttk.Label(root, text="Loading...")
        loading_label.pack(pady=10)

        Btn = Button(root, text="Next", command=lambda: self.openLoginPage(root))
        Btn.pack(pady=10)

    def _from_rgb(self, rgb):
        # translates an rgb tuple of int to a tkinter friendly color code
        return "#%02x%02x%02x" % rgb
    
    def openLoginPage(self,root):
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

        # Configure rows and columns to center widgets
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        # Username label and text entry box
        usernameLabel = Label(root, text="Username: ").grid(row=0, column=0, sticky="e")
        username = StringVar()
        usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1, sticky="w") 

        # Password label and password entry box
        passwordLabel = Label(root,text="Password: ").grid(row=1, column=0, sticky="e")  
        password = StringVar()
        passwordEntry = Entry(root, textvariable=password, show='*').grid(row=1, column=1, sticky="w")
        
        # Space
        ttk.Frame(root).grid(row=2, column=0, columnspan=2, pady=0)

        validateLogin = functools.partial(self.validateLogin, root, username, password)
        
        # Login Btn
        Btn = Button(root, text="Login", command=validateLogin).grid(row=3, column=0, columnspan=2, sticky="n", ipady=5, pady=0)

        # Space
        ttk.Frame(root).grid(row=4, column=0, columnspan=2, pady=0)

        # Create Acc Btn
        Btn2 = Button(root, text="Create Account :D", command=lambda:self.CreateAccount(root)).grid(row=5, column=0, columnspan=2, sticky="n", ipady=5, pady=0)

        for widget in root.winfo_children():
            widget.grid(padx=5, pady=5)

    def validateLogin(self, root, username, password):
        print("username entered :", username.get())
        print("password entered :", password.get())

        # WX: Change "username" and "password" to data from database?
        if username.get()=="username" and password.get()=="password":
            self.openMainNotebooks(root)
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    # Suggestion for Wen Xin
    '''
    if username.get() == LOGIN_DETAILS["username"] and password.get() == LOGIN_DETAILS["password"]:
            self.openMainNotebooks(root)

    # Centralized login details
    LOGIN_DETAILS = {
        "username": "your_username",
        "password": "your_password",
        }

    Login details are stored in the LOGIN_DETAILS dictionary.
    You can easily modify the values in this dictionary to update the login credentials.
    '''

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

        # Configure rows and columns to center widgets
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)

        # Username label and text entry box
        usernameLabel = Label(root, text="Username: ").grid(row=0, column=0, sticky="e")
        username = StringVar()
        usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1, sticky="w") 

        # Password label and password entry box
        passwordLabel = Label(root,text="Password: ").grid(row=1, column=0, sticky="e")  
        password = StringVar()
        passwordEntry = Entry(root, textvariable=password).grid(row=1, column=1, sticky="w")

        # Email label and email entry box
        emailLabel = Label(root, text="Email (opt): ").grid(row=2, column=0, sticky="e")  
        email = StringVar()
        emailLabel = Entry(root, textvariable=email).grid(row=2, column=1, sticky="w")

        # Wen Xin: Add account to database? and then return to login page
        CBtn = Button(root, text="Create", command=lambda:self.openLoginPage(root))
        CBtn.grid(row=3, column=0, columnspan=2, sticky="n", ipady=5, pady=0)

        for widget in root.winfo_children():
            widget.grid(padx=5, pady=5)

    def add_new(self, root):
        pass
    # Wen Xin to return the data to her.


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
