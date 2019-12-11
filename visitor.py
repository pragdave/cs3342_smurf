# from arpeggio import *
# import visitorNodes as node
# class SmurfVisitor(PTNodeVisitor):
#     #result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))
#     def visit_integer(self, node, children):
#         if self.debug:
#             print("Converting {}.".format(node.value))
#         expr = children[0]
#         # print(f"int expr: {expr}")
#         print(f"full expr: {children}")
#         print(f"node.value: {node.value}")
#         # print(f"node.value[0]: {node.value[0]}")
#         # #print(f"node.value[1]: {node.value[1]}")
#         # print(f"node.value.len: {len(node.value)}")
#         # print(f"typeof node.value: {type(node.value)}")
#         # print(f"typeof node.value[0]: {type(node.value[0])}")
#         #print(f"typeof node.value[1]: {type(node.value[1])}")
#         temp = 0
#         print(f"Length of children: {len(children)}")
#         # for i in range(2, len(children), 2):# this will start at 2, go until len(children), and will iterate by 2
#         #   print(f"int loop counter: {i}")
#         #   print(f"Neg Int Children i - 1: {children[i-1]}")
#         #   if i and children[i - 1] == "-":
#         #     print(f"Negative Int")
#         #     temp = int(node.value) * -1
#         #     return temp
#         #   elif i and isinstance(children[i-1], int):
#         #     print(f"Positive Int")
#         #     temp = int(node.value)
#         #     return temp
#         if(children[0] == '-'):
#           print(f"Returning: {int(node.value[4:]) * -1}")
#           return (int(node.value[4:]) * -1)
#         expr = int(node.value)
#         print(f"typeof expr: {type(expr)}")
#         print(f"isinstance expr: {isinstance(expr, int)}")
#         if isinstance(expr, int):
#           print(f"Returning: {int(node.value)}")
#           return int(node.value)
#         print(f"Default Return -1")
#         return -1
#     def visit_mult_term(self, node, children):
#         expr = children[0]
#         for i in range(2, len(children), 2):
#           if i and children[i - 1] == "*":
#             print("Multiplication")
#             expr *= children[i]
#           elif i and children[i-1] == "/":
#             print(f"Division")
#             expr /= children[i]
#         return int(expr)
#     def visit_arithmetic_expression(self, node, children):
#         if self.debug:
#             print("addop {}".format(children))
#         expr = children[0]
#         print(f"arithmetic_expression length: {len(children)}")

#         print(f"arithmetic_expression: {children}")
#         #if children[1]:
#           #print("Children[1]: " + children[1])
#         #if children[0]:
#           #print("Children[0]: " + children[0])
#         #if children[-1]:
#           #print("Children[-1]: " + children[-1])
        
#         for i in range(2, len(children), 2):
#             print(f"i: {i}")
#             print(f"children[i-1]: {children[i - 1]}")
#             if i and children[i - 1] == "-":
#                 expr -= children[i]
#             elif i and children[i - 1] == "+":
#                 expr += children[i]

#         if self.debug:
#             print("addop {}".format(children))
#         return expr
#     # def visit_statement(self, node, children):
#     #   print(f"visit_statement node: {node}")
#     #   print(f"visit_statement children: {children}")

#     # def visit_idk():
#     #   1=1

# class MyLanguageVisitor(PTNodeVisitor):

#   def visit_somerule(self, node, children):
#     if self.debug:
#       print("Visiting some rule!")

# def visit_bar(self, node, children):
#   # Index access
#   child = children[2]

#   # Iteration
#   for child in children:
#     ...

#   # Returns a list of all rules created by PEG rule 'baz'
#   baz_created = children.baz
