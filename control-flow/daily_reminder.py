task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):").lower()  # Convert input to lowercase

match priority:
    case "high":
        statement = "is a high priority task"
    case "medium":
        statement = "is medium priority task"
    case "low":
        statement = "is a low priority task"

if time_bound == "yes":
    print(f"Reminder: {task} {statement} that requires immediate attention today!")
else:
    print(f"Note: {task} {statement}. Consider completing it when you have free time")