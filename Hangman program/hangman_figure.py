from tkinter import *

def draw_hangman(canvas, tries_left):
    canvas.delete("all") 
    # Draw the hangman progressively based on remaining tries
    canvas.create_line(50, 600, 400, 600, width=8)  # Ground
    if tries_left < 10:
        canvas.create_line(320, 50, 320, 600, width=5)  # Pole
    if tries_left < 9:
        canvas.create_line(100, 50, 350, 50, width=5)  # Top bar
    if tries_left < 8:
        canvas.create_line(220, 50, 320, 150, width=5)  # Support
    if tries_left < 7:
        canvas.create_line(120, 50, 120, 100, width=3)  # String
    if tries_left < 6:
        canvas.create_oval(80, 100, 160, 175, width=5)  # Head
    if tries_left < 5:
        canvas.create_line(120, 175, 120, 400, width=5)  # Body
    if tries_left < 4:
        canvas.create_line(120, 175, 200, 300, width=5)  # Right hand
    if tries_left < 3:
        canvas.create_line(120, 175, 40, 300, width=5)  # Left hand
    if tries_left < 2:
        canvas.create_line(120, 400, 200, 530, width=5)  # Right leg
    if tries_left < 1:
        canvas.create_line(120, 400, 40, 530, width=5)  # Left leg
