from tkinter import *
from hangman_figure import draw_hangman
from hangman_endScreen import show_end_screen

def create_letter_buttons(left_frame, letter_buttons, make_guess):
    # Create a frame to hold all letter buttons
    letters_frame = Frame(left_frame)
    letters_frame.pack(pady=10)
    
    # Create buttons for each letter A-Z
    for i in range(26):
        letter = chr(ord('a') + i)
        btn = Button(letters_frame, text=letter.lower(), width=3, height=1,
                    command=lambda l=letter: make_guess(l))
        btn.grid(row=i//7, column=i%7, padx=2, pady=2)
        letter_buttons[letter] = btn

def update_word_display(word_label, secret_word, guessed_letters):
    display = []
    # Create a display of the word with guessed letters revealed
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    word_label.config(text=" ".join(display))
    return display

def disable_all_buttons(letter_buttons):
    for btn in letter_buttons.values():
        btn.config(state=DISABLED)