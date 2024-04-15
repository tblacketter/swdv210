from dataclasses import dataclass

@dataclass
class Task:
    description:str 
    completion:bool 

    def __init__(self, description):
        self.description = description
        self.completion = False


    def __str__(self):
        if self.completion == False:
            return f"{self.description}"
        else:
            return f"{self.description} (DONE!)"

@dataclass
class TaskList:
    tasklist:list
    description:str

    def __init__(self, description):
        self.description = description
        self.tasklist = []

    def addItem(self):
        description = input("Description: ")
        newTask = Task(description)
        self.tasklist.append(newTask)

    def removeItem(self, index:int):
        self.tasklist.pop(index)
    
    def completeTask(self, index:int):
        task:Task
        task = self.tasklist[index]
        task.completion = True

    def displayList(self):
        count = 1
        for task in self.tasklist:
            print(f"{count}. {task}")
            count += 1

    def __iter__(self):
        for task in self.tasklist:
            yield task