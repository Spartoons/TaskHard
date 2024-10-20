# Task management logic (input, categorization, scheduling)

def capture_tasks():
    tasks = []
    while True:
        task = input("Enter a new task or 'exit' to finish: ")
        if task.lower() == "exit":
            break
        tasks.append(task)
    return tasks

def categorize_tasks(tasks):
    categorized_tasks = {"urgent_important": [], "not_urgent_important": [], "urgent_not_important": [], "not_urgent_not_important": []}

    for task in tasks:
        urgency = input(f"Is the task '{task}' urgent? (yes/no): ").lower()
        importance = input(f"Is the task '{task}' important? (yes/no): ").lower()

        if urgency == "yes" and importance == "yes":
            categorized_tasks["urgent_important"].append(task)
        elif urgency == "no" and importance == "yes":
            categorized_tasks["not_urgent_important"].append(task)
        elif urgency == "yes" and importance == "no":
            categorized_tasks["urgent_not_important"].append(task)
        else:
            categorized_tasks["not_urgent_not_important"].append(task)

    return categorized_tasks

def display_tasks(categorized_tasks):
    for category, tasks in categorized_tasks.items():
        print(f"Category: {category}")
        for task in tasks:
            print(f" - {task}")
