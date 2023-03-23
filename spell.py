import tkinter as tk
import random
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define the list of words to be used in the spelling bee
word_list = ["accrue", "accumulate", "advantageous","bureaucracy","camouflage","carburetor","changeable",
 "affiliate", "alchemy","allergenic", "chaperone","commodity","consonant",
"amateur", "amphibian", "apostrophe", "artificial",
 "atmosphere","automobile","auxiliary","bankruptcy","banquet","beautician","besiege","boulevard","bungalow","counterfeit","courageous","damageable","denominator",
 "desecration","desperately","disaster","disciplinary","dungeon","embryo","epitome","equation","exacerbate"]

# Define the function that will be called when the "Spell" button is clicked
def spell_word():
    # Randomly select a word from the list
    word = random.choice(word_list)
    # Say the word using the text-to-speech engine
    engine.say(word)
    engine.runAndWait()
    # Clear the user's previous answer
    answer_entry.delete(0, tk.END)
    # Save the current word as a global variable
    global current_word
    current_word = word

def check_answer():
    # Get the user's answer from the entry box
    user_input = answer_entry.get()
    # Get the word spoken by the computer
    word = current_word
    # Check if the user's input is correct
    if user_input.lower() == word:
        message = "You are right!"
    else:
        message = "You are wrong!"
    # Display the result of the spelling bee
    result_label.config(text=message)

# Create the main window
root = tk.Tk()
root.title("Spelling Bee")

# Set the window size
root.geometry("700x400")

# Create an entry box for the user's answer
answer_entry = tk.Entry(root)
answer_entry.pack()

# Create the "Spell" button
spell_button = tk.Button(root, text="Spell", command=spell_word)
spell_button.pack()

# Create the "Check" button
check_button = tk.Button(root, text="Check", command=check_answer)
check_button.pack()

# Create a label to display the result of the spelling bee
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
