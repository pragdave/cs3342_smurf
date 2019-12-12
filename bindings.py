class binding:

    def __init__(self, owner):
        self.binding = {}
        self.owner = owner

    #adds in or changes a value
    #easieer to have one function than one to create and one to replace bc it would work the same
    def setVar(self, name, value):
        self.binding[name] = value

    def getVar(self, name):
        curr = self 
         #when checking a value you can look at your parents bc those would still be in scope
        while (not(curr is None) and not(name in curr.binding)):
            curr = curr.owner 
        if curr is None:
            raise Exception("Undefined reference encountered.")
        else:
            return curr.binding[name]