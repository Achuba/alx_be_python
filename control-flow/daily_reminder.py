task = input ("Enter your task:  ")
priority = input ("Priority (high/medium/low): ") 
time_bound = input ("Is it time-bound? (yes/no): ")
 
match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            time_bound_yes = (f"'Finish project report' is a {priority} task that requires immediate attention today!")
            print (time_bound_yes)
        else : 
            time_bound_no = (f"Read a book' is a {priority} task. Consider completing it when you have free time.")
            print (time_bound_no)
    case "medium":
        if time_bound.lower() == "yes":
            time_bound_yes = (f"'Finish project report' is a {priority} task that requires immediate attention today!")
            print (time_bound_yes)
        else : 
            time_bound_no = (f"Read a book' is a {priority} task. Consider completing it when you have free time.")
            print (time_bound_no)
    case "low":
        if time_bound.lower() == "yes":
            time_bound_yes = (f"'Finish project report' is a {priority} task that requires immediate attention today!")
            print (time_bound_yes)
        else : 
            time_bound_no = (f"Read a book' is a {priority} task. Consider completing it when you have free time.")
            print (time_bound_no)
    case _:
    
        priority_level = 4 
        print ("Unrecognized priority level. Please use high, medium, or low.")


