class Bindings():
    def __init__(self, parent, binding):
        self.parent = parent
        self.binding = binding
    
    def getVal(self, identifier):
        print("getValIdentifier:", identifier)
        print(self.binding)
        if isinstance(identifier, str):
            if str(self.binding[identifier]):
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
        
        for param in params:
            print("identifier:",identifier)
            if isinstance(identifier, str):
                print("param:",param)
                paramsTemp.append(param)
            else:
                print("param:",param.ident)
                paramsTemp.append(param.ident)
            
        print("paramsTemp:",paramsTemp)
        
        self.binding[identifier] = [paramsTemp, code, bindings]
        print("self.binding:",self.binding)
        
    def copy(self):
        tempBinding = dict(self.binding)
        
        newBinding = Bindings(self.parent, tempBinding)
        return newBinding
        
    def __str__(self):
        return str(self.binding)