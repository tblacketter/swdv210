from objects import TaskList, Task

S1 = "<20"
S2 = "<10"

def commandInterface():
    print("COMMAND MENU")
    print(f"{'list':{S2}}{'- List all tasks':{S1}}")
    print(f"{'add':{S2}}{'- Add a task':{S1}}")
    print(f"{'complete':{S2}}{'- Complete a task':{S1}}")
    print(f"{'delete':{S2}}{'- Delete a task':{S1}}")
    print(f"{'switch':{S2}}{'- Switch selected task list':{S1}}")
    print(f"{'exit':{S2}}{'- Exit program':{S1}}")
    print()

def displayTaskLists(taskLists:list):
    print("TASK LISTS")
    count = 1
    for tasklist in taskLists:
        print(f"{count}. {tasklist.description}")
        count += 1

def chooseList(taskList:list)->TaskList:

    while True:
        try:
            listChoice = int(input("Enter number to select task list: "))
            if listChoice >= 1 and listChoice <= len(taskList):
                chosenTaskList = taskList[listChoice-1]
                break
            else:
                print("Please enter a valid choice")
        except:
            print("Please enter a valid number")
        
    print(f"{chosenTaskList.description} task list was selected")
    return chosenTaskList

def getInput(tasklist:TaskList)->int:
    
    while True:
        try:
            taskNum = int(input("Number: "))

            if taskNum > len(tasklist.tasklist) or taskNum < len(tasklist.tasklist):
                print("Number is not on list please enter a valid number")
            else:
                return taskNum  
        except:
            print("Please enter a valid number")

def getTaskLists()->list:
    tempList = []
    with open("taskLists.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            tempTaskList = TaskList(line)
            tempTaskList.readTasksFromFile()
            tempList.append(tempTaskList)
    return tempList


def main():
    with open("taskLists.txt", "w") as file:
        file.write("Personal\n")
        file.write("Business\n")

    taskLists = getTaskLists()

    commandInterface()

    displayTaskLists(taskLists)
    chosenTaskList = chooseList(taskLists)

    while True:

        commandInput = input("Command: ")
    
        if(commandInput == "list"):
            chosenTaskList.displayList()
        elif(commandInput == "add"):
            chosenTaskList.addItem()
        elif(commandInput == "complete"):
            taskToComplete = getInput(chosenTaskList)
            chosenTaskList.completeTask(taskToComplete - 1)
        elif(commandInput == "delete"):
            taskToDelete = getInput(chosenTaskList)
            chosenTaskList.removeItem(taskToDelete)
        elif(commandInput == "switch"):
            chosenTaskList = chooseList(taskLists)
        elif(commandInput == "exit"):
            for tasks in taskLists:
                tasks.writeTasksToFile()
            exit()
        else:
            print("Invalid command Try again")


if __name__ == "__main__":
    main()