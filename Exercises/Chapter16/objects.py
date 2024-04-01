from dataclasses import dataclass

@dataclass
class Task:
    description:str = ""
    completion:bool = False

    def __str__(self):
        if self.completion == False:
            return f"{self.description}"
        else:
            return f"{self.description} (DONE!)"

