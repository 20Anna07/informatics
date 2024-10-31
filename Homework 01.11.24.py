from tkinter import *
from datetime import *
from PIL import Image, ImageTk

root = Tk()
root.title("Мировое время")
f1 = Frame(root, width = 200, height = 100)
f1.pack()

f2 = Frame(root, width = 200, height = 100)
f2.pack(side = LEFT)

f3 = Frame(root, width = 200, height = 100)
f3.pack(side = RIGHT)

now = datetime.utcnow()

def Paris(*args):
    time = (now + timedelta(hours=1)).time().replace(microsecond=0)
    Label(root, text=(f'В Париже сейчас {time}')).pack(pady=4)
def Moscow(*args):
    time = (now + timedelta(hours=3)).time().replace(microsecond=0)
    Label(root, text=(f'В Москве сейчас {time}')).pack(pady=4)
def London(*args):
    time = now.time().replace(microsecond=0)
    Label(root, text=(f'В Лондоне сейчас {time}')).pack(pady=4)
def Hongkong(*args):
    time = (now + timedelta(hours=8)).time().replace(microsecond=0)
    Label(root, text=(f'В Гонконге сейчас {time}')).pack(pady=4)
def Los_Angeles(*args):
    time = (now - timedelta(hours=8)).time().replace(microsecond=0)
    Label(root, text=(f'В Лос-Анжелесе сейчас {time}')).pack(pady=4)
def Toronto(*args):
    time = (now - timedelta(hours=5)).time().replace(microsecond=0)
    Label(root, text=(f'В Торонто сейчас {time}')).pack(pady=4)
def Tokyo(*args):
    time = (now + timedelta(hours=9)).time().replace(microsecond=0)
    Label(root, text=(f'В Токио сейчас {time}')).pack(pady=4)
def Rio_de_Janeiro(*args):
    time = (now - timedelta(hours=3)).time().replace(microsecond=0)
    Label(root, text=(f'В Рио-де-Жанейро сейчас {time}')).pack(pady=4)    

label = Label(f1, text="Выбери город:", font=("Arial", 14))
label.pack(pady=10)

button = Button(f2, text="Paris", command=Paris)
button.config(cursor="hand2", bg='#FFBBCC')
button.pack(pady=10, padx=100)
button = Button(f2, text="Moscow", command=Moscow)
button.config(cursor="hand2", bg='#FFCCCC')
button.pack(pady=10)
button = Button(f2, text="London", command=London)
button.config(cursor="hand2", bg='#FFDDCC')
button.pack(pady=10)
button = Button(f2, text="Hongkong", command=Hongkong)
button.config(cursor="hand2", bg='#FFEECC')
button.pack(pady=10)
button = Button(f3, text="Los Angeles", command=Los_Angeles)
button.config(cursor="hand2", bg='#BA99BE')
button.pack(pady=10, padx=100)
button = Button(f3, text="Toronto", command=Toronto)
button.config(cursor="hand2", bg='#D6B4D0')
button.pack(pady=10)
button = Button(f3, text="Tokyo", command=Tokyo)
button.config(cursor="hand2", bg='#D2C4FA')
button.pack(pady=10)
button = Button(f3, text="Rio de Janeiro", command=Rio_de_Janeiro)
button.config(cursor="hand2", bg='#E7D7FF')
button.pack(pady=10)

root.mainloop()