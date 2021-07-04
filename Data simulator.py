from tkinter import*
import random

root = Tk()
root.title("Dice simulator")

root.geometry('400x300')

label = Label(root,font = ("times", 150 , 'bold'), text ="",fg = 'red')

def rolldice():
  dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
  label.config(text = f'{random.choice(dice)}')
  label.pack()
  
button = Button(root, font = ("Helviticia", 25 , 'bold'), text = "roll the dice", command = rolldice, bg = 'blue')
button.place(x=100,y=0)
button.pack()

root.mainloop()
