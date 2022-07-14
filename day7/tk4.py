import tkinter as tk
root=tk.Tk()
root.title('My Window')
root.geometry('600x400')

btn=tk.Button(root,text='Click Me!',font=('Arial',50))
btn.place(x=100,y=100)
root.mainloop()
