import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.geometry('500x420')
root.title("Paramètres Mode Solo")

# Variables
player_name = tk.StringVar()
difficulty = tk.StringVar()
language = tk.StringVar()

# Main Frame
main_frame = tk.Frame(root)
main_frame.pack(expand=True)

# Widgets in the main frame
tk.Label(main_frame, text="Nom du joueur: ").grid(row=0, column=0, sticky="w")
tk.Entry(main_frame, textvariable=player_name).grid(row=0, column=1)

tk.Label(main_frame, text="Difficulté: ").grid(row=1, column=0, sticky="w")
difficulty_options = ["Facile", "Normal", "Difficile"]
tk.OptionMenu(main_frame, difficulty, *difficulty_options).grid(row=1, column=1)

tk.Label(main_frame, text="Language:").grid(row=2, column=0, sticky="w")
language_options = ["Français", "English"]
tk.OptionMenu(main_frame, language, *language_options).grid(row=2, column=1)

# Submit Button Action
def submit_action():
    print(f"Player Name: {player_name.get()}")
    print(f"Difficulty: {difficulty.get()}")
    print(f"Language: {language.get()}")

tk.Button(main_frame, text="Submit", command=submit_action).grid(row=3, column=0, columnspan=2)

# Main loop
root.mainloop()
