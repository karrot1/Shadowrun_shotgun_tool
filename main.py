from tkinter import *
from shotgun import *
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Shadowrun Shotgun Tool")
        self.grid()
        column1 = ['', 'Short\n(0-15)', 'Medium\n(16-30)', 'Long\n(31-45)', 'Extreme\n(46-60)']
        r=0
        for c in column1:
            Label(self, text=c, relief=RIDGE,width=10).grid(row=r,column=0)
            r = r + 1
        row1 = ['Narrow', 'Medium', 'Wide']
        r=0
        for c in row1:
            Label(self, text=c, relief=RIDGE,width=16).grid(row=0,column=r+1, columnspan = 2)
            r = r + 2
        shotty = Shotgun(4, 14)
        self.update_shotgunstats(shotty)

        #setting up entry spaces
        Label(self, text="DV", relief=RIDGE, width=8).grid(row=6, column=1)
        dventry = Entry(self, width = 8)
        dventry.grid(row = 6, column =2)
        dventry.insert(0, 14)
        Label(self, text="acc", relief=RIDGE, width=8).grid(row=6, column=3)
        accentry = Entry(self, width = 8)
        accentry.grid(row = 6, column = 4)
        accentry.insert(0, 4)
        statbutton = Button(self,text="Recalculate", width = 16, command =lambda: self.recalculate(shotty, dventry, accentry))
        statbutton.grid(row=6, column=5)
    def recalculate(self, shotty, dventry, accentry):
        shotgunstats = shotty.getstats()
        dv = shotgunstats[0]
        acc = shotgunstats[1]
        try:
            dv = int(dventry.get())
        except:
            dventry.delete(0, END)
            dventry.insert(0, shotgunstats[0])
        try:
            acc = int(accentry.get())
        except:
            accentry.delete(0, END)
            accentry.insert(0, shotgunstats[1])
        shotty.setstats(acc, dv)
        self.update_shotgunstats(shotty)

    def update_shotgunstats(self, shotty):
        shotstats =shotty.getstats()
        y = 0
        while (y < 4):
            x = 0
            while(x<3):
                labeltext = ""
                if x == 0:
                    labeltext = str(shotstats[0]) + "P, -1 def, " +str(shotstats[1])+"acc"+ "\n" + "1 target"
                elif x == 1:
                    labeltext = str(shotstats[0]-(1+y*2))+"P, -3 def, "
                    if y <2 :
                        labeltext += str(shotstats[1])+"acc"+ "\n"
                    else:
                        labeltext +=str(shotstats[1]-1)+"acc"+ "\n"
                    labeltext+=str(y+2)+" targets, " + str(2*(y+1))+"m"
                else:
                    labeltext = str(shotstats[0]-(1+(1+y)*2))+"P, -5 def, "
                    if y <2 :
                        labeltext += str(shotstats[1])+"acc"+ "\n"
                    else:
                        labeltext +=str(shotstats[1]-1)+"acc"+ "\n"
                    if y != 3:
                        labeltext+=str(y+2)+" targets, " + str(3*(y+1))+"m"
                    else:
                        labeltext += "6 targets, " + str(3 * (y + 1)) + "m"
                Label(self, text=labeltext, relief=RIDGE, width=16).grid(row=y+1, column=(x*2)+1, columnspan = 2)
                x = x+1
            y = y+1
root = Tk()
app = Window(root)
root.mainloop()