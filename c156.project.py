from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Endless Pokemon Game")
root.geometry("600x400")

root.configure(background="aqua")

player1 = Label(root,text = "Player 1", bg="dark blue",fg="white")
player1.place(relx=0.2,rely=0.3,anchor= CENTER)

player2 = Label(root,text = "Player 2", bg="dark blue",fg="white")
player2.place(relx=0.8,rely=0.3,anchor= CENTER)

player1_score = Label(root,bg="blue",fg="white")
player1_score.place(relx=0.2,rely=0.4,anchor= CENTER)

player2_score = Label(root,bg="blue",fg="white")
player2_score.place(relx=0.8,rely=0.4,anchor= CENTER)

random_dice_value = Label(root,bg="red",fg="white")
random_dice_value.place(relx=0.5,rely=0.5,anchor= CENTER)


root.mainloop()