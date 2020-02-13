from tkinter import *
import os
import random


class GuessCorrect:
    def __init__(self, parent):
        self.score = 0
        self.start = True
        self.gifs = []
        self.correct = 0
        self.path = "."
        self.answer = ""
        self.load_gifs()
        self.setup()

    def show_images(self):
        self.img_label_one = Label(root, width = 300, height=300)
        self.img_label_one.image = PhotoImage(file=self.gif_one)
        self.img_label_one['image'] = self.img_label_one.image
        self.img_label_one.grid(row=2, column=0)
        self.img_label_two = Label(root, width = 300, height=300)
        self.img_label_two.image = PhotoImage(file=self.gif_two)
        self.img_label_two['image'] = self.img_label_two.image
        self.img_label_two.grid(row=2, column=1)

    def load_gifs(self):
        for file in os.listdir(self.path):
            if file.endswith(".gif"):
                self.gifs.append(file)

    def select_gifs(self):
        self.gif_one = random.choice(self.gifs)
        self.gif_two = random.choice(self.gifs)
        list = [self.gif_one, self.gif_two]
        self.answer = random.choice(list).split(".")[0]

    def check_answer(self, option):
        if self.answer == option:
            self.correct += 1
            self.score += self.correct * 10
            self.setup()
        else:
            self.correct = 0
            self.score = 0
            self.setup()

    def setup(self):
        if self.start:
            self.score_label = Label(root, text="Score: " + str(self.score))
            self.load_gifs()
            self.select_gifs()
            self.answer_label = Label(root, text= self.answer)
            self.option_one = Button(root, text = "Odaberi!", width = 50, command = lambda: self.check_answer(self.gif_one.split(".")[0]))
            self.option_two = Button(root, text = "Odaberi!", width = 50, command = lambda: self.check_answer(self.gif_two.split(".")[0]))
            self.score_label.grid(row = 0, columnspan = 2 )
            self.answer_label.grid(row = 1, columnspan = 2)
            self.show_images()
            self.option_one.grid(row = 3, column = 0 )
            self.option_two.grid(row = 3, column = 1 )
        else:
            self.score_label.grid_forget()
            self.score_label = Label(text = "Score: " + str(self.score))
            self.score_label.grid(row = 0, columnspan = 2)
            self.img_label_one.grid_forget()
            self.img_label_two.grid_forget()
            self.select_gifs()
            self.show_images()
            self.answer_label.grid_forget()
            self.answer_label = Label(root, text= self.answer)
            self.answer_label.grid(row = 1, columnspan = 2)



root = Tk()
root.title("Pogodi")
Pogodi = GuessCorrect(root)
root.mainloop()
