from tkinter import *
import random
#A function that chooses a number between 1 and 6
#And shows a matching dice face
def show_face(dice):
    dice.delete("all")
    face_shown=random.randint(1,7)
    if(face_shown==1):
        dice.create_oval(30,33,50,53,fill="black")
    elif(face_shown==2):
        dice.create_oval(5,5,25,25,fill="black")
        dice.create_oval(57,59,77,79,fill="black")
    elif(face_shown==3):
        dice.create_oval(5,5,25,25,fill="black")
        dice.create_oval(57,59,77,79,fill="black")
        dice.create_oval(30,33,50,53,fill="black")
    elif(face_shown==4):
        dice.create_oval(5,5,25,25,fill="black")
        dice.create_oval(57,59,77,79,fill="black")
        dice.create_oval(55,5,75,25,fill="black")
        dice.create_oval(5,59,25,79,fill="black")
    elif(face_shown==5):
        dice.create_oval(5,5,25,25,fill="black")
        dice.create_oval(57,59,77,79,fill="black")
        dice.create_oval(55,5,75,25,fill="black")
        dice.create_oval(5,59,25,79,fill="black")
        dice.create_oval(30,33,50,53,fill="black")
    else:
        dice.create_oval(5,5,25,25,fill="black")
        dice.create_oval(59,59,79,79,fill="black")
        dice.create_oval(59,5,79,25,fill="black")
        dice.create_oval(5,59,25,79,fill="black")
        dice.create_oval(5,33,25,53,fill="black")
        dice.create_oval(59,33,79,53,fill="black")
#Creates both dice faces
def rollboth(dice1,dice2):
    show_face(dice1)
    show_face(dice2)
#This chunk of code stes up the GUI
window=Tk()
window.resizable(False, False)
window.title("Dice")
window.geometry("200x130")
window.configure(bg="grey")
roll_button=Button(text="ROLL",font=("ms serif",10),bg="red",fg="white",command=lambda:rollboth(dice1,dice2))
dice1 = Canvas(window,width=80,height=80, highlightthickness=2,bg="white",highlightbackground="black")
dice1.place(x=8,y=10)
dice2 = Canvas(window,width=80,height=80, highlightthickness=2,bg="white",highlightbackground="black")
dice2.place(x=108,y=10)
roll_button.place(x=77,y=100)
window.mainloop()
