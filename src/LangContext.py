class Context:
    # Represents a set of bindings (or an execution scope)
    # Contains a parent reference (to another context); vars not located in
    # the current context are propagated up to higher (more widely-scoped) contexts

    def __init__(self, parent):
        self.context = {}
        self.parent = parent

    def setVar(self, name, value):
        # assign variable in context; do not evaluate value since it may be a function
        # definition or expression that cannot yet be reduced to a terminal
        self.context[name] = value

    def getVar(self, name):
        # start curContext at this binding set
        curContext = self
        # then move up the chain of parents until a specified variable is found
        while (not(curContext is None) and not(name in curContext.context)):
            curContext = curContext.parent

        # curContext will be 'None' if the var couldn't be found
        if curContext is None:
            raise Exception("Undefined reference encountered.")

        # return the var as represented in the closest context
        else:
            return curContext.context[name]
