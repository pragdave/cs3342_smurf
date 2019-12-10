from arpeggio import PTNodeVisitor
from bindings import Binding as binding

class Interpreter(PTNodeVisitor):
    
    def evaluate_code(self, node, binding):
        value = 0
        for exp in node.expressions:
            value = exp.accept(self, binding)
        return value
    
    def evaluate_assignment(self, node, binding):
        value = node.expression.accept(self, binding)
        binding.set_variable(self.name, value)
        return value
    
    def evaluate_var_value(self, node, binding):
        val =  binding.get_variable_value(node.name)
        return val
    
    def evaluate_print_smurf(self, node, binding):
        printer = ""
        for i in node.to_print:
            printer += str(i.accept(self, binding))
            if(len(node.to_print) > 1):
                printer += "|"
        print("Print: {}".format(printer))
    
    def evaluate_arith_expr(self, node, binding):
        val = node.lhs.accept(self, binding)
        for i in range(1, len(node.expressions), 2):
            if(node.expressions[i-1] == '+'):
                val += node.expressions[i].accept(self, binding)
            elif(node.expressions[i-1] == '-'):
                val -= node.expressions[i].accept(self, binding)
        return int(val)
    
    def evaluate_mult_term(self, node, binding):
        val = node.lhs.accept(self, binding)
        for i in range(1, len(node.expressions), 2):
            if(node.expressions[i-1] == '*'):
                val *= node.expressions[i].accept(self, binding)
            elif(node.expressions[i-1] == '/'):
                val /= node.expressions[i].accept(self, binding)
        return int(val)
    
    def evaluate_bool_expr(self, node, binding):
        left  = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        if(node.op == '=='):
            return int(left == right)
        elif(node.op == '!='):
            return int(left != right)
        elif(node.op == '<='):
            return int(left <= right)
        elif(node.op == '<'):
            return int(left < right)
        elif(node.op == '>='):
            return int(left >= right)
        elif(node.op == '>'):
            return int(left > right)
    
    def evaluate_integer(self, node, binding):
        if(node.sign == '-'):
            return -1*(int(node.value))
        return int(node.value)
    
    def evaluate_identifier(self, node, binding):
        return node.ident.accept(self)
    