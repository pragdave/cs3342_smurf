class Context:
    def __init__(self, parent):
        self.context = {}
        self.parent = parent

    def setVar(self, name, value):
        self.context[name] = value

    def getVar(self, name):
        curContext = self
        while (not(curContext is None) and not(name in curContext.context)):
            curContext = curContext.parent

        if curContext is None:
            raise Exception("Undefined reference encountered.")

        else:
            return curContext.context[name]


class Terminal:
    def __init__(self, val):
        self.value = val

    def eval(self, context):
        return self.value
