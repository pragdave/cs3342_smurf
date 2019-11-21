from AstVisitor import Binding, Thunk
import math

class Interpreter:
    def __init__(self):
        self.binding = Binding()
    
    def evaluate_Int(self, node, binding):
        if node.sign == '-':
            return -1*int(node.value, 10)
        else:
            return int(node.value, 10)
        
    def evaluate_binOp(self, node, binding):
        lval = node.left.accept(self, binding)
        rval = node.right.accept(self, binding)
        if node.op == '+':
            return lval + rval
        elif node.op == '-':
            return lval - rval
        elif node.op == '*':
            return lval * rval
        elif node.op == '/':
            return math.trunc(lval/rval)
        
    def evaluate_RelOp(self, node, binding):
        lval = node.left.accept(self, binding)
        rval = node.right.accept(self, binding)
        
        if node.op == '==' and lval == rval:
            return 1
        elif node.op == '!=' and lval != rval:
            return 1
        elif node.op == '>=' and lval >= rval:
            return 1
        elif node.op == '>' and lval > rval:
            return 1
        elif node.op == '<=' and lval <= rval:
            return 1
        elif node.op == '<' and lval < rval:
            return 1  
        else:
            return 0
        
    def evaluate_Assignment(self, node, binding):
        val = node.expression.accept(self, binding)
        binding.set_var_val(node.name, val)   
        return val
    
    def evaluate_Code(self, node, binding):
        value = ''
        for ex in node.expressions:
            value = ex.accept(self, binding)
        return value
    
    def evaluate_VarDec(self, node, binding):
        val = node.value.accept(self, binding)
        binding.set_var(node.name, val)
        return val
    
    def evaluate_DecList(self, node, binding):
        last = ''
        for i in node.decls:
            last = i.accept(self, binding)
        return last
    
    def evaluate_VarRef(self, node, binding):
        return binding.get_var(node.name)
    
    def evaluate_Printer(self, node, binding):
        val = 0
        # out = open('output.txt', 'a')
        print("Print: ", end='')
        for i, x in enumerate(node.expressions):
            val = x.accept(self, binding)
            if i < len(node.expressions) - 1:
                print(str(val), end='|')
            else:
                print(str(val), end='\n')      
        return val
    
    def evaluate_If(self, node, binding):
        if node.expr.accept(self, binding) == 1:
            return node.code.accept(self, binding)
        else:
            return False
        
    def evaluate_IfElse(self, node, binding):
        if node.expr.accept(self, binding) == 1:
            return node.ifCode.accept(self, binding)
        else:
            return node.elseCode.accept(self, binding)
        
    def evaluate_FnDef(self, node, binding):
        thun = Thunk(node.params, node.body, binding)
        return thun
    
    def evaluate_FnCall(self, node, binding):
        params = []

        for i in node.args:
            params.append(i.accept(self, binding))
        
        thun = node.name.accept(self, binding)
        return thun.accept(self, binding, params)
    
    def evaluate_Thunk(self, node, binding, args):
        outer = node.binding.push()
        # print("evaluating thunk")
        # print("self bind:" + str(self.binding.print()) + " outer:" + str(outer.print()))
        # print("params:" + str(self.params) + "args:" + str(args))
        
        if len(args) < len(node.params):
            raise Exception('Not enough arguments for function')
        elif len(args) > len(node.params):
            raise Exception('Too many arguments for function')
        for key, val in zip(node.params, args):
            outer.set_var(key, val)
            
        result = node.block.accept(self, outer)
        outer.pop()
        return result