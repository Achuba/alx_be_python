task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

run = True

while run:
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
            if time_bound == "yes":
                    reminder += " that requires immediate attention today!"
            else:
                reminder += ". Consider completing it as soon as possible."
            print(reminder)
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
            if time_bound == "yes":
                reminder += " that requires attention today!"
            else:
                reminder += ". Try to complete it soon."
            print(reminder)
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
            if time_bound == "yes":
                reminder += " that you might want to address today."
            else:
                reminder += ". You can do it whenever you have free time."
            print(reminder)
        case _:
            reminder = "Unrecognized priority level."
            print(reminder)
            break 


  
    run = False
