from arpeggio import PTNodeVisitor

class Interpreter(PTNodeVisitor):
    binding = {}
    
    ##############
    #Math Portion#
    ##############
    
    def evaluate_number(self, node):
        try:
            return int(node.value)
        except ValueError:
            return self.binding[node.value]
    
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
        self.binding[node.name] = node.expr.accept(self)
        print("bindings: ", self.binding)
    
    def evaluate_let(self, node):
        for decl in node.list:
            if isinstance(decl, str):
                self.binding[decl] = 0
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
        printLine = str(node.expression.accept(self))
        for expr in node.list:
            printLine += "|"
            printLine += str(expr.accept(self))
        print(printLine)
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
        
    ####################
    #Top Level Function#
    ####################
        
    def evaluate_code(self, node):
        for expr in node.list:
            value = expr.accept(self)
        return value;