tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# ### MVP

# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks
def completed():
    for task in tasks:
        if task["completed"] == False:
             print(f"{task['description']} was uncompleted. Please complete the task.")
completed()


# 2. Print a list of completed tasks
def completed():
    for task in tasks:
        if task["completed"] == True:
             print(f"{task['description']} was completed. Good job!.")
completed()

# 3. Print a list of all task descriptions
def descriptions():
    for task in tasks:
        print(task["description"])
descriptions()
#4. Print a list of tasks where time_taken is at least a given time ##Let's say 15 minutes
def times():
    for task in tasks:
        if task["time_taken"] >= 45:
            print("It takes more than 45 minutes to complete this task")
times()

# time_taken = tasks[1]["time_taken"]
# print(time_taken)
# 5. Print any task with a given description
def first_task():
    print(f"The first task for today is {tasks[1]['description']}")
first_task()


# ### Extension

# 6. Given a description update that task to mark it as complete.
def update():
    for task in tasks:
        if task["completed"] == False and task["time_taken"] <= 5:
            task["completed"] = True
update()
print(tasks)

# 7. Add a task to the list
tasks.append( {"description": "Workout", "completed": True, "time_taken": 180 })
print(tasks)

# ### Further Extensions

#8. Use a while loop to display the following menu and allow the use to enter an option.

def menu(user_choice):
    #user_logged_in = True
    #user_choice = input("Please press the button ")
    user_choice.
    while (user_choice == range(7) or user_choice == 'p'):
    #for choice in user_choice:
        if user_choice == 0:
            print("Menu:")
        elif user_choice == 1:
            print("1: Display All Tasks")
        elif user_choice == 2:
            print("2: Display Uncompleted Tasks")
        elif user_choice == 3:
            print("3: Display Completed Tasks")
        elif user_choice == 4:
            print("4: Mark Task as Complete")
        elif user_choice == 5:
            print("5: Get Tasks Which Take Longer Than a Given Time")
        elif user_choice == 6:
            print("6: Find Task by Description")
        elif user_choice == 7:
            print("7: Add a new Task to list")
        elif user_choice == 'M' or user_choice == 'm':
            print("M or m: Display this menu")
        elif user_choice == 'Q' or user_choice == 'q':
            print("Q or q: Quit")
        else:
            print("Wrong input")
    #break
menu(1)

#9. Call the appropriate function depending on the users choice.