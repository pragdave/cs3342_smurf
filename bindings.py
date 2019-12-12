#BINDING LOGIC THAT FITS WELL WITH ARPEGGIO AND THAT WE LEARNED IN CLASS
class Binding:
    def __init__(self, outer=None):
        self.bindings = {}
        self.outer    = outer

    def push(self):
        return Binding(self)

    def pop(self):
        return self.outer

    def set_variable(self, name, value):
        self.bindings[name] = value
        return self.bindings[name]
        
    def get_variable_value(self, name):
        if name in self.bindings:
            return self.bindings[name]
        if self.outer:
            return self.outer.get_variable_value(name)
        raise Exception(f"Variable '{name}' is not defined")
    