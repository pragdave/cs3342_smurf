from dataclasses import dataclass

class Program:
    def __init__(self,code):
        self.code = code

    def evaluate(self):
        mainBinding = Binding({})
        return self.code.evaluate(mainBinding)


class Code:
    def __init__(self,statements):
        self.statements = statements
    
    def evaluate(self,binding):
        value = 0
        for i in self.statements:
            value = i.evaluate(binding)
        return value


class Statement:
    def __init__(self,statement):
        self.statement = statement 
    
    def evaluate(self,binding):
        return self.statement.evaluate(binding)


class VariableDeclaration:
    def __init__(self,declList):
        self.declList = declList
    
    def evaluate(self,binding):
        for decl in self.declList:
            last = decl.evaluate(binding)
        return last


class Decl:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def evaluate(self,binding):
        return binding.add(self.name.evaluate(binding),self.value.evaluate(binding))


class Identifier:
    def __init__(self,value):
        self.value = value
    
    def evaluate(self,binding):
        return self.value


class VariableReference:
    def __init__(self,value):
        self.value = value
    
    def evaluate(self,binding):
        return binding.get(self.value)


class Assignment:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def evaluate(self,binding):
        return binding.add(self.name.evaluate(binding),self.value.evaluate(binding))
        #if(binding.doesExist(self.name)):
            #return binding.add(self.name,self.value)
        #else:
            #print("Must declare new variables using 'let'")
            #return self.value


class Expr:
    def __init__(self,expression):
        self.expression = expression

    def evaluate(self,binding):
        return self.expression.evaluate(binding)


class Integer:
    def __init__(self,value):
        self.value = value

    def evaluate(self,binding):
        return self.value

#addop - adding operations
class Plus:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return self.leftside.evaluate(binding) + self.rightside.evaluate(binding)

class Minus:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return self.leftside.evaluate(binding) - self.rightside.evaluate(binding)

#mulop - multiply operations
class Multiply:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return self.leftside.evaluate(binding) * self.rightside.evaluate(binding)

class Divide:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return int(self.leftside.evaluate(binding) / self.rightside.evaluate(binding))

#relop - relative operations
class IsEqualTo:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self,binding):
        if(self.leftside.evaluate(binding) == self.rightside.evaluate(binding)):
            return 1
        else:
            return 0

class IsNotEqualTo:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self,binding):
        if(self.leftside.evaluate(binding) != self.rightside.evaluate(binding)):
            return 1
        else:
            return 0

class IsGreaterThanOrEqualTo:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self,binding):
        if(self.leftside.evaluate(binding) >= self.rightside.evaluate(binding)):
            return 1
        else:
            return 0

class IsLessThanOrEqualTo:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self,binding):
        if(self.leftside.evaluate(binding) <= self.rightside.evaluate(binding)):
            return 1
        else:
            return 0

class IsGreaterThan:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self,binding):
        if(self.leftside.evaluate(binding) > self.rightside.evaluate(binding)):
            return 1
        else:
            return 0

class IsLessThan:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self,binding):
        if(self.leftside.evaluate(binding) < self.rightside.evaluate(binding)):
            return 1
        else:
            return 0


class Binding:
    def __init__(self,parent):
        self.parent = parent
        self.binding = {}

    def add(self,name,value):
        self.binding[name] = value
        return value
    
    def get(self,name):
        return self.binding[name]

    def doesExist(self,name):
        if name in self.binding:
            return True
        else:
            return False


