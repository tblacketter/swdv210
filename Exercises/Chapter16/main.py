from objects import TaskList, Task

S1 = "<20"
S2 = "<10"

personalTaskList = TaskList("Personal")
businessTaskList = TaskList("Business")

def commandInterface():
    print("COMMAND MENU")
    print(f"{'list':{S2}}{'- List all tasks':{S1}}")
    print(f"{'add':{S2}}{'- Add a task':{S1}}")
    print(f"{'complete':{S2}}{'- Complete a task':{S1}}")
    print(f"{'delete':{S2}}{'- Delete a task':{S1}}")
    print(f"{'switch':{S2}}{'- Switch selected task list':{S1}}")
    print(f"{'exit':{S2}}{'- Exit program':{S1}}")

def displayTaskLists():
    print(f"1. {personalTaskList.description}")
    print(f"2. {businessTaskList.description}")

def chooseList()->TaskList:

    while True:
        
        listChoice = int(input("Enter number to select task list: "))

        if listChoice == 1:
            chosenTaskList = personalTaskList
            break
        elif listChoice == 2:
            chosenTaskList = businessTaskList
            break
        else:
            print("Please enter a valid choice")
        
    print(f"{chosenTaskList.description} task list was selected")
    return chosenTaskList

def main():
    commandInterface()

    displayTaskLists()
    chosenTaskList = chooseList()

    while True:

        commandInput = input("Command: ")
    
        if(commandInput == "list"):
            chosenTaskList.displayList()
        elif(commandInput == "add"):
            chosenTaskList.addItem()
        elif(commandInput == "complete"):
            taskToComplete = int(input("Number: "))
            chosenTaskList.completeTask(taskToComplete - 1)
        elif(commandInput == "delete"):
            taskToDelete = int(input("Number: "))
            chosenTaskList.removeItem(taskToDelete)
        elif(commandInput == "switch"):
            chosenTaskList = chooseList()
        elif(commandInput == "exit"):
            exit()
        else:
            print("Invalid command Try again")


if __name__ == "__main__":
    main()