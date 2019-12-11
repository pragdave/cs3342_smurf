
class Binding():
    def __init__(self, binding, parent):
        self.binding = binding
        self.parent = parent
        
    def setValue(self, name, value):
        self.binding[name] = value
        
    def getValue(self, name):
        if name in self.binding.keys():
            return self.binding[name]
        else:
            raise Exception("not a valid value")
            
    
    def createVal(self, name, value):
        self.binding[name] = value
        return value
    
    def hasVal(self, name):
        if name in self.binding.keys():
            return True
        return False
    
    #functions
