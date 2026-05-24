import tkinter as tk






class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("paint")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="black",width=640,height=400)
        self.canvas.pack(padx=0,pady=0)
        self.bt1=tk.Button(background="black",text="delete",command=self.bt1_click,foreground="white")
        self.bt1.pack(padx=0,pady=0)
        self.counter:int=0
        self.objs=[]
        self.bb=None
        self.b=self.canvas.bind("<Button-1>",self.clicks)
        self.lastx=0
        self.lasty=0
    def clicks(self,event):
        a=self.counter & 1
        if a==0:
            self.lastx,self.lasty = event.x, event.y
        else:
            self.objs.append(self.canvas.create_line(self.lastx, self.lasty, event.x, event.y, fill="white"))
        
        self.counter=self.counter+1
    def bt1_click(self):
        if len(self.objs):
            a=len(self.objs)-1
            self.canvas.delete(self.objs[a])
            self.objs.pop()







root=tk.Tk()
apps=myapps(root)
root.mainloop()