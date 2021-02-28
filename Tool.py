class Tool():
    def __init__(self, name):
        self.name = name
        self.actions = []
    
    def addAction(self, action):
        self.actions.append(action)