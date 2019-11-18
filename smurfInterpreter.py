#########################
# Structural classes ####
#########################

class Binding:
    def __init__(self,parent):
        # self.parent = parent
        self.bindings = {}

    def setVariable(self,name,value):
        if name in self.bindings:
            self.bindings[name] = value
            return value
        else:
            raise Exception("Variable " + str(name) + " does not exist")

    def getVariable(self,name,value):
        if name in self.bindings:
            return self.bindings[name]
        else:
            raise Exception("Variable " + str(name) + " does not exist")

    def defineVariable(self,name):
        self.bindings[name] = 0;
    
#########################
# Non-Terminals #########
#########################

class Integer:
    def __init__(self,value):
        self.value = value
    
    def evaluate(self,binding):
        return self.value

#########################
# Arithmetic operations #
#########################

class Plus:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        return self.lhs.evaluate(binding) + self.rhs.evaluate(binding)

class Minus:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        return self.lhs.evaluate(binding) - self.rhs.evaluate(binding)

class Times:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        return self.lhs.evaluate(binding) * self.rhs.evaluate(binding)

class Divide:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        return self.lhs.evaluate(binding) / self.rhs.evaluate(binding)

#########################
# Boolean Operations ####
#########################

class Equal:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        if(self.lhs.evaluate(binding) == self.rhs.evaluate(binding)):
            return 1
        else:
            return 0

class NotEqual:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        if(self.lhs.evaluate(binding) != self.rhs.evaluate(binding)):
            return 1
        else:
            return 0

class GreaterEqual:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        if(self.lhs.evaluate(binding) >= self.rhs.evaluate(binding)):
            return 1
        else:
            return 0

class Greater:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        if(self.lhs.evaluate(binding) > self.rhs.evaluate(binding)):
            return 1
        else:
            return 0

class LessEqual:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        if(self.lhs.evaluate(binding) <= self.rhs.evaluate(binding)):
            return 1
        else:
            return 0

class Less:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        if(self.lhs.evaluate(binding) < self.rhs.evaluate(binding)):
            return 1
        else:
            return 0

#########################
#########################
#########################

class Expr:
    def __init__(self,expression):
        self.expression = expression

    def evaluate(self,binding):
        return self.expression.evaluate(binding)