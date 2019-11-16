from arpeggio import PTNodeVisitor

class Interpreter(PTNodeVisitor):
    binding = {}
    
    def evaluate_number(self, node):
        try:
            return float(node.value)
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
        return multTerm
        
    def evaluate_arithmetic_expression(self, node):
        expr = node.multTerm.accept(self)
        for i in range(1, len(node.plusAndTermList), 2):
            if i and node.plusAndTermList[i-1] == "-":
                expr -= node.plusAndTermList[i].accept(self)
            else:
                expr += node.plusAndTermList[i].accept(self)
        return expr
    
    def evaluate_var_decl(self, node):
        self.binding[node.name] = node.expr.accept(self)
        print("bindings: ", self.binding)
    
    def evaluate_let(self, node):
        for decl in node.list:
            decl.accept(self)
    
    def evaluate_boolean_expression(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        
        if node.op == "==":
            return left == right
        elif node.op == "!=":
            return left != right
        elif node.op == ">=":
            return left >= right
        elif node.op == ">":
            return left > right
        elif node.op == "<=":
            return left <= right
        else:
            return left < right
    
    def evaluate_print(self, node):
        if isinstance(node.expression, str):
            printLine = self.binding[node.expression]
        else:
            printLine = str(node.expression.accept(self))
        for expr in node.list:
            printLine += "|"
            if isinstance(node.expression, str):
                printLine = self.binding[expr.expression]
            else:
                printLine = str(expr.expression.accept(self))
        print(printLine)
        
    def evaluate_code(self, node):
        for expr in node.list:
            value = expr.accept(self)
        
        return value;