from arpeggio import PTNodeVisitor
from Bindings import Bindings

class Interpreter(PTNodeVisitor):    
    ##############
    #Math Portion#
    ##############
    
    def evaluate_number(self, node, bindings):
        if node.sign == "-":
            return -1 * int(node.value)
        return int(node.value)
        
    def evaluate_var_ref(self, node, bindings):
        return bindings.getVal(node.ident)
            
    def evaluate_factor(self, node, bindings):
        return node.value.accept(self, bindings)
        
    def evaluate_mult_term(self, node, bindings):
        multTerm = node.factor.accept(self, bindings)
        for i in range(1, len(node.multAndFactList), 2):
            if node.multAndFactList[i-1] == "*":
                multTerm *= node.multAndFactList[i].accept(self, bindings)
            else:
                multTerm /= node.multAndFactList[i].accept(self, bindings)
        return int(multTerm)
        
    def evaluate_arithmetic_expression(self, node, bindings):
        expr = node.multTerm.accept(self, bindings)
        for i in range(1, len(node.plusAndTermList), 2):
            if i and node.plusAndTermList[i-1] == "-":
                expr -= node.plusAndTermList[i].accept(self, bindings)
            else:
                expr += node.plusAndTermList[i].accept(self, bindings)
        return int(expr)
    
    ####################
    #Built in Functions#
    ####################
    
    def evaluate_var_decl(self, node, bindings):
        
        bindings.setVal(node.name, node.expr.accept(self, bindings))
        print("variable bindings: ", bindings)
    
    def evaluate_var_let(self, node, bindings):
        for decl in node.list:
            if isinstance(decl, str):
                self.bindings.setVal(decl, 0)
            else:
                decl.accept(self, bindings)
    
    def evaluate_var_decl(self, node, bindings):
        bindings.setVal(node.name.ident, node.expr.accept(self, bindings))
        #print("bindings: ", bindings)
    
    def evaluate_var_let(self, node, bindings):
        for decl in node.list:
            if isinstance(decl, str):
                bindings.setVal(decl, 0)
            else:
                decl.accept(self, bindings)
    
    def evaluate_boolean_expression(self, node, bindings):
        left = node.left.accept(self, bindings)
        right = node.right.accept(self, bindings)
        
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
    
    def evaluate_print_func(self, node, bindings):
        list = node.listOfList[0]
        printLine = ""
        for expr in list:
            printLine += str(expr.accept(self, bindings))
            printLine += "|"
        printLine = printLine[:-1]
        print("Print: ",printLine)
        return printLine
        
    def evaluate_code_block(self, node, bindings):
        lastLine = node.list.pop()
        for line in node.list:
            line.accept(self, bindings)
        return lastLine.accept(self, bindings)
        
    def evaluate_if_statement(self, node, bindings):
        boolVal = node.boolExpr.accept(self, bindings)
        if boolVal == 1:
            return node.ifBlock.accept(self, bindings)
        return node.elseBlock.accept(self, bindings)
    
    def evaluate_fn_decl(self, node, bindings):
        newBindings = Bindings(bindings, {})
        if isinstance(node.name, str):
            bindings.setFunc(node.name, node.paramList, node.codeBlock, newBindings)
        else:
            bindings.setFunc(node.name.ident, node.paramList, node.codeBlock, newBindings)
        #print("bindings: ", bindings)
        
    def evaluate_fn_let(self, node, bindings):
        for decl in node.list:
            decl.accept(self, bindings)
            
    def evaluate_fn_call(self, node, bindings):
        function = bindings.getVal(node.name)
        parameters = function[0]
        code = function[1]
        index = 0
        for param in parameters:
            bindings.setVal(param, node.paramList[index].accept(self, bindings))
            index += 1
        return code.accept(self, bindings)
    
    ####################
    #Top Level Function#
    ####################
        
    def evaluate_code(self, node):
        globalBinding = Bindings(None, {})
        for expr in node.list:
            value = expr.accept(self, globalBinding)
        return value;
