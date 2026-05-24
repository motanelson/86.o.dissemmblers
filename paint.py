import tkinter as tk






class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("paint")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="black",width=640,height=480)
        self.canvas.pack(padx=0,pady=0)
        self.counter:int=0
        self.bb=None
        self.b=self.canvas.bind("<Button-1>",self.clicks)
        self.lastx=0
        self.lasty=0
    def clicks(self,event):
        a=self.counter & 1
        if a==0:
            self.lastx,self.lasty = event.x, event.y
        else:
            self.canvas.create_line(self.lastx, self.lasty, event.x, event.y, fill="white")
        
        self.counter=self.counter+1







root=tk.Tk()
apps=myapps(root)
root.mainloop()