 # Title
      more_details_window.title("Select a new Profile Picture")

      l1 = tk.Label(more_details_window,text='Choose a new Profile Picture :DD',width=30)  
      l1.grid(row=1,column=1)                     
      ro, col = 1, 1
      """ recommended_canvas = tk.Canvas(self, width=50, height=50)
         recommended_canvas.grid(column=col, row=ro, padx=10, pady=10, sticky='w') """

      filepath = "profilePicture/" + str(1) + ".png"
      print(filepath)
      img = PhotoImage(file=filepath)
      img_label = Label(image = img)
      button= Button(more_details_window, image=img)
      #button.pack(pady=30)
      print("displayed.")

      text= Label(more_details_window, text= "")
      text.pack(pady=30)