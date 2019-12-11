from arpeggio import PTNodeVisitor
from binding import Binding

class Interpreter(PTNodeVisitor):
    
    def evaluate_code(self, node):
        g_binding = Binding({}, None)
        for exp in node.expressions:
            value = exp.accept(self, g_binding)
        return value
    
    def evaluate_function_call(self, node, bindings):
        params = node.args.accept(self, bindings)
        func_name = node.name.accept(self, bindings)
        funcBinding = Binding(func_name[0].parent)
        funcBinding.bindings = func_name[0].bindings.copy()
        function = func_name[1]
        for x in range(len(params)):
            funcBinding.setValue(list(funcBinding.bindings.keys())[x],params[x])
        return function.accept(self, funcBinding)
    
    def evaluate_brace_block(self, node, bindings):
        for exp in node.expressions:
            value = exp.accept(self, bindings)
        return value
    
    def evaluate_func_definition(self, node, bindings):
        new_binding = node.func_binding.accept(self, bindings)
        return new_binding
        
    def evaluate_parameters(self, node, bindings):
        func_binding = Binding(bindings)
        for p in node.params:
            func_binding.createVal(p.accept(self, bindings))
        return func_binding
    
    def evaluate_arguments(self, node, bindings):
        argList = []
        for a in node.args:
            argList.append(map(a.accept(self, bindings), node.args))
        return argList
    
    def evaluate_let_decl(self, node, bindings):
        for let in node.expressions:
            if isinstance(let, str):
                bindings.setValue(let, 0)
            else:
                let.accept(self, bindings)
    
    def evaluate_assignment(self, node, bindings):
        left = node.name.accept(self, bindings)
        right = node.value.accept(self, bindings)
        bindings.setValue(left, right)
    
    def evaluate_var_decl(self, node, bindings):
        return bindings.setValue(node.name.accept(self, bindings), 0)
    
    def evaluate_var_value(self, node, bindings):
        name = node.name
        value = bindings.getValue(name)
        return value
    
    def evaluate_print_smurf(self, node, bindings):
        printer = ""
        for i in node.to_print:
            printer += str(i.accept(self, bindings))
            if(len(node.to_print) > 1):
                printer += "|"
        print("Print: {}".format(printer))
    
    
    def evaluate_if_expr(self, node, bindings):
        boolean = node.if_expr.accept(self, bindings)
        if boolean == 1:
            return node.if_expr.accept(self, bindings)
        else:
            return node.else_expr.accept(self, bindings)
    
    def evaluate_if(self, node, bindings):
        boolean = int(node.if_bool.accept(self, bindings))
        if boolean == 1:
            return node.if_expr.accept(self, bindings)
    
    def evaluate_arith_expr(self, node, bindings):
        val = node.lhs.accept(self, bindings)
        for i in range(1, len(node.expressions), 2):
            if(node.expressions[i-1] == '+'):
                val += node.expressions[i].accept(self, bindings)
            elif(node.expressions[i-1] == '-'):
                val -= node.expressions[i].accept(self, bindings)
            if len(node.expressions) > 2:
                print("({} {} {})".format(node.expressions[i-1].accept(self, bindings), node.lhs.accept(self, bindings), node.expressions[i].accept(self, bindings)), end="")
            else:
                print("({} {} {})".format(node.expressions[i-1], node.lhs.accept(self, bindings), node.expressions[i].accept(self, bindings)), end="")
        return int(val)
    
    def evaluate_mult_term(self, node, bindings):
        val = node.lhs.accept(self, bindings)
        if str(type(val)) == 'NoneType':
            print("not valid input")
            return
        for i in range(1, len(node.expressions), 2):
            if(node.expressions[i-1] == '*'):
                val *= node.expressions[i].accept(self, bindings)
            elif(node.expressions[i-1] == '/'):
                val /= node.expressions[i].accept(self, bindings)
            if len(node.expressions) > 2:
                print("({} {} {})".format(node.expressions[i-1].accept(self, bindings), node.lhs.accept(self, bindings), node.expressions[i].accept(self, bindings)))
            else:
                print("{} {} {}".format(node.expressions[i-1], node.lhs.accept(self, bindings), node.expressions[i].accept(self, bindings)))
        return int(val)
    
    def evaluate_bool_expr(self, node, bindings):
        left  = node.lhs.accept(self, bindings)
        right = node.rhs.accept(self, bindings)
        print("{} {} {}".format(str(node.op), left, right))
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
        try:
            val = bindings.getValue(node.ident.accept(self, bindings))
        except:
            val = node.ident
        return val
    