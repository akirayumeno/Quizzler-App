from distutils.core import setup_keywords
from tkinter import Tk, Canvas, Label, Image, PhotoImage, Button
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.config(padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=270, text="some question text", font=("Arial", 20, "italic"), anchor="center", fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.right_answer_next_question)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.wrong_answer_next_question)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def wrong_answer_next_question(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def right_answer_next_question(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_correct):
        if not is_correct:
            self.canvas.config(bg="#FA7070")
        else:
            self.canvas.config(bg="#B3D8A8")
        self.window.after(1000, self.get_next_question)





