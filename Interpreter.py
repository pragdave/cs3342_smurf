from arpeggio import PTNodeVisitor
from Bindings import Bindings

class Interpreter(PTNodeVisitor):
    varBinding = Bindings(None, {})
    funcBinding = Bindings(None, {})
    
    ##############
    #Math Portion#
    ##############
    
    def evaluate_number(self, node):
        try:
            return int(node.value)
        except ValueError:
            return self.varBinding.getVal(node.value)
            
    def evaluate_factor(self, node):
        if node.sign == "-":
            return -1 * node.value.accept(self)
        return node.value.accept(self)
        
    def evaluate_mult_term(self, node):
        multTerm = node.factor.accept(self)
        for i in range(1, len(node.multAndFactList), 2):
            if node.multAndFactList[i-1] == "*":
                multTerm *= node.multAndFactList[i].accept(self)
            else:
                multTerm /= node.multAndFactList[i].accept(self)
        return int(multTerm)
        
    def evaluate_arithmetic_expression(self, node):
        expr = node.multTerm.accept(self)
        for i in range(1, len(node.plusAndTermList), 2):
            if i and node.plusAndTermList[i-1] == "-":
                expr -= node.plusAndTermList[i].accept(self)
            else:
                expr += node.plusAndTermList[i].accept(self)
        return int(expr)
    
    ####################
    #Built in Functions#
    ####################
    
    def evaluate_var_decl(self, node):
        self.varBinding.setVal(node.name, node.expr.accept(self))
        print("variable bindings: ", self.varBinding)
    
    def evaluate_var_let(self, node):
        for decl in node.list:
            if isinstance(decl, str):
                self.varBinding.setVal(decl, 0)
            else:
                decl.accept(self)
    
    def evaluate_var_decl(self, node):
        self.varBinding.setVal(node.name, node.expr.accept(self))
        print("bindings: ", self.varBinding)
    
    def evaluate_var_let(self, node):
        for decl in node.list:
            if isinstance(decl, str):
                self.varBinding.setVal(decl, 0)
            else:
                decl.accept(self)
    
    def evaluate_boolean_expression(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        
        if node.op == "==":
            return int(left == right)
        elif node.op == "!=":
            return int(left != right)
        elif node.op == ">=":
            return int(left >= right)
        elif node.op == ">":
            return int(left > right)
        elif node.op == "<=":
            return int(left <= right)
        else:
            return int(left < right)
    
    def evaluate_print_func(self, node):
        list = node.listOfList[0]
        printLine = ""
        for expr in list:
            printLine += str(expr.accept(self))
            printLine += "|"
        printLine = printLine[:-1]
        print("Print: ",printLine)
        return printLine
        
    def evaluate_code_block(self, node):
        lastLine = node.list.pop()
        for line in node.list:
            line.accept(self)
        return lastLine.accept(self)
        
    def evaluate_if_statement(self, node):
        boolVal = node.boolExpr.accept(self)
        if boolVal == 1:
            return node.ifBlock.accept(self)
        return node.elseBlock.accept(self)
    
    def evaluate_fn_decl(self, node):
        self.funcBinding.setFunc(node.name, node.paramList, node.codeBlock)
        print("function bindings: ", self.funcBinding)
        
    def evaluate_fn_let(self, node):
        for decl in node.list:
            decl.accept(self)
            
    def evaluate_fn_call(self, node):
        function = self.funcBinding.getVal(node.name)
        parameters = function[0]
        code = function[1]
        #tempBinding = self.varBinding.copy()
        
        #index = 0
        #for param in parameters:
        #    tempBinding[param] = node.paramList[index].accept(self)
        #    index += 1
        #print(self.varBinding)
        #print(tempBinding)
        return code.accept(self)
    
    ####################
    #Top Level Function#
    ####################
        
    def evaluate_code(self, node):
        for expr in node.list:
            value = expr.accept(self)
        return value;
