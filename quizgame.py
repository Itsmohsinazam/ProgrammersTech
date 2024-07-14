import tkinter as tk
from tkinter import messagebox

# Sample questions with multiple choices
questions = [
    ("What is the capital of Pakistan?", ["Islamabad", "London", "Berlin", "Madrid"], "Islamabad"),
    ("Who won the FIFA World Cup in 2022?", ["Brazil", "France", "England", "Argentina"], "Argentina"),
    ("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
    ("Which animal is known as the 'Ship of the Desert'?", ["Camel", "Tiger", "Lion", "Zebra"], "Camel"),
    ("What is the smallest prime number?", ["1", "2", "3", "5"], "2"),
]

# Initialize variables
current_question = 0
score = 0
time_limit = 10  # seconds
time_left = time_limit
timer_running = False

def update_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time left: {time_left}s")
        root.after(1000, update_timer)
    elif timer_running and time_left == 0:
        timer_running = False
        next_question()

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        update_timer()

def check_answer():
    global current_question, score, timer_running
    selected_answer = answer_var.get()
    correct_answer = questions[current_question][2]
    if selected_answer == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showinfo("Incorrect", f"The correct answer was {correct_answer}")
    next_question()

def next_question():
    global current_question, time_left
    current_question += 1
    if current_question < len(questions):
        time_left = time_limit
        load_question()
        start_timer()
    else:
        show_final_score()

def load_question():
    print(f"Loading question {current_question}")  # Debug print
    question, choices, _ = questions[current_question]
    question_label.config(text=question)
    for idx, choice in enumerate(choices):
        choice_rb[idx].config(text=choice, value=choice)
    answer_var.set(None)  # Reset the selected answer

def show_final_score():
    print("Showing final score...")  # Debug print
    if score == 5:
        question_label.config(text=f"Quiz over! Your final score is {score}/{len(questions)} \nExcellent, Keep it up!")
    elif 4 <= score >= 3:
        question_label.config(text=f"Quiz over! Your final score is {score}/{len(questions)} \nGood work, Better luck next time")
    else:
        question_label.config(text=f"Quiz over! Your final score is {score}/{len(questions)}, \nYou need lot of improvement")
    for rb in choice_rb:
        rb.pack_forget()
    submit_button.pack_forget()
    timer_label.pack_forget()

root = tk.Tk()
root.title("Quiz Game")

# Set window size and position (optional)
window_width = 300
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

print("Creating GUI elements...")  # Debug print

question_label = tk.Label(root, text="", wraplength=300)
question_label.pack(pady=20)

timer_label = tk.Label(root, text=f"Time left: {time_limit}s", wraplength=300)
timer_label.pack(pady=5)

answer_var = tk.StringVar()

choice_rb = [tk.Radiobutton(root, text="", variable=answer_var, value="") for _ in range(4)]
for rb in choice_rb:
    rb.pack(pady=5)

submit_button = tk.Button(root, text="Submit Answer", command=check_answer)
submit_button.pack(pady=20)

print("Starting GUI...")  # Debug print
load_question()
start_timer()

root.mainloop()
