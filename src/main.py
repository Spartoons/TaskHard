# Entry point for the application

from tasks import capture_tasks, categorize_tasks, display_tasks
from pomodoro import start_pomodoro
from review import review_tasks

def main():
    print("Welcome to the Task Management Tool")

    tasks = []

    while True:
        choice = input("Choose an option: 1) Add Task 2) View Tasks 3) Start Pomodoro 4) Review Tasks 5) Exit: ")

        if choice == "1":
            tasks.extend(capture_tasks())  # Add tasks to the existing list
        elif choice == "2":
            categorized_tasks = categorize_tasks(tasks)
            display_tasks(categorized_tasks)
        elif choice == "3":
            selected_task = input("Enter the task to focus on: ")
            start_pomodoro(selected_task)
        elif choice == "4":
            review_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
