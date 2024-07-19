from tkinter import *
from random import *
##from PIL import ImageTk, Image
f = open("picList.txt","r")
x = f.readlines()
picfiles = list()
for p in x:
    fn = p.strip().split(';')
    picfiles.append(fn[1])
    
picNum = 0



class Window(Frame):
    Level = 0
    picfiles = []
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        root.config(bg = "#1D2951")
        self.Frame1()
        self.Frame2()
        self.FrameShowLetters()
        self.FrameButtons()
        #self.clearWords()
        self.pack()

    def List(self):
        f = open("picList.txt","r")
        x = f.readlines()
        picfiles = list()
        for p in x:
            fn = p.strip().split(';')
            Window.picfiles.append(fn[1])
            
    def Frame1(self):
        #Frame for the Top part 
        Topframe = Frame(self.master,bg = 'Royal blue')
        Topframe.pack(side = TOP,fill = X,pady = 6)
        LevelLabel = Label(Topframe, text = 'LEVEL:',font = 'Arial 11',bg = 'Royal blue',height = 2)
        LevelLabel.pack(side = LEFT,padx = 5) 
        self.LevelNumber = Label(Topframe, text = '1',font = 'Arial 15 bold',bg = 'Royal blue')
        self.LevelNumber.pack(side = LEFT)
        self.CoinsLeft = Label(Topframe, text = '100', font = 'Arial 15 bold', bg = 'Royal blue')
        self.CoinsLeft.pack(side = RIGHT,padx = 5)

        CoinIcon = Label(Topframe,text = 'Coins:', font = 'Arial 11',bg = 'Royal blue')
        CoinIcon.pack(side = RIGHT)
        
        #coins = PhotoImage(file = "coin_32.png")
        #lblcoin = Label(Topframe, image = coins, bg = 'Royal blue')
        #lblcoin.image = coins
        #lblcoin.pack(side = RIGHT, padx = 4)
        
    def Frame2(self):
        #Frame for the Picture
        MidFrame = Frame(self.master, bg = "#1D2951")
        MidFrame.pack(fill = X,pady = 5)
        self.pics = PhotoImage(file=picfiles[0]+".png")
        lblpic = Label(MidFrame,image=self.pics)
        lblpic.pack()
        #self.nextPic = Button(MidFrame,text="Picture No."+str(picNum+1)+". NEXT?",command=self.changeImage)
        #self.nextPic.pack()

    def FrameShowLetters(self):
        #Frame for the buttons/empty boxes below the picture
        showframe = Frame(self.master)
        showframe.pack(pady = 5)
##        b = picfiles[picNum]
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##        self.a = sample(self.alpha,12-len(b))
##        for i in b.upper():
##            c = randint(0,11)
##            self.a.insert(c,i)
##        cols = 0#
        self.wordanswer = Label(showframe, width = 20, height = 2,font = 'System 15')
        self.wordanswer.grid(row = 0, column = 0)
        CheckButton = Button(showframe, text = "CHECK", font = "Arial 10 bold",
                            height = 2, width = 5, relief = "solid",
                            bg = "black" , fg = "white")
        CheckButton.grid(column = 1, row = 0 )
        CheckButton.bind('<Button-1>', self.check)

        DeleteButton = Button(showframe, text = "DELETE", font = "Arial 10 bold",
                            height = 2, width = 5, relief = "solid",
                            bg = "red" , fg = "white")
        
        DeleteButton.grid(column = 2, row = 0)
        

    #def clearWords(self):
        
        
    def FrameButtons(self):
        #Frame for the Button
        BottomFrame = Frame(self.master,bg = "#800000")
        BottomFrame.pack(padx = 6, pady = 6)
        BLight_bulb = Button(BottomFrame, text = "HINT", font = "Arial 10 bold",
                             height = 2, width = 5, relief = "solid", bg = "black", fg = "white",
                             command = self.hint)
        PassButton = Button(BottomFrame, text = "PASS", font = "Arial 10 bold",
                            height = 2, width = 5, relief = "solid", bg = "black" ,
                            fg = "white", command = self.changeImage)
        
        BLight_bulb.grid(column = 11, row = 0, padx = 3, pady = 3)
        PassButton.grid(column = 11, row = 1, padx = 3, pady = 3)
##        self.B1 = Button(BottomFrame, text = self.a[letters],font = 'Arial 10 bold', fg = "black", height = 2, width = 5,
##                        relief = "solid",command = self.letterrepl))
        self.buttons2 = [None for _ in range(26)]
        r = 0
        col = 0
        
        for i in range(26):
            self.buttons2[i] = Button(BottomFrame, text = self.alpha[i],font = 'Arial 9 bold', fg = "black", height = 2, width = 5,
                        relief = "solid",command = lambda i=i:self.letterplace(i))
            self.buttons2[i].grid(column = col, row = r, padx = 1, pady = 3)
            col+=1
            if i!=10 and (i+1)%10==0:
                r+=1
                col = 0
                if r==2:
                    col=2
       
        
    def changeImage(self):
        global picNum
        picNum+=1
        if picNum==50:
            picNum=0
        self.pics.config(file=picfiles[picNum]+".png")
        self.LevelNumber['text'] = str(picNum+1)
        self.CoinsLeft['text'] = str(int(self.CoinsLeft['text'])-10)
        word = picfiles[picNum]
 
    def letterplace(self,index):
        newtext = self.wordanswer['text']+self.buttons2[index]['text']
        self.wordanswer.config(text = newtext)

    def hint(self):
        self.CoinsLeft['text'] = str(int(self.CoinsLeft['text'])-2)
        word = picfiles[picNum]
        a = self.wordanswer['text']
        for i in range(len(word)):
            if a == '':
                self.wordanswer['text'] = a+word[i]
                break
            elif a!='':
                self.wordanswer['text'] = a+word[len(a)]
            
    
    def check(self,*args):
        global picNum
        word = self.wordanswer['text']
        if word == picfiles[picNum].upper():
            if picNum==50:
                picNum=0
            picNum+=1
            self.CoinsLeft['text'] = str(int(self.CoinsLeft['text'])+10)
            self.wordanswer['text'] = ''
            self.pics.config(file=picfiles[picNum]+".png")
            self.LevelNumber['text'] = str(picNum+1)
        else:
            self.wordanswer['text']=''
            word = self.wordanswer['text']
            


root = Tk()
root.title("4 pics 1 word")
#root.iconbitmap("d:/MACHINE PROBLEM 2/Pics/pics/4picsicon.ico") #icon katabi nung title 
root.geometry("550x590")
##root.resizable(0, 0)
app = Window(root)
root.mainloop()

