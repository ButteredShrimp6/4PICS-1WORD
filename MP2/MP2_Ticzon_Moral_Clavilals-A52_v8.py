from tkinter import *
from tkinter import messagebox
from random import *
import string
from abc import ABC, abstractmethod

f = open("picList.txt","r")
x = f.readlines()



class Window(ABC,Frame):
    @abstractmethod
    def Frame1(self):
        pass
             
    def Frame2(self):
        pass

class Functions(Window):    
    picfiles = list()
    Level = 1 
    coins = 100 
    
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        root.config(bg = "#1D2951")
        self.list()
        self.Frame1()
        self.Frame2()
        self.OpenPlayerData()
        self.FrameButtons()
        self.FrameShowLetters()
        self.keyboardchange()
        self.pack()

    def list(self):
        for p in x:
            fn = p.strip().split(';')
            Functions.picfiles.append(fn[1])

    def OpenPlayerData(self):
        try:
            f=open('PlayerData.txt','r')
        except Exception as e:
            pass
        else:
            x=f.read()
            if len(x)==0:
                return
            else:
                r=x.split(',')
                Functions.Level = int(r[0])
                Functionscoins=int(r[1])
                self.LevelNumber['text'] = str(Functions.Level)
                self.CoinsLeft['text'] = str(Functions.coins)
                self.pics.config(file=Functions.picfiles[Functions.Level-1]+".png")
    def Frame1(self):
        #Frame for the Top part 
        Topframe = Frame(self.master,bg = 'Royal blue')
        Topframe.pack(side = TOP,fill = X,pady = 6)
        LevelLabel = Label(Topframe, text = 'LEVEL:',font = 'Arial 11',bg = 'Royal blue',height = 2)
        LevelLabel.pack(side = LEFT,padx = 5) 
        self.LevelNumber = Label(Topframe, text = Functions.Level,font = 'Arial 15 bold',bg = 'Royal blue')
        self.LevelNumber.pack(side = LEFT)
        self.CoinsLeft = Label(Topframe, text = Functions.coins, font = 'Arial 15 bold', bg = 'Royal blue')
        self.CoinsLeft.pack(side = RIGHT,padx = 5)

        CoinIcon = Label(Topframe,text = 'Coins:', font = 'Arial 11',bg = 'Royal blue')
        CoinIcon.pack(side = RIGHT)
        
        coins = PhotoImage(file = "coin_32.png")
        lblcoin = Label(Topframe, image = coins, bg = 'Royal blue')
        lblcoin.image = coins
        lblcoin.pack(side = RIGHT, padx = 4)
             
    def Frame2(self):
        #Frame for the Picture
        MidFrame = Frame(self.master, bg = "#1D2951")
        MidFrame.pack(fill = X,pady = 5)
        self.pics = PhotoImage(file=Functions.picfiles[0]+".png")
        lblpic = Label(MidFrame,image=self.pics)
        lblpic.pack()

                
    def FrameShowLetters(self):
        global showframe
        #Frame for the buttons/empty boxes below the picture
        showframe = Frame(self.master)
        showframe.pack(pady = 5)
        self.wordanswer = [None for x in range(len(Functions.picfiles[Functions.Level-1]))]
        r = 0
        c = 0
        for i in range(len(Functions.picfiles[Functions.Level-1])):
            self.wordanswer[i] = Button(showframe,text = '',font = "System 10",
                            height = 2, width = 5, relief = "solid")
            self.wordanswer[i].grid(row = 0, column = c)
            c+=1
        self.CheckButton = Button(showframe, text = "CHECK", font = "Arial 10 bold",
                            height = 2, width = 5, relief = "solid",
                            bg = "black" , fg = "white",command = self.check)
        self.CheckButton.grid(column = len(Functions.picfiles[Functions.Level-1])+1, row = 0 )

        DeleteButton = Button(showframe, text = "DELETE", font = "Arial 10 bold",
                            height = 2, width = 6, relief = "solid",
                            bg = "red" , fg = "white",command = self.clearWords)
        
        DeleteButton.grid(column = len(Functions.picfiles[Functions.Level-1])+2, row = 0)
        
 
    def FrameButtons(self):
        global BottomFrame
        #Frame for the Button
        BottomFrame = Frame(self.master,bg = "#800000")
        BottomFrame.pack(padx = 6, pady = 6)
        lightbulb = PhotoImage(file = "Light_bulb_button.png")
        Pbutton = PhotoImage(file = "Pass_button.png")
        self.BLight_bulb = Button(BottomFrame, image = lightbulb, 
                         height = 32, width = 32, activebackground = "black", relief = "solid", bg = "black", fg = "white",state = NORMAL,
                         command = self.hint)
   
        self.PassButton = Button(BottomFrame, image = Pbutton,
                        height = 32, width = 32,activebackground = "black", relief = "solid", bg = "black" ,
                        fg = "white",state = NORMAL, command = self.changeImage)      
        self.BLight_bulb.image = lightbulb
        self.PassButton.image = Pbutton
        self.BLight_bulb.grid(column = 0, row = 0, padx = 3, pady = 3)
        self.PassButton.grid(column = 1, row = 0, padx = 3, pady = 3)
        self.btnSave=Button(BottomFrame,text = "SAVE",font = "Arial 10 bold",
                            height = 2,width = 5,activebackground = "black",relief = SOLID,
                            bg = "black",fg = "white",command=self.UserSave)
        self.btnSave.grid(column = 4, row = 0, padx = 3, pady = 3)
        btnQuit=Button(BottomFrame,text = "QUIT",font = "Arial 10 bold",
                            height = 2,width = 5,activebackground = "black",relief = SOLID,
                            bg = "black",fg = "white",command=self.UserQuit)
        btnQuit.grid(column = 3, row = 0, padx = 3, pady = 3)
            
    def keyboardchange(self):
        global button,frame
        frame = Frame(self.master,bg = "#800000")
        frame.pack(padx = 6, pady = 6)
        self.button = [None for x in range(12)]
        x = Functions.picfiles[Functions.Level-1]
        letters = sample(string.ascii_uppercase,12 - len(Functions.picfiles[Functions.Level-1]))
        for k in x.upper():
            n = randint(0,11)           
            letters.insert(n,k)
        letters = list(letters)
        r = 1
        c = 0
        for i in range(12):
            if c == 6:
                r+=1
                c = 0
            self.button[i] = Button(frame,text = letters[i],width = 5, height = 2,font = 'Arial 9 bold', fg = "black",
                        relief = "solid",command = lambda i=i:self.letterplace(i))
            self.button[i].grid(row = r,column=c, padx = 1, pady = 3)
            c+=1

    def clearWords(self):
        for i in self.wordanswer:
            i['text'] = ''
        for i in self.button:
            i.config(state = ACTIVE)
        
    def changeImage(self):
        global button,frame,showframe
        Functions.Level+=1
        Functions.coins-=10
        if Functions.Level==51:
            Functions.Level=1
        if Functions.coins == 0:
            self.BLight_bulb.config(state = DISABLED)
            self.PassButton.config(state = DISABLED)
        elif (Functions.coins-10)< 0:
            self.PassButton.config(state = DISABLED)
        showframe.destroy()
        for b in self.wordanswer:
            b.destroy()
        frame.destroy()
        for i in self.button:
            i.destroy()
        self.FrameShowLetters()
        self.keyboardchange()
        self.pics.config(file=Functions.picfiles[Functions.Level-1]+".png")
        self.LevelNumber['text'] = str(Functions.Level)
        self.CoinsLeft['text'] = str(Functions.coins)
        
            
    def letterplace(self,index):
        for i in range(len(self.wordanswer)):
            if self.wordanswer[i]['text'] == '':
                self.wordanswer[i].config(text = self.button[index]['text'])
                self.button[index].config(state = DISABLED)
                break
            else:
                continue

    def hint(self):
        word = Functions.picfiles[Functions.Level-1].upper()
        Window.coins-=2
        self.CoinsLeft['text'] = str(Functions.coins)
        if Functions.coins == 0:
            self.BLight_bulb.config(state = DISABLED)
            self.PassButton.config(state = DISABLED)
        elif (Functions.coins-2)< 0:
            self.PassButton.config(state = DISABLED)
        for i in range(len(self.wordanswer)):
            if self.wordanswer[i]['text'] == '':
                self.wordanswer[i]['text'] = word[i]
                for k in self.button:
                    if k['text'] == word[i]:
                        k.config(state = DISABLED)
                    else:
                        continue
                break
            else:
                continue
    
    def check(self,*args):
        global picNum,showframe,frame
        word = ''
        try:
            for i in self.wordanswer:
                word = word+i['text']
            if word == Functions.picfiles[Functions.Level-1].upper():
                if Functions.Level==51:
                    Functions.Level=0
                Functions.Level+=1
                BottomFrame.destroy()
                self.FrameButtons()
                showframe.destroy()
                for b in self.wordanswer:
                    b.destroy()
                frame.destroy()
                for i in self.button:
                    i.destroy()
                self.FrameShowLetters()
                self.keyboardchange()
                Functions.coins+=10
                self.CoinsLeft['text'] = str(Functions.coins)
                self.pics.config(file=Functions.picfiles[Functions.Level-1]+".png")
                self.LevelNumber['text'] = str(Functions.Level)
            else:
                for i in self.wordanswer:
                    i['text'] = ''
        except:
            self.CheckButton.config(state = DISABLED)

    def UserSave(self):
        with open('PlayerData.txt','w') as f:
            a=str(Functions.Level)
            b=str(Functions.coins)
            f.write('{},{}'.format(a,b))
            f.close() 

    def UserQuit(self):
        if messagebox.askokcancel('Quit','Do you want to quit?'):
            root.destroy()            
        
 
          
root = Tk()
root.geometry("500x590")
root.title("4 pics 1 word")
root.iconbitmap("4picsicon.ico")
app = Functions(root)
root.protocol('WM_DELETE_WINDOW',app.UserQuit)
root.mainloop()
