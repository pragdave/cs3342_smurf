from arpeggio import *
class SmurfVisitor(PTNodeVisitor):
    #result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))
    def visit_integer(self, node, children):
        if self.debug:
            print("Converting {}.".format(node.value))
        return int(node.value)
    def visit_mult_term(self, node, children):
        expr = children[0]
        for i in range(2, len(children), 2):
          if i and children[i - 1] == "*":
            print("Multiplication")
            expr *= children[i]
          elif i and children[i-1] == "/":
            print(f"Division")
            expr /= children[i]
        return expr
    def visit_arithmetic_expression(self, node, children):
        if self.debug:
            print("addop {}".format(children))
        expr = children[0]
        print(f"arithmetic_expression length: {len(children)}")

        print(f"arithmetic_expression: {children}")
        #if children[1]:
          #print("Children[1]: " + children[1])
        #if children[0]:
          #print("Children[0]: " + children[0])
        #if children[-1]:
          #print("Children[-1]: " + children[-1])
        
        for i in range(2, len(children), 2):
            print(f"i: {i}")
            print(f"children[i-1]: {children[i - 1]}")
            if i and children[i - 1] == "-":
                expr -= children[i]
            elif i and children[i - 1] == "+":
                expr += children[i]

        if self.debug:
            print("addop {}".format(children))
        return expr
    # def visit_idk():
    #   1=1

class MyLanguageVisitor(PTNodeVisitor):

  def visit_somerule(self, node, children):
    if self.debug:
      print("Visiting some rule!")

def visit_bar(self, node, children):
  # Index access
  child = children[2]

  # Iteration
  for child in children:
    ...

  # Returns a list of all rules created by PEG rule 'baz'
  baz_created = children.baz
