from dataclasses import dataclass

class Program:
    def __init__(self,code):
        self.code = code

    def evaluate(self):
        mainBinding = Binding()
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


# class IfExpression:
#     def __init__(self,expression,ifblock,elseblock):
#         self.expression = expression
#         self.ifblock = ifblock
#         self.elseblock = elseblock

#     def evaluate(self,binding):
#         if(self.expression.evaluate(binding) == 1):
#             return self.ifblock.evaluate(binding)
#         else:
#             return self.elseblock.evaluate(binding)

class IfExpression:
    def __init__(self,children):
        self.children = children

    def evaluate(self,binding):
        if(self.children[0].evaluate(binding) == 1):
            return self.children[1].evaluate(binding)
        else:
            if(len(self.children) == 3):
                return self.children[2].evaluate(binding)


class Assignment:
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def evaluate(self,binding):
        return binding.add(self.name.evaluate(binding),self.value.evaluate(binding))
        # if(binding.doesExist(self.name)):
        #     return binding.add(self.name,self.value)
        # else:
        #     print("Must declare new variables using 'let'")
        #     return self.value


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

#NOT YET TESTED
class FunctionCall:
    def __init__(self,name,call_arguments):
        self.name = name
        self.call_arguments = call_arguments
    
    def evaluate(self,binding):
        arguments = self.call_arguments.evaluate(binding)

        if self.name == "print":
            output = "Print: "
            for args in arguments:
                output = output + str(args)
            print(output)
            return
        else:
            variableRef = self.name.evaluate(binding)
            newBinding = Binding(variableRef[0].parent)
            newBinding.binding = variableRef[0].binding.copy()
            for i in range(len(arguments)):
                newBinding.add(list(newBinding.binding.keys())[i],arguments[i])
            functionBody = variableRef[1]
            return functionBody.evaluate(newBinding)


#NOT YET TESTED
class CallArguments:
    def __init__(self,arguments):
        self.arguments = arguments

    def evaluate(self,binding):
        # i = 0
        # for name in binding.binding:
        #     binding[name] = self.arguments[i].evalutate(binding)
        # return self.arguments[i].evaluate(binding)
        return list(map(lambda arg: arg.evaluate(binding),self.arguments))


#NOT YET TESTED
class FunctionDefinition:
    def __init__(self,newBinding,codeBlock):
        self.newBinding = newBinding
        self.codeBlock = codeBlock
    
    def evaluate(self,binding):
        evaluatedBinding = self.newBinding.evaluate(binding)
        funcDef = (evaluatedBinding,self.codeBlock)
        return funcDef


#NOT YET TESTED
class ParamList:
    def __init__(self,parameters):
        self.parameters = parameters
    
    def evaluate(self,binding):
        newBinding = Binding(binding)
        if(len(self.parameters) != 0):
            for parameter in self.parameters:
                newBinding.add(parameter,0)
        return newBinding


class BraceBlock:
    def __init__(self,code):
        self.code = code
    
    def evaluate(self,binding):
        return self.code.evaluate(binding)


class Binding:
    def __init__(self,parent=None):
        self.parent = parent
        self.binding = {}

    def add(self,name,value):
        self.binding[name] = value
        return value
    
    def get(self,name):
        if name in self.binding:
            return self.binding[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            print("variable " + name + " is not defined")

    def doesExist(self,name):
        if name in self.binding:
            return True
        elif self.parent:
            return self.parent.doesExist(name)
        else:
            return False


