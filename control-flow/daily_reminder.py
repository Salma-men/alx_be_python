# daily_reminder.py

def daily_task_reminder():
        # Prompting user for input
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        # Validate priority input
        if priority not in ["high", "medium", "low"]:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

        # Validate time-bound input
        if time_bound not in ["yes", "no"]:
            print("Invalid time-bound response. Please enter yes or no.")
            return

        # Process task based on priority
        match priority:
            case "high":
                reminder = f"'{task}' is a high priority task."
            case "medium":
                reminder = f"'{task}' is a medium priority task."
            case "low":
                reminder = f"'{task}' is a low priority task."

        # Modify reminder if time-bound
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
        else:
            reminder += " Consider completing it when you have free time."

        # Print the reminder
        print(f"Reminder: {reminder}")