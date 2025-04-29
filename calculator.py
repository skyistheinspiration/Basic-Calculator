import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x550")  # Set the size of the window

# Set the background color
root.config(bg="#f0f0f0")

# Create an entry widget for the display
display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#fff", fg="#000")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Initialize memory
memory = 0

# Function to update the display when a button is clicked
def button_click(char):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + char)

# Function to clear the display
def button_clear():
    display.delete(0, tk.END)

# Function to calculate the result
def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Cannot divide by zero")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function for square root
def button_sqrt():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except ValueError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function for power (x^y)
def button_power():
    try:
        numbers = display.get().split("^")
        if len(numbers) == 2:
            base, exponent = float(numbers[0]), float(numbers[1])
            result = base ** exponent
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        else:
            display.delete(0, tk.END)
            display.insert(tk.END, "Invalid power format")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to store a number in memory
def button_memory_store():
    global memory
    try:
        memory = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, "Memory Saved")
    except ValueError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to recall memory
def button_memory_recall():
    global memory
    display.delete(0, tk.END)
    display.insert(tk.END, str(memory))

# Button Layout (Numbers 0-9, Operators, and Advanced Functions)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('^', 4, 3),  # Power button
    ('C', 5, 0), ('√', 5, 1), ('=', 5, 2), ('M', 5, 3),  # M: Memory store
    ('MR', 6, 0)  # MR: Memory recall
]

# Create the buttons and add them to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), command=button_equal, bg="#4CAF50", fg="white")
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), command=button_clear, bg="#f44336", fg="white")
    elif text == "√":
        button = tk.Button(root, text=text, font=("Arial", 18), command=button_sqrt, bg="#2196F3", fg="white")
    elif text == "^":
        button = tk.Button(root, text=text, font=("Arial", 18), command=button_power, bg="#FF9800", fg="white")
    elif text == "M":
        button = tk.Button(root, text=text, font=("Arial", 18), command=button_memory_store, bg="#9C27B0", fg="white")
    elif text == "MR":
        button = tk.Button(root, text=text, font=("Arial", 18), command=button_memory_recall, bg="#009688", fg="white")
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda char=text: button_click(char), bg="#E0E0E0", fg="black")
    
    button.grid(row=row, column=col, ipadx=20, ipady=20, sticky="nsew", padx=5, pady=5)

# Make all buttons stretch to fill the available space
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop()
