from arpeggio import PTNodeVisitor

class FunctionVisitor(PTNodeVisitor):
    def visit_function_definition(self, node, children):
        print("Function definition: ")
        node = None
