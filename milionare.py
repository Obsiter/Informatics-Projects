import tkinter as tk
import random


class Milionare:
    def __init__(self, parent):
        self.bal = 0
        self.correct = 0
        self.answer = ""
        self.rewards = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
        self.restart_label = tk.Button(root, text = "Pokušaj ponovno!", width = 50, command = self.setup)
        self.setup()



        #Create your questions in a list object [question, answer(correct), random answer, random answer, random answer]
    def create_question(self):
        questions = [
            ["s koliko zemalja hrvatska graniči?", "6", "5", "8", "4"],
            ["koje godine započinje drugi svjetski rat?", "1939", "1938", "1941", "1945"],
            ["tko je napisao tekst hrvatske himne?", "antun mihanović", "runjanin josip", "ivo josipović", "august šenoa"],
            ["koja je površinom najveća svjetska zemlja?", "rusija", "kina", "amerika", "brazil"],
            ["gdje su održane prve olimpijske igre?", "grčka", "francuska", "engleska", "italija"],
            ["koliko nogu ima mrav?", "6", "4", "2", "8"],
            ["koji je najveći hrvatski otok?", "cres", "krk", "pag", "rab"],
            ["tko je otkrio ameriku?", "kristofer kolumbo", "amerigo vespucci", "james cook", "ferdinand magellan"],
            ["kako se zove osoba koja jezično-stilski uređuje rukopis?", "lektor", "urednik", "pisac", "režiser"],
            ["formula za izračun kruga?", "radius na kvadrat puta PI", "dva puta radius puta PI", "radius puta PI", "radius puta pi na kvadrat"],
            ["koji je najduži planinski lanac?", "ande", "velebit", "alpe", "ural"],
            ["najrašireniji kemijski element?", "kisik", "vodik", "željezo", "bakar"],
            ["kako se zvao prvi američki predsjednik?","george washington", "abraham lincoln", "bill clinton", "john adams"],
            ["koje nacionalnosti je bio josif v. staljin?", "gruzijac", "rus", "ukrajinac", "poljak"],
            ["koji astronaut je prvi zakoračio u svemir?", "jurij gagarin", "scot kelly", "neil amstrong", "michael collins"]
        ]
        data = questions[self.correct]
        question = data[0]
        self.answer = data[1]
        data.pop(0)
        fake = random.choice(data)
        data.remove(fake)
        fakeI = random.choice(data)
        data.remove(fakeI)
        fakeII = random.choice(data)
        data.remove(fakeII)
        fakeIII = data[0]
        return(question, fake, fakeI, fakeII, fakeIII)

        #Create widgets
    def create_layout(self, question, fake, fakeI, fakeII, fakeIII):
        question_label = tk.Label(root, text = question, width=50)
        button_one = tk.Button(root, text = fake, width=25, command = lambda: self.check_answer(self.firstAnswer))
        button_two = tk.Button(root, text = fakeI, width=25, command = lambda: self.check_answer(self.secondAnswer))
        button_three = tk.Button(root, text = fakeII, width=25, command = lambda: self.check_answer(self.thirdAnswer))
        button_four = tk.Button(root, text = fakeIII, width=25, command = lambda: self.check_answer(self.fourthAnswer))
        return(question_label, button_one, button_two, button_three, button_four)


    def setup(self, score=False):
        self.restart_label.grid_remove()
        if not score:
            self.score = tk.Label(root, text = "Money: " + str(self.bal), width = 50)
            self.score.grid(row=0, column=0, columnspan=2)
        else:
            self.score.config(text="Money: " + str(self.bal), width = 50)
            #create all the buttons
        self.question, self.firstAnswer, self.secondAnswer, self.thirdAnswer, self.fourthAnswer = self.create_question()
        self.question_label, self.firstAnswer_label, self.secondAnswer_label, self.thirdAnswer_label, self.fourthAnswer_label = self.create_layout(self.question, self.firstAnswer, self.secondAnswer, self.thirdAnswer, self.fourthAnswer)
        self.question_label.grid(row=1, column=0, columnspan=2)
        self.firstAnswer_label.grid(row=2, column=0)
        self.secondAnswer_label.grid(row=2, column=1)
        self.thirdAnswer_label.grid(row=3, column=0)
        self.fourthAnswer_label.grid(row=3, column=1)

    def check_answer(self, answer):
        if answer == self.answer:
            self.correct += 1
            self.bal = self.rewards[self.correct]
            if self.bal != 1000000:
                self.score.config(text="Novac: " + str(self.bal), width = 50)
                #remove questions and answers
                self.question_label.grid_remove()
                self.firstAnswer_label.grid_remove()
                self.secondAnswer_label.grid_remove()
                self.thirdAnswer_label.grid_remove()
                self.fourthAnswer_label.grid_remove()
                self.setup(self.score)
            else:
                self.score.config(text="Money: " + str(self.bal), width = 50)
                #remove questions and answers
                self.question_label.grid_remove()
                self.firstAnswer_label.grid_remove()
                self.secondAnswer_label.grid_remove()
                self.thirdAnswer_label.grid_remove()
                self.fourthAnswer_label.grid_remove()
                self.win = tk.Label(root, text = "YOU WON!!!", width=50)
                self.win.grid(row=1, column=0, columnspan=2)

        else:
            #adding retry button
            self.score.config(text="Izgubili ste.", width = 50)
            self.restart_label = tk.Button(root, text = "Try again!", width = 50, command = lambda: self.setup(self.score))
            self.restart_label.grid(row=1, column=0, columnspan=2)
            self.bal = 0
            self.score = 0
            self.correct = 0
            #remove questions and answers
            self.question_label.grid_remove()
            self.firstAnswer_label.grid_remove()
            self.secondAnswer_label.grid_remove()
            self.thirdAnswer_label.grid_remove()
            self.fourthAnswer_label.grid_remove()






root = tk.Tk()
root.title("Milionare")
milijunas = Milionare(root)
root.mainloop()
