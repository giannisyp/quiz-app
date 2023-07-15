from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_button)
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_button)
        self.false_button.grid(column=1, row=2)
        self.true_button.grid(column=0, row=2)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280 )
        self.canvas.grid(column=0,row=1, columnspan=2,padx=20, pady=20)
        self.label = Label(text="Score : 0", bg=THEME_COLOR)
        self.label.grid(column=1, row=0,padx=10, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)


