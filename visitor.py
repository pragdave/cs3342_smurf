class SmurfVisitor(PTNodeVisitor):
    result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))
    def visit_number(self, node, children):
        return float(node.value)

    def visit_factor(self, node, children):
        if len(children) == 1:
            return children[0]
        sign = -1 if children[0] == '-' else 1
        return sign * children[-1]

class MyLanguageVisitor(PTNodeVisitor):

  def visit_somerule(self, node, children):
    if self.debug:
      print("Visiting some rule!")