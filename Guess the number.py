# Importing the tkinter module for creating a GUI and random module for generating a random number
import tkinter as tk
import random

# Initialize the global variable 'number' to None
number = None

# Define a function to guess the number
def guess_number():
   # Try to execute the following code
   try:
       # If 'number' is None, generate a random number within the range provided by the user
       if number is None:
           number = random.randint(int(start_textbox.get()), int(end_textbox.get()))
       # Get the user's guess and convert it to an integer
       guess = int(guess_textbox.get())
       # Check if the user's guess is greater than, less than, or equal to the random number
       if guess > number:
           output_textbox.insert(tk.END, "Hmmmm, try a lower number 📉\n")
       elif guess < number:
           output_textbox.insert(tk.END, "Go a little higher 📈 \n")
       elif guess == number:
           output_textbox.insert(tk.END, "Right on! Well done! 🥇\n")
           # Reset the value of 'number' to None and bring focus back to start_textbox
           number = None 
           start_textbox.focus() 
   # If a ValueError is raised, display an error message
   except ValueError:
       output_textbox.insert(tk.END, "Invalid input. you know what is a 'number' right? 😕🤔 \n")

# Define a function to start a new game
def new_game():
   # Reset the value of 'number' to None and clear all the text boxes and output text box
   global number
   number = None
   start_textbox.delete(0, tk.END)
   end_textbox.delete(0, tk.END)
   guess_textbox.delete(0, tk.END)
   output_textbox.delete(1.0, tk.END)
   start_textbox.focus() 

# Create a new tkinter window and set its title
root = tk.Tk()
root.title("Guess the Number")

# Create and place the range label, start text box, end label, end text box, guess label, guess text box, guess button, new game button, output label, and output text box
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

# Start the tkinter event loop
root.mainloop()
