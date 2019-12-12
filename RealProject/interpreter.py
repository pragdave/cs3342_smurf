class Program:
    def __init__(self,node, program):
        self.program = program
        #Node is included for debugging
        self.node = node

    def eval(self):
        return self.program.eval()


class Comment:
    def __init__(self, comment):
        self.comment = comment


class Code:
    def __init__(self, programStatements):
        #list_
        self.programStatements = programStatements

    def eval(self):
        #forin will go through each statement that is provided
        for eachStatement in self.programStatements:
            statementValue = eachStatement.eval()
        return statementValue


class Statement:
    def __init__(self, statement):
        self.statement = statement

    def eval(self):
        return self.statement.eval()


class Expr:
    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        return self.expr.eval()

class If:
    def __init__(self,ifExpr):
        self.ifExpr = ifExpr

    def eval(self):
        #ifExpr[0] is the if condition
        #ifExpr[1] is what is within the if block
        #ifExpr[2] is what is within the else block
        if self.ifExpr[0].eval():
            return self.ifExpr[1].eval()
        elif (len(self.ifExpr) > 2):
            return self.ifExpr[2].eval()

        return

class AddSub:
    def __init__(self, term1, addop, term3):
        self.term1 = term1
        self.addop = addop
        self.term3 = term3

    def eval(self):
        if(self.addop == '+'):
            return self.term1.eval() + self.term3.eval()
        else:
            return self.term1.eval() - self.term3.eval()

class MultDivide:
    def __init__(self,term1, mulop, term3):
        #term 1 is the term to the left of the mulop
        #mulop is the multiplication or division operator
        #term3 is the term to the left of the mulop
        self.term1 = term1
        self.mulop = mulop
        self.term3 = term3

    def eval(self):
        if (self.mulop == '*'):
            return self.term1.eval() * self.term3.eval()
        else:
            return int(self.term1.eval() / self.term3.eval())

class Boolean:
    def __init__(self, term1,relop, term3):
        #term1 is the term to the left of the operator
        self.term1 = term1
        #relop is one of the relops[==,!=,>=,>,<=,<]
        self.relop = relop
        #term3 is the term to the right of the relop
        self.term3 = term3
    #this eval will determine the integer result of relop with the two terms being compared    
    def eval(self):
        if (self.relop == "=="):
            return int(self.term1.eval() == self.term3.eval())
        elif (self.relop == "!="):
            return int(self.term1.eval() != self.term3.eval())
        elif (self.relop == ">="):
            return int(self.term1.eval() >= self.term3.eval())
        elif (self.relop == ">"):
            return int(self.term1.eval() > self.term3.eval())
        elif (self.relop == "<="):
            return int(self.term1.eval() <= self.term3.eval())
        elif (self.relop == "<"):
            return int(self.term1.eval() < self.term3.eval())
        print("Incorrect Boolean Operator provided")
        return

class Integer:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return int(self.num)

class FunctionCall:
    def __init__(self, function, arguments):
        self.function = function
        self.arguments = arguments

    def eval(self):
        num = self.arguments.eval()
        if type(num) == int:
            print(f"{num}")