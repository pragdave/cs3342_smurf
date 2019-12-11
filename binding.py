
class Binding():
    def __init__(self, binding):
        self.binding = binding
        
    def setValue(self, name, value):
        self.binding[name] = value
        
    def getValue(self, name):
        return self.binding[name]
    
    #functions
