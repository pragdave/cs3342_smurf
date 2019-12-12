class Bindings():
    def __init__(self, parent, binding):
        self.parent = parent
        self.binding = binding
    
    def getVal(self, identifier):
        if isinstance(identifier, str):
            if identifier in self.binding:
                return self.binding[identifier]
            else:
                return self.parent.getVal(identifier)
        if isinstance(identifier, object):
            return self.binding[identifier.ident]
        
    def setVal(self, identifier, val):
        if isinstance(identifier, str):
            self.binding[identifier] = val
        else:
            self.binding[identifier.ident] = val
        
    def setFunc(self, identifier, params, code, bindings):
        paramsTemp = []
        
        for param in bindings.binding:
            self.binding[param] = bindings.getVal(param)
        
        for param in params:
            if isinstance(identifier, str):
                paramsTemp.append(param)
            else:
                paramsTemp.append(param.ident)
        
        self.binding[identifier] = [paramsTemp, code, bindings]
        
    def copy(self):
        tempBinding = dict(self.binding)
        
        newBinding = Bindings(self.parent, tempBinding)
        return newBinding
        
    def __str__(self):
        return str(self.binding)