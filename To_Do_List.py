tasks=[]

def addTask():
    task=input("Bro, Enter a task:")
    tasks.append(task)
    print(f"Task {task} added to the list.")

def listTask():
    if not tasks:
        print("There are not tasks currently.")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}.{task}")
def deleteTask():
    listTask()
    try:
        tasktodelete=eval(input("Enter the # to delete: "))
        if tasktodelete >= 0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"Task {tasktodelete} has been removed.")
        else:
            print(f"Task #{tasktodelete} was not found")
    except:
        print("Invalid input.")  

if __name__ == "__main__":
    print("Welcome to the To Do List app:")
    while True:
        print("/n")
        #print("What would you like to do?")
        print("Please select one of the following options")
        print("-------------------------------------------")
        print("1, Add a new task")
        print("2, Delect a task")
        print("3, List out tasks")
        print("4, Quit")
        choice=input("Enter your choice: ")
        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTask()
        elif (choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")

print("Good Bye friends........")