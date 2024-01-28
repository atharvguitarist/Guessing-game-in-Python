import tkinter as tk
import random

number = None

def guess_number():
    global number
    try:
        if number is None:
            number = random.randint(int(start_textbox.get()), int(end_textbox.get()))
        guess = int(guess_textbox.get())
        if guess > number:
            output_textbox.insert(tk.END, "Hmmmm, try a lower number 📉\n")
        elif guess < number:
            output_textbox.insert(tk.END, "Go a little higher 📈 \n")
        elif guess == number:
            output_textbox.insert(tk.END, "Right on! Well done! 🥇\n")
            number = None 
            start_textbox.focus() # bring focus back to start_textbox
    except ValueError:
        output_textbox.insert(tk.END, "Invalid input. you know what is a 'number' right? 😕🤔 \n")

def new_game():
    global number
    number = None
    start_textbox.delete(0, tk.END)
    end_textbox.delete(0, tk.END)
    guess_textbox.delete(0, tk.END)
    output_textbox.delete(1.0, tk.END)
    start_textbox.focus()

root = tk.Tk()
root.title("Guess the Number")

start_label = tk.Label(root, text="Range of Random Numbers:")
start_label.grid(row=0, column=0, pady=5)
start_textbox = tk.Entry(root)
start_textbox.grid(row=0, column=1, pady=5)

end_label = tk.Label(root, text="to")
end_label.grid(row=0, column=2, pady=5)
end_textbox = tk.Entry(root)
end_textbox.grid(row=0, column=3, pady=5)

guess_label = tk.Label(root, text="Enter your guess:")
guess_label.grid(row=1, column=0, pady=5)
guess_textbox = tk.Entry(root)
guess_textbox.grid(row=1, column=1, pady=5)

guess_button = tk.Button(root, text="Guess", command=guess_number)
guess_button.grid(row=1, column=2)

new_game_button = tk.Button(root, text="New Game", command=new_game, height = 1, padx=5)
new_game_button.grid(row=2, column=3, pady=4)

output_label = tk.Label(root, text="      Output:")
output_label.grid(row=2, column=0, sticky= tk.W)
output_textbox = tk.Text(root, height=10, width=50)
output_textbox.grid(row=3, column=0, columnspan=4)

root.mainloop()