class Method():
    def __init__(self, name):
        self.name = name
        self.tools = []

    def addTool(self, tool):
        self.append(tool)