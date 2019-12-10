class Context:
    def __init__(self, parent):
        self.context = {}
        self.parent = parent

    def setVar(self, name, value):
        self.context[name] = value

    def getVar(self, name):
        if name in self.context:
            return self.context[name]
        else:
            raise Exception("Undefined reference encountered.")
