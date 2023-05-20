import tkinter as tk
from src.word_frequency_analyzer import WordFrequencyAnalyzer

def start():
    input_string = text.get("1.0", tk.END).strip()
    result = WordFrequencyAnalyzer(input_string)
    highest_frequency.config(text=str(result.result))
    for count,word in enumerate(result.word_counts):
        unique_words.insert(tk.END, str(count+1)+ ".  " + str(word) + ' : ' + str(result.word_counts[word])+ "\n")

# Create the main window
window = tk.Tk()
window.geometry("800x600")
window.title("Word Frequency Analyzer")

label = tk.Label(window, text="Enter the String to Analyze")
label.pack()

text = tk.Text(window, font=("Arial", 12), height=10, width=90) 
text.pack()


button = tk.Button(window, text="Submit", command=start)
button.pack()


highest_frequency = tk.Label(window, text="Result:", wraplength=500)
highest_frequency.pack()

unique_words = tk.Text(window, font=("Arial", 12), height=10, width=60)
unique_words.pack()


window.mainloop()