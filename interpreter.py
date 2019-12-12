from bindings import *
class Interpreter:
    def __init__(self):
        #THIS TOOK FOREVER BUT EVEUNTAULLY REALIZED THIS WAS THE KEY TO BINDING WITH THE INTERPRETER
        self.binding = Binding()

    def evaluate_program(self, node):
        return node.value.accept(Binding())

    def evaluate_code(self, node):
        for e in node.value:
            value = e.accept(self)
        return value 

    def evaluate_binop(self, node): 
        #SENDS THESE VALUES FOR OPERATIONS
        left = node.left.accept(self)
        right= node.right.accept(self)
        return node.ops[node.op](left, right)


    def evaluate_relop(self, node):
        #SENDS THESE VALUES FOR OPERATIONS
        left = node.left.accept(self)
        right= node.right.accept(self)
        return node.ops[node.op](left, right)


    def evaluate_expr(self, node):
        return node.value.accept(self)


    def evaluate_integer(self, node):
        return node.value


    def evaluate_assignment(self, node):
        value = node.value.accept(self)
        self.binding.set_variable(node.name, value)
        return value     


    def evaluate_variable_reference(self, node):
        return self.binding.get_variable_value(node.name) 


    def evaluate_variable_declaration(self, node):
        for value2 in node.value:
            value = value2.accept(self)
        return value

    def evaluate_decl(self, node):
        nodeOne = node.name
        nodeTwo = node.value.accept(self)

        #SETS THESE TWO NODES THEN SENDS TO BINDING TO BE SET TO BE REMEBERED IN THE BINDING
        return self.binding.set_variable(nodeOne, nodeTwo)

    def evaluate_let_decl(self, node):
        self.binding.set_variable(node.value, None)

#INTERPRETER FOR DEF LOGIC
    def evaluate_function_definition(self, node):
        return Thunk(node.name, node.values, self.binding)

    #INTERPRETER FOR CALL LOGIC
    def evaluate_function_call(self, node):
        values = [value.accept(self) for value in node.values]
        thunk = self.binding.get_variable_value(node.name)
        return thunk.accept(self, values)

    #INTERPRETER FOR THUNK LOGIC
    def evaluate_thunk(self, values):
        binding = node.defining_binding
        binding = binding.push()

        for formal, actual in zip(node.params, actuals):
            self.binding.set_variable(formal, actual)

        result = node.body.accept(binding)
        binding = binding.pop()
        return result

    def evaluate_print_call(self, node):
        #CANT FIGURE OUT HOW TO GET PAST str ERROR SAYS DOSENT HAVE ATTRIBUTE
        values = [value.accept(self) for value in node.value]

        output = "Print: "

        for counter in range(0, len(values)):
            output = output + str(values[counter])
            if counter == len(values) - 1:
                break
            else:
                output = output + "|"

        print(output)
        return values[-1]
