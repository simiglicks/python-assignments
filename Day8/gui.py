import tkinter as tk
from tkinter import messagebox
from random import randint

START = 1
STOP = 20


def guess_the_number(correct_num, user_guess):
    """
    Takes a correct number and a guess, and checks if the guess is correct.
    """
    if not user_guess.isdigit():
        return "Invalid input! Please enter a number."
    user_guess = int(user_guess)
    if user_guess < correct_num:
        return "Your guess was too small."
    elif user_guess > correct_num:
        return "Your guess was too big."
    else:
        return "correct"

# GUI Implementation
class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        self.correct_number = randint(START, STOP)
        self.guesses = 0

        # Create the widgets
        self.label = tk.Label(root, text=f"Guess a number between {START} and {STOP}:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_game)
        self.exit_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack(pady=10)

    def check_guess(self):
        user_guess = self.entry.get()
        if not user_guess:
            self.result_label.config(text="Please enter a number!")
            return

        self.guesses += 1
        result = guess_the_number(self.correct_number, user_guess)
        if result == "correct":
            messagebox.showinfo("Correct!", f"Your guess was exact! Total guesses: {self.guesses}")
            self.play_again()
        else:
            self.result_label.config(text=result)

    def show_answer(self):
        messagebox.showinfo("Answer", f"The correct number is {self.correct_number}")

    def exit_game(self):
        self.root.destroy()

    def play_again(self):
        play_again = messagebox.askyesno("Play Again", "Would you like to play again?")
        if play_again:
            self.correct_number = randint(START, STOP)
            self.guesses = 0
            self.result_label.config(text="")
            self.entry.delete(0, tk.END)  # delete the question dialog box
        else:
            self.exit_game()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()
