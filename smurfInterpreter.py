class Binding:
    def __init__(self,parent):
        self.parent = parent
        self.bindings = {}

    def setVariable(self,name,value):
        if name in self.bindings:
            value = self.bindings[name] = value
        else:
            raise Exception("Variable " + str(name) + " does not exist")

    def getVariable(self,name):
        if name in self.bindings:
            return self.bindings[name]
        elif self.parent:
            return self.parent.getVariable(name)
        else:
            raise Exception("Variable " + str(name) + " does not exist")

    def defineVariable(self,name,value=0):
        self.bindings[name] = value
        return value
        
#########################
# Top-Level Structures ##
#########################

class Program:
    def __init__(self,code):
        self.code = code

    def evaluate(self):
        return self.code.evaluate(Binding({}))


class Code:
    def __init__(self,statementList):
        self.statementList = statementList

    def evaluate(self,binding):
        for statement in self.statementList:
            value = statement.evaluate(binding)
        return value


class Variable_Declaration:
    def __init__(self,declList):
        self.declList = declList

    def evaluate(self,binding):
        for decl in self.declList:
            value = decl.evaluate(binding)
        return value


class Decl:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def evaluate(self,binding):
        lhs = self.name.evaluate(binding);
        rhs = self.value.evaluate(binding)
        return binding.defineVariable(lhs,rhs)


class Variable_Reference:
    def __init__(self,name):
        self.name = name

    def evaluate(self,binding):
        return binding.getVariable(self.name)


class If_Expression:
    def __init__(self,condition,then,elseThen = 0):
        self.condition = condition
        self.then = then
        self.elseThen = elseThen

    def evaluate(self,binding):
        if self.condition.evaluate(binding) != 0:
            return self.then.evaluate(binding)
        else:
            return self.elseThen.evaluate(binding)


class Assignment:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def evaluate(self,binding):
        lhs = self.name.evaluate(binding);
        rhs = self.value.evaluate(binding)
        return binding.setVariable(lhs,rhs)


class Function_Call:
    def __init__(self,arguments,name):
        self.arguments = arguments
        self.name = name

    def evaluate(self,binding):
        argList = self.arguments.evaluate(binding)
        variable = self.name.evaluate(binding)
        newBinding = Binding(variable[0].parent)
        newBinding.bindings = variable[0].bindings.copy()
        function = variable[1]
        for x in range(len(argList)):
            newBinding.setVariable(list(newBinding.bindings.keys())[x],argList[x])
        return function.evaluate(newBinding)

class Print_Call:
    def __init__(self,arguments):
        self.arguments = arguments

    def evaluate(self,binding):
        argList = self.arguments.evaluate(binding)
        printStr = "Print: "
        for x in range(len(argList)):
            if x > 0:
                printStr = printStr + "|"
            printStr = printStr + str(argList[x])
        print(printStr)
        return 0;

class Call_Arguments:
    def __init__(self,argList):
        self.argList = argList

    def evaluate(self,binding):
        return list(map(lambda arg: arg.evaluate(binding),self.argList))


class Function_Definition:
    def __init__(self,functionBinding,function):
        self.functionBinding = functionBinding
        self.function = function

    def evaluate(self,binding):
        newBinding = self.functionBinding.evaluate(binding)
        return (newBinding,self.function)


class Param_List:
    def __init__(self,paramList):
        self.paramList = paramList

    def evaluate(self,binding):
        newBinding = Binding(binding)
        for param in self.paramList:
            newBinding.defineVariable(param.evaluate(binding))
        return newBinding
        
#########################
# Terminals #############
#########################

class Integer:
    def __init__(self,value):
        self.value = value
    
    def evaluate(self,binding):
        return self.value


class Identifier:
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
        result = self.lhs.evaluate(binding) + self.rhs.evaluate(binding)
        return result


class Minus:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        result = self.lhs.evaluate(binding) - self.rhs.evaluate(binding)
        return result


class Times:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        result = self.lhs.evaluate(binding) * self.rhs.evaluate(binding)
        return result


class Divide:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self,binding):
        result = self.lhs.evaluate(binding) / self.rhs.evaluate(binding)
        return int(result)

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
