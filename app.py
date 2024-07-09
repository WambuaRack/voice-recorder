import tkinter as tk
import emoji

def emoji_to_text(input_text):
    return emoji.demojize(input_text)

def convert_emoji():
    input_text = entry.get()
    converted_text = emoji_to_text(input_text)
    result_label.config(text=converted_text)

# Create the main window
root = tk.Tk()
root.title("Emoji to Text Converter")

# Create GUI components
label = tk.Label(root, text="Enter text with emojis:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_emoji)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main loop aefcesav
root.mainloop()
