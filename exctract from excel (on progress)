import tkinter as tk
from tkinter import filedialog
import pandas as pd

# findata from excel. (on progress)
    root = tk.Tk()
    canvas1 = tk.Canvas(root)
    canvas1.pack()
    def getfile():
        global df
        file = filedialog.askopenfilename()
        df = pd.read_excel(file)
        print(df)


    browseButton_Excel = tk.Button(text='Import Excel File', command=getfile)
    canvas1.create_window(150, 150, window=browseButton_Excel)

    root.mainloop()

#if choice == 3: # findata from web. Webscrapping (beautifulSoup): finance.yahoo, bloomberg (on progress) 

