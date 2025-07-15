task = input("Enter Task Description: ")
priority = input("Enter task’s priority (high, medium, low): ")
time_bound = input("Is this task time-bound (yes or no): ")

match priority:
    case 'high':
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case 'medium':
        print(f"Reminder: {task} is a medium priority task that may be done later...!")
    case 'low':
        print(f'Reminder: {task} is a low priority task. Just do it if main ones, that matter are done.')

if time_bound == "no":
    print(f'Note: {task} is a low priority task. Just do it if main ones, that matter are done.')
else:
    print(f'Note: {task} can be done in the right time.')
