import json


def load_progress():
    with open("data/progress.json", "r") as file:
        data = json.load(file)

    return data


def save_progress(question):
    data = load_progress()

    if question not in data["solved_questions"]:
        data["solved_questions"].append(question)

    with open("data/progress.json", "w") as file:
        json.dump(data, file, indent=4)


def get_total_solved():
    data = load_progress()
    return len(data["solved_questions"])