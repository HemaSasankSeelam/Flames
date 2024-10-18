from tkinter import *
import customtkinter as ct
import re
from collections import deque

class FLAMES:

    def __init__(self) -> None:
        self.root = Tk(className=" Flames Game")
        self.root.geometry("500x500+550+100")
        self.root.resizable(width=False,height=False)
        
        self.create_frames()
        self.root.bind("<Return>",self.checking) # adding event when press enter button
        self.root.mainloop()
    
    def validation(self,e :Event = None) -> None:

        self.l1.configure(text="")
        if self.b1.cget('state') == 'disabled' and e.char != '\r': # char != '\r' means enter button

            self.b1.configure(state=ACTIVE,text="Find Relation")
            self.p1.stop() # stops the progress bar
            self.p1.configure(progress_color="SystemButtonface")
            self.root.after_cancel(self.cancle)# cancle the timer

        if self.e1._entry == e.widget and self.e1.get() != "":

            if self.e1.get()[-1].isalpha() or e.char == " ": # self.e1.get()[-1]  returns last value
                pass
            else:
                t = self.e1.get()
                self.e1.delete(0,END)
                self.e1.insert(0,t[0:len(t)-1:1])

        elif self.e2._entry == e.widget and self.e2.get() != "":

            if self.e2.get()[-1].isalpha() or e.char == " ": # e.char == " " also accepts when press space bar
                pass
            else:
                t = self.e2.get() # gets the entire string
                self.e2.delete(0,END) # deletes every thing
                self.e2.insert(0,t[0:len(t)-1:1]) # enters upto last but one
            

    def create_frames(self) -> None:

        self.e1 = ct.CTkEntry(self.root,placeholder_text='Enter person1 Name',fg_color='SystemButtonface',
                              width=400,height=50,text_color="#1f71cf",font=("TimesNewRoman",25),justify='center')
        self.e1.pack(pady=10)

        self.e2 = ct.CTkEntry(self.root,placeholder_text='Enter person2 Name',fg_color='SystemButtonface',
                              width=400,height=50,text_color="#f207e3",font=("TimesNewRoman",25),justify='center')
        self.e2.pack(pady=(0,30))


        self.b1 = ct.CTkButton(self.root,width=300,height=40,text="Find Relation",font=("TimesNewRoman",20),corner_radius=100,
                               command=self.checking)
        self.b1.pack(pady=40)

        self.p1 = ct.CTkProgressBar(self.root,width=400,corner_radius=100,mode='indeterminate',fg_color='SystemButtonface',progress_color='SystemButtonface')
        self.p1.pack(pady=(0,70))

        self.l1 = ct.CTkLabel(self.root,text="",font=("TimesNewRoman",25),text_color='red')
        self.l1.pack()

        self.e1.bind("<KeyRelease>",self.validation)
        self.e2.bind("<KeyRelease>",self.validation)
        

    def checking(self,e :Event = None) -> None:

        if self.e1.get() == "" or self.e2.get() == "":
            self.l1.configure(text="Enter Names Correctly!")
        
        elif self.e1.get() == self.e2.get():
            self.l1.configure(text="Both Names Should Not Match")  

        else:
            self.e1._entry_focus_out()
            self.e2._entry_focus_out()
            self.b1.configure(text="Finding...",state=DISABLED)
            self.p1.configure(progress_color='#21d96a')
            self.p1.start()
            self.cancle = self.root.after(10000,self.finding_relation) # after 10 secs
            
    
    def finding_relation(self) ->None:

        self.b1.configure(text="Found",state=DISABLED)
        self.p1.configure(progress_color='Systembuttonface')

        name1 = self.e1.get().strip().lower() # removes leading white spcaes and converts to lower case
        name2 = self.e2.get().strip().lower()

        name1 = re.sub(pattern=r'\s',string=name1,repl="") # replace white spce with empty string
        name2 = re.sub(pattern=r'\s',string=name2,repl="")

        for i in name1:

            if i in name2:
                name1 = name1.replace(i,"",1) # repalce the common chars with empty string 1 time
                name2 = name2.replace(i,"",1)
            
        total_count = len(name1) + len(name2)

        li = deque(["F","L","A","M","E","S"])

        while len(li) != 1:

            li.rotate(-(total_count-1))
            li.popleft()
            
        meanings = {"F":"Friend's 🤝","L":"Lover's ﮩـﮩﮩ٨ـ🫀ﮩ٨ـﮩﮩ٨ـ","A":"Attraction 🧲","M":"Marriage 👰🏻","E":"Enemye's 😡","S":"Slibling's 👧🏻"}

        self.l1.configure(text=f"""The Relation Between\n  Two Person's Is\n  "{meanings[li[0]]}" """,text_color='#0ccef0')

            

FLAMES()
