from tkinter import *

def show_end_screen(window, won, secret_word):
    # Clear the entire window
    for widget in window.winfo_children():
        widget.destroy()
    
    # Set background color
    bg_color = "#FFFACD" if won else "black"
    window.config(bg=bg_color)
    
    # Create end screen content
    main_text = "You saved him! He told me to thank you! XD" if won else "You Failed... He's dead now..."
    sub_text = f"The correct word was ==> {secret_word}"
    
    main_label = Label(window, text=main_text, font=("Arial", 24, "bold"),
                      bg=bg_color, fg="red" if not won else "pink")
    main_label.pack(expand=True)
    
    sub_label = Label(window, text=sub_text, font=("Arial", 12),
                     bg=bg_color, fg="gray" if won else "white")
    sub_label.pack(pady=10)
    
    # Add quit button at bottom
    quit_button = Button(window, text="Quit", command=window.destroy, 
                        font=("Arial", 12), bg=bg_color,
                        fg="red")
    quit_button.pack(pady=20)