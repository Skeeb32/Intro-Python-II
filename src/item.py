class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return(f"You have aquired {self.name}/n {self.description}/n")