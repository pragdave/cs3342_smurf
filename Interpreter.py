from arpeggio import PTNodeVisitor

class Interpreter(PTNodeVisitor):
    def evaluate_number(self, node):
        return float(node.value)
    
    def evaluate_factor(self, node):
        if node.sign == "-":
            return -1 * node.value.accept(self)
        return node.value.accept(self)
        
    def evaluate_term(self, node):
        term = node.factor.accept(self)
        for i in range(1, len(node.multAndFactList), 2):
            if node.multAndFactList[i-1] == "*":
                term *= node.multAndFactList[i].accept(self)
            else:
                term /= node.multAndFactList[i].accept(self)
        return term
        
    def evaluate_arithmetic_expression(self, node):
        expr = node.term.accept(self)
        for i in range(1, len(node.plusAndTermList), 2):
            if i and node.plusAndTermList[i-1] == "-":
                expr -= node.plusAndTermList[i].accept(self)
            else:
                expr += node.plusAndTermList[i].accept(self)
        return expr
    
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
        printLine = str(node.expression.accept(self))
        for expr in node.list:
            printLine += "|"
            printLine += str(expr.accept(self))
        print(printLine)
        
    def evaluate_code(self, node):
        for expr in node.list:
            value = expr.accept(self)
        
        return value;