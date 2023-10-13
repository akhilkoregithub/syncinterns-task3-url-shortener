from copy import copy
from struct import pack
from tokenize import String
import pyperclip
import pyshorteners
from tkinter import *

#GUI
root = Tk()
root.geometry("700x350")
root.title("URL Shortener Application")
root.configure(bg="#7CB9E8")

#Define Variable for url
urlmain = StringVar()
urlshortmain = StringVar()

#Define Function
def urlShortner():
    urladdress = urlmain.get()
    urlshort = pyshorteners.Shortener().tinyurl.short(urladdress)
    urlshortmain.set(urlshort)

def copyurl():
    urlshort = urlshortmain.get()
    pyperclip.copy(urlshort)


Label(root,text="URL Shortener App",font=('Arial', 12)).pack(pady=10)
#Label(root, text="Enter URL Here", font=('Arial', 9)).pack(pady=(25,0))
Label(root, text="Enter URL Here", font=('Arial', 9)).place(x=75, y=35)
Entry(root,textvariable=urlmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Covet",command=urlShortner, width=10).pack(pady=20)
#Label(root, text="Short URL", font=('Arial', 9)).pack(pady=(20, 0))
Label(root, text="Short URL", font=('Arial', 9)).place(x=75, y=145)
Entry(root,textvariable=urlshortmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Copy",command=copyurl, width=9).pack(pady=15)

root.mainloop()
