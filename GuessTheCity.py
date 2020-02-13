from tkinter import *
import os
import random


class GuessTheCity:
    def __init__(self, parent):
        self.score = 0
        self.start = True
        self.pairs = [
            "Albanija - Tirana",
            "Andora - Andora la Velja",
            "Austrija - Beč",
            "Belgija - Brisel",
            "Belorusija - Minsk",
            "Bosna i Hercegovina - Sarajevo",
            "Grčka - Atena",
            "Danska - Kopenhagen",
            "Estonija - Talin",
            "Island - Rejkjavik",
            "Hrvatska - Zagreb",
            "Jermenija - Jerevan",
            "Letonija - Riga",
            "Moldavija - Kišinjev",
            "Nemačka - Berlin",
            "Monako - Monako",
            "Mađarska - Budimpešta",
            "Poljska - Varšava",
            "Norveška - Oslo",
            "Srbija - Beograd",
            "Slovačka - Bratislava",
            "Slovenija - Ljubljana",
            "Vatikan - Vatikan",
            "Ukrajina - Kijev",
            "San Marino - San Marino",
            "Rumunjska - Bukurešt",
            "Makedonija - Skopje",
            "Litvanija - Vilnjus",
            "Luksemburg - Luksemburg",
            "Francuska - Pariz",
            "Finska - Helsinki",
            "Češka - Prag",
            "Crna Gora - Podgorica"
        ]
        self.correct = 0
        self.answer = ""
        self.question = ""
        self.setup()


    def set_pair(self):
        self.question, self.answer = self.pairs[random.randint(0,len(self.pairs))].split(" - ")




    def check_answer(self, answer):
        if self.answer.lower() == answer.lower():
            self.correct += 1
            self.score += self.correct * 10
            self.setup()
        else:
            self.correct = 0
            self.score = 0
            self.setup()

    def setup(self):
        if self.start:
            self.set_pair()
            self.score_label = Label(root, text="Score: " + str(self.score))
            self.question_label = Label(root, text="Koji je glavni grad države: {}?".format(self.question))
            self.entry = Entry(root, width=55, borderwidth=3)
            self.answer_button = Button(root, text = "Odgovori!", width = 50, command = lambda: self.check_answer(self.entry.get()))
            self.score_label.grid(row = 0, columnspan = 3)
            self.question_label.grid(row = 1, columnspan = 3)
            self.entry.grid(row = 2, column = 2)
            self.answer_button.grid(row = 3, column = 2 )
            self.start = False
        else:
            self.set_pair()
            self.score_label.grid_forget()
            self.score_label = Label(root, text = "Score: " + str(self.score))
            self.score_label.grid(row = 0, columnspan = 3)
            self.question_label.grid_forget()
            self.question_label = Label(root, text= "Koji je glavni grad države: {}?".format(self.question))
            self.question_label.grid(row = 1, columnspan = 3)
            self.entry.delete(0, END)



root = Tk()
root.title("Pogodi Glavni Grad")
Pogodi = GuessTheCity(root)
root.mainloop()
