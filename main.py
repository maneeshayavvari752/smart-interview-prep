import tkinter as tk
from tkinter import messagebox
import json
from roadmap import generate_roadmap
from recommender import recommend_questions, get_company_focus
from progress import save_progress, load_progress, get_total_solved
from data_manager import generate_schedule


recommended_questions = []


# ---------------- FUNCTIONS ---------------- #

def mark_question_solved():
    question = selected_question.get()

    if question != "Select Question":
        save_progress(question)
        output_box.insert(tk.END, f"\n✓ Marked as solved: {question}\n")


def show_progress():
    progress_data = load_progress()

    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END, "SOLVED QUESTIONS\n")
    output_box.insert(tk.END, "===============================\n\n")

    for question in progress_data["solved_questions"]:
        output_box.insert(tk.END, f"• {question}\n")


def show_analytics():
    total_solved = get_total_solved()

    try:
        with open("data/user_data.json", "r") as file:
            user_data = json.load(file)
    except:
        messagebox.showerror("Error", "Generate a study plan first.")
        return

    name = user_data.get("name", "Unknown")
    company = user_data.get("company", "Unknown")
    hours = user_data.get("hours", "Unknown")
    topics = user_data.get("topics", [])

    if total_solved < 3:
        level = "Beginner"
    elif total_solved < 7:
        level = "Intermediate"
    else:
        level = "Advanced"

    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END, "ANALYTICS DASHBOARD\n")
    output_box.insert(tk.END, "===============================\n\n")

    output_box.insert(tk.END, f"Name: {name}\n")
    output_box.insert(tk.END, f"Target Company: {company}\n")
    output_box.insert(tk.END, f"Study Hours/Day: {hours}\n")
    output_box.insert(tk.END, f"Weak Topics Count: {len(topics)}\n")
    output_box.insert(tk.END, f"Total Solved Questions: {total_solved}\n")
    output_box.insert(tk.END, f"Completion Level: {level}\n")


def update_dropdown(questions):
    menu = question_dropdown["menu"]
    menu.delete(0, "end")

    for question in questions:
        menu.add_command(
            label=question,
            command=tk._setit(selected_question, question)
        )

    selected_question.set("Select Question")


def generate_plan():
    global recommended_questions

    name = name_entry.get().strip()
    company = company_entry.get().strip()
    hours = hours_entry.get().strip()
    topics = topics_entry.get().strip()

    if not name or not company or not hours or not topics:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    if not hours.isdigit():
        messagebox.showerror("Input Error", "Study hours must be a number.")
        return

    topic_list = topics.split(",")

    user_data = {
        "name": name,
        "company": company,
        "hours": hours,
        "topics": topic_list
    }

    with open("data/user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)

    roadmap = generate_roadmap(topic_list)
    recommended_questions = recommend_questions(topic_list)
    company_focus = get_company_focus(company)
    schedule = generate_schedule(hours)

    update_dropdown(recommended_questions)

    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END, "PERSONALIZED STUDY ROADMAP\n")
    output_box.insert(tk.END, "===============================\n\n")

    for item in roadmap:
        output_box.insert(tk.END, f"• {item}\n")

    output_box.insert(tk.END, "\nDAILY STUDY SCHEDULE\n")
    output_box.insert(tk.END, "===============================\n\n")

    for i, task in enumerate(schedule, start=1):
        output_box.insert(tk.END, f"Hour {i} → {task}\n")

    output_box.insert(tk.END, "\nCOMPANY FOCUS AREAS\n")
    output_box.insert(tk.END, "===============================\n\n")

    for item in company_focus:
        output_box.insert(tk.END, f"• {item}\n")

    output_box.insert(tk.END, "\nRECOMMENDED QUESTIONS\n")
    output_box.insert(tk.END, "===============================\n\n")

    for question in recommended_questions:
        output_box.insert(tk.END, f"• {question}\n")


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Smart Interview Preparation Engine")
root.geometry("1100x900")
root.configure(bg="#1e1e2f")


main_frame = tk.Frame(root, bg="#2d2d44", padx=30, pady=20)
main_frame.pack(pady=20)


heading = tk.Label(
    main_frame,
    text="Smart Interview Preparation Engine",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#2d2d44"
)
heading.pack(pady=20)


def create_label(text):
    return tk.Label(
        main_frame,
        text=text,
        font=("Segoe UI", 11),
        fg="white",
        bg="#2d2d44"
    )


def create_entry():
    return tk.Entry(
        main_frame,
        width=35,
        font=("Segoe UI", 11)
    )


create_label("Enter Your Name").pack()
name_entry = create_entry()
name_entry.pack(pady=8)

create_label("Target Company").pack()
company_entry = create_entry()
company_entry.pack(pady=8)

create_label("Study Hours Per Day").pack()
hours_entry = create_entry()
hours_entry.pack(pady=8)

create_label("Weak DSA Topics (comma separated)").pack()
topics_entry = create_entry()
topics_entry.pack(pady=8)


generate_button = tk.Button(
    main_frame,
    text="Generate Plan",
    command=generate_plan,
    font=("Segoe UI", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20
)
generate_button.pack(pady=15)


create_label("Select Solved Question").pack()

selected_question = tk.StringVar(root)
selected_question.set("Select Question")

question_dropdown = tk.OptionMenu(main_frame, selected_question, "Select Question")
question_dropdown.config(
    width=30,
    font=("Segoe UI", 10),
    bg="white"
)
question_dropdown.pack(pady=10)


button_frame = tk.Frame(main_frame, bg="#2d2d44")
button_frame.pack(pady=10)


mark_button = tk.Button(
    button_frame,
    text="Mark Solved",
    command=mark_question_solved,
    font=("Segoe UI", 10, "bold"),
    bg="#2196F3",
    fg="white",
    width=15
)
mark_button.grid(row=0, column=0, padx=10)


progress_button = tk.Button(
    button_frame,
    text="View Progress",
    command=show_progress,
    font=("Segoe UI", 10, "bold"),
    bg="#FF9800",
    fg="white",
    width=15
)
progress_button.grid(row=0, column=1, padx=10)


analytics_button = tk.Button(
    button_frame,
    text="Analytics",
    command=show_analytics,
    font=("Segoe UI", 10, "bold"),
    bg="#9C27B0",
    fg="white",
    width=15
)
analytics_button.grid(row=0, column=2, padx=10)


output_box = tk.Text(
    root,
    width=100,
    height=22,
    font=("Consolas", 11),
    bg="#121212",
    fg="#00FF99",
    insertbackground="white"
)
output_box.pack(pady=20)


root.mainloop()