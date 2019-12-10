from visitor import *

class Binding:
    def __init__(self):
        self.bindings = {}
        
    def set_variable_value(self, name, value):
        print(f"Set {name} to {value}")
        self.bindings[name] = value
        
    def get_variable_value(self, name):
        return self.bindings.get(name, 0)
    
    #functions
