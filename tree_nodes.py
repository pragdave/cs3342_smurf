from binding import Binding

class Variable:
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_value(self, bindings)

class Code:
    def __init__(self, expressions):
        self.expressions = expressions
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_code(self)

class Arguments:
    def __init__(self, args):
        self.args = args
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_arguments(self, bindings)
    
class Parameters:
    def __init__(self, params):
        self.params = params
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_parameters(self, bindings)

class Function_Call:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_func_call(self, bindings)
        
class Function_Definition:
    def __init__(self, func_binding, func):
        self.func_binding = func_binding
        self.func = func
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_func_definition(self, bindings)
        
class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_assignment(self, bindings)

class Brace_Block:
    def __init__(self, expressions):
        self.expressions = expressions
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_brace_block(self, bindings)

class Let_Decl:
    def __init__(self, expressions):
        self.expressions = expressions
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_let_decl(self, bindings)


class If_Else:
    def __init__(self, if_bool, if_expr, else_expr):
        self.if_bool = if_bool
        self.if_expr = if_expr
        self.else_expr = else_expr
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_if_expr(self, bindings)

class If_Expression:
    def __init__(self, if_bool, if_expr):
        self.if_bool = if_bool
        self.if_expr = if_expr
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_if(self, bindings)

class Declaration:
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_decl(self, bindings)

class Arithmetic_Expression:
    def __init__(self, lhs, expressions):
        self.lhs = lhs
        self.expressions = expressions
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_arith_expr(self, bindings)

class Mult_Term:
    def __init__(self, lhs, expressions):
        self.lhs = lhs
        self.expressions = expressions
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_mult_term(self, bindings)
    
class Boolean_Expression:
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_bool_expr(self, bindings)
    
class Print_Smurf:
    def __init__(self, to_print):
        self.to_print = to_print
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_print_smurf(self, bindings)

#############
# TERMINALS #
#############

class Integer:
    def __init__(self, sign, value):
        self.sign = sign
        self.value = value
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_integer(self, bindings)

class Identifier:
    def __init__(self, ident):
        self.ident = ident
    
    def accept(self, visitor, bindings):
        if(bindings.hasVal(self.ident)):
            return bindings.getValue(self.ident)
        return visitor.evaluate_identifier(self, bindings)
