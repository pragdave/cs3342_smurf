from arpeggio import PTNodeVisitor
from binding import Binding

class Interpreter(PTNodeVisitor):
    
    def evaluate_code(self, node):
        g_binding = Binding({})
        value = 0
        for exp in node.expressions:
            value = exp.accept(self, g_binding)
        return value
    
    def evaluate_multiple_decl(self, node, bindings):
        if len(expr1) == 1:
            bindings.setValue(node.expr1[0].accept(self, bindings), '0')
        elif len(expr1) == 3:
            bindings.setValue(node.expr1[0].accept(self, bindings), node.expr1[2].accept(self, bindings))
        
        for i in range(1, len(node.expressions), 2):
            expr = node.expressions[i]
            if(expr == ','):
                continue
            elif(len(expr) > 2):
                bindings.setValue(expr[0].accept(self, bindings), expr[2].accept(self, bindings))
            else:
                bindings.setValue(expr[0].accept(self, bindings), '0')
    
    def evaluate_assignment(self, node, bindings):
        bindings.setValue(node.name.accept(self, bindings), node.value.accept(self, bindings))
    
    def evaluate_var_decl(self, node, bindings):
        bindings.setValue(node.name.accept(self, bindings), '0')
    
    def evaluate_var_value(self, node, bindings):
        name = node.ident
        value = bindings.getValue(name)
        return value
    
    def evaluate_print_smurf(self, node, bindings):
        printer = ""
        #if(len(node.to_print) == 1):
        #    print("Print: {}".format(node.to_print))
        for i in node.to_print:
            printer += str(i.accept(self, bindings))
            if(len(node.to_print) > 1):
                printer += "|"
        print("Print: {}".format(printer))
    
    """
    def evaluate_if_expr(self, node, bindings):
        boolean = node.if_expr.accept(self, bindings)
        if boolean == 1:
            
    """
    
    def evaluate_arith_expr(self, node, bindings):
        val = node.lhs.accept(self, bindings)
        for i in range(1, len(node.expressions), 2):
            if(node.expressions[i-1] == '+'):
                val += node.expressions[i].accept(self, binding)
            elif(node.expressions[i-1] == '-'):
                val -= node.expressions[i].accept(self, binding)
        return int(val)
    
    def evaluate_mult_term(self, node, bindings):
        val = node.lhs.accept(self, bindings)
        for i in range(1, len(node.expressions), 2):
            if(node.expressions[i-1] == '*'):
                val *= node.expressions[i].accept(self, binding)
            elif(node.expressions[i-1] == '/'):
                val /= node.expressions[i].accept(self, binding)
        return int(val)
    
    def evaluate_bool_expr(self, node, bindings):
        left  = node.lhs.accept(self, bindings)
        right = node.rhs.accept(self, bindings)
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
    
    def evaluate_integer(self, node, bindings):
        if(node.sign == '-'):
            return -1*(int(node.value))
        return int(node.value)
    
    def evaluate_identifier(self, node, bindings):
        return node.ident
    