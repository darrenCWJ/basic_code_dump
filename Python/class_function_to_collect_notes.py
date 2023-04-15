class Notes:
    def __init__(self):
        self.tasks = {}
    
    def list(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks.items()):
                description, deadline = task
                print(f"{i+1}. {description} (deadline: {deadline})")
    
    def todo(self, description):
        self.tasks[description] = None
        print(f"Added task: {description}")
    
    def set_deadline(self, description, date_string):
        if description not in self.tasks:
            print(f"Task '{description}' does not exist.")
        else:
            self.tasks[description] = date_string
            print(f"Deadline for task '{description}' set to: {date_string}")
            
    

notes = Notes()
notes.list()  # No tasks available.

notes.todo("Borrow book")
notes.todo("read book")
notes.list()
# Tasks:
# 1. Borrow book (deadline: None)
# 2. read book (deadline: None)

notes.set_deadline("Borrow book", "end of may")
# Deadline for task 'Borrow book' set to: end of may

notes.list()
# Tasks:
# 1. Borrow book (deadline: end of may)
# 2. read book (deadline: None)