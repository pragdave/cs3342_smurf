class Bindings():
    def __init__(self, parent, binding):
        self.parent = parent
        self.binding = binding
    
    def getVal(self, identifier):
        if isinstance(identifier, str):
            if str(self.binding[identifier]):
                return self.binding[identifier]
            else:
                return self.parent.getVal(identifier)
        if isinstance(identifier, object):
            return self.binding[identifier.ident]
        
    def setVal(self, identifier, val):
        self.binding[identifier] = val
        
    def setFunc(self, identifier, params, code, bindings):
        paramsTemp = []
        
        for param in params:
            paramsTemp.append(param.ident)
        
        self.binding[identifier] = [paramsTemp, code, bindings]
        
    def copy(self):
        tempBinding = dict(self.binding)
        
        newBinding = Bindings(self.parent, tempBinding)
        return newBinding
        
    def __str__(self):
        return str(self.binding)