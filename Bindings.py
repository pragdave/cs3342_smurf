class Bindings():
    def __init__(self, parent, binding):
        self.parent = parent
        self.binding = binding
    
    def getVal(self, identifier):
        if self.binding[identifier]:
            return self.binding[identifier]
        return self.parent.getVal(identifier)
        
    def setVal(self, identifier, val):
        self.binding[identifier] = val
        
    def setFunc(self, identifier, params, code):
        self.binding[identifier] = [params, code]
        
    def __str__(self):
        return str(self.binding)