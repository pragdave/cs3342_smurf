from arpeggio import PTNodeVisitor

class Visitor(PTNodeVisitor):
    def visit_number(self, node, children):
        if self.debug:
            print("Converting {}".format(node.value))
        return float(node.value)
    
    def visit_factor(self, node, children):
        if self.debug:
            print("Factor {}".format(children))
        if len(children) == 1:
            return children[0]
        if children[0] == '-':
            sign = -1
        else:
            sign = 1
        return sign * children[1]
        
    def visit_term(self, node, children):
        if self.debug:
            print("Term {}".format(children))
        term = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "*":
                term *= children[i]
            else:
                term /= children[i]
        if self.debug:
            print("Term = {}".format(term))
        return term
        
    def visit_arithmetic_expression(self, node, children):
        if self.debug:
            print("Expression{}".format(children))
        expr = children[0]
        for i in range(2, len(children), 2):
            if i and children[i-1] == "-":
                expr -= children[i]
            else:
                expr += children[i]
        if self.debug:
            print("Expression = {}".format(expr))
        return expr
        
    def visit_print_func(self, node, children):
        print(children[0])