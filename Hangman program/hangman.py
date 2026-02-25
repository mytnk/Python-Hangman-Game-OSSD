import random
from tkinter import *
from hangman_figure import draw_hangman
from hangman_endScreen import show_end_screen
from hangman_helpers import create_letter_buttons, update_word_display, disable_all_buttons

class HangmanGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Hangman Game")
        
        # Game variables
        self.words = [
    "Schadenfreude", "Bittersweet", "Euphoria", "Despair", "Sonder",
    "Anxiety", "Jealousy", "Bliss", "Awe", "Trepidation",
    "Saudade", "Whimsy", "Frenzy", "Giddy", "Zen",
    "Amusement", "Dread", "Nostalgia", "Guilt", "Enthusiasm",
    "Compersion", "Wanderlust", "Pride", "Regret", "Optimism",
    "Melancholy", "Bewilderment", "Triumph", "Shame", "Apathy",
    "Empathy", "Ambivalence", "Resentment", "Bitterness", "Panic",
    "Agony", "Misery", "Envy", "Frustration", "Serenity",
    "Gratitude", "Excitement", "Confidence", "Satisfaction", "Calm",
    "Hope", "Loneliness", "Disgust", "Fear", "Angry",
    "Sad", "Happy", "Love", "Hate", "Joy",
    "Pain", "Butterflies", "Heartache", "Warmth", "Chills"
]
        self.secret_word = random.choice(self.words).lower() # lowercase for consistency
        self.guessed_letters = set()
        self.tries = 10
        self.letter_buttons = {}
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create frames for left and right layout
        self.left_frame = Frame(self.window)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.right_frame = Frame(self.window)
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        mission_label = Label(self.left_frame, 
                            text="This is your mission. Save the hangman by guessing the emotion he's feeling :) \nhint: He's a little weird and unpreditable so it can be any emotion, literally.",
                            font=("Arial", 10, "italic"))
        mission_label.pack(pady=10)

        # Create UI elements for left frame
        self.word_label = Label(self.left_frame, text="_ " * len(self.secret_word), font=("Arial", 24))
        self.word_label.pack(pady=20)
        self.tries_label = Label(self.left_frame, text=f"Tries left: {self.tries}", font=("Arial", 12))
        self.tries_label.pack()
        self.message_label = Label(self.left_frame, text="", font=("Arial", 12))
        self.message_label.pack(pady=10)

        # Create letter buttons
        create_letter_buttons(self.left_frame, self.letter_buttons, self.make_guess)

        # Add quit button
        quit_button = Button(self.left_frame, text="Quit", command=self.window.destroy, font=("Arial", 12), fg="red")
        quit_button.pack(pady=20)

        # Create canvas in right frame
        self.canvas = Canvas(self.right_frame, width=450, height=650, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)

        # Initial drawing
        draw_hangman(self.canvas, self.tries)
        
    def make_guess(self, letter):
        # Ignore if already guessed or game over
        if letter in self.guessed_letters or self.tries <= 0:
            return
        
        self.guessed_letters.add(letter)
        self.letter_buttons[letter].config(state=DISABLED)
        
        if letter not in self.secret_word:
            self.tries -= 1
            self.tries_label.config(text=f"Tries left: {self.tries}")
            draw_hangman(self.canvas, self.tries)
            self.message_label.config(text="Incorrect!")
        else:
            self.message_label.config(text="Correct!") 
        
        
        # Update word display
        current_display = update_word_display(self.word_label, self.secret_word, self.guessed_letters)
        
        # Check game status
        if "_" not in current_display:
            show_end_screen(self.window, True, self.secret_word)
        elif self.tries <= 0:
            show_end_screen(self.window, False, self.secret_word)

if __name__ == "__main__":
    window = Tk()
    game = HangmanGame(window)
    window.mainloop()