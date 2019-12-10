from arpeggio import PTNodeVisitor
from bindings import Binding as binding

class Interpreter(PTNodeVisitor):
    
    def evaluate_code(self, node, binding):
        value = 0
        for exp in node.expressions:
            value = exp.accept(self, binding)
        return value
    
    def evaluate_assignment(self, node, binding):
        value = node.expression.accept(self)
        binding.set_variable(self.name, value)
        return value
    
    def evaluate_var_value(self, node, binding):
        val =  binding.get_variable_value(self.name)
        return val
    
    def evaluate_integer(self, node, binding):
        return int(node.value)
    
    def evaluate_greater_than(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        rel = int(left) > int(right)
        return rel
    
    def evaluate_greater_equal(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        rel = int(left) >= int(right)
        return rel
    
    def evaluate_equals(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        rel = int(left) == int(right)
        return rel
    
    def evaluate_not_equals(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        rel = int(left) != int(right)
        return rel
    
    def evaluate_less_than(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        rel = int(left) < int(right)
        return rel
    
    def evaluate_less_equal(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        rel = int(left) <= int(right)
        return rel
    
    def evaluate_identifier(self, node, binding):
        return node.ident.accept(self)
    
    def evaluate_plus(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        total = int(left) + int(right)
        print("{} + {}".format(int(left),int(right)))
        return total
    
    def evaluate_divide(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        total = int(left) / int(right)
        print("{} / {}".format(int(left),int(right)))
        return total
    
    def evaluate_times(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        total = int(left) * int(right)
        print("{} * {}".format(int(left),int(right)))
        return total
        
    def evaluate_minus(self, node, binding):
        left = node.lhs.accept(self, binding)
        right = node.rhs.accept(self, binding)
        total = int(left) - int(right)
        print("{} - {}".format(int(left),int(right)))
        return total
