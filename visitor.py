from arpeggio import PTNodeVisitor
import tree_nodes as node

class Visitor(PTNodeVisitor):
    
    def visit_integer(self, node, children):
        return node
    
    def visit_expression(self, node, children):
        return node
