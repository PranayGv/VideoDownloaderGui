"""
        Made by PranayGv copyright@ 2022
        Do    pip install pytube3
        
"""


from tkinter import *
from pytube import YouTube
from tkinter import filedialog

root=Tk()
root.title("Youtube video downloader")
root.geometry("365x584+400+100")
root.resizable(False,False)
def track():
    url = entry.get()
    file_path = filedialog.askdirectory()
    video = YouTube(url).streams.get_highest_resolution()
    if url=="Enter Url":status.config(text="Please enter valid URL")
    else:
        try:
            if file_path is not None:
                status.config(text="Status: Downloading")
                video.download(file_path)
                status.config(text=f"Status: Downloaded to {file_path}",wraplength = root.winfo_width())
            else: status.config(text="something wrong with your download destination")
        except Exception as e: status.config(text=f"Status: something went wrong {e}",wraplength = root.winfo_width())
    status.config(text="Status: waiting")



Heading=Label(root,text="Youtube Downloader",font=("arial",20,"bold"))
Heading.place(x=50,y=90)

entry=StringVar()
enter_number=Entry(root,textvariable=entry, width=17, bd=0, font=("arial",20),justify="center",)
enter_number.place(x=50,y=220)

Search_image=PhotoImage(file="assets/download png.png")   
search=Button(image=Search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=75,y=300)

Box=PhotoImage(file="assets/bottom png.png")
Label(root, image=Box).place(x=-2,y=355)

status = Label(root, text="Status: waiting",bg="#5770A9",fg="white",font=("arial",10,"bold"))
status.place(x=30,y=400)

root.mainloop()