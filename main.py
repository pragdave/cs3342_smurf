from smurf import *
from smurfVisitor import *

parser = ParserPython(program,comment,reduce_tree=False)

parseTree = parser.parse("")

# print(parseTree)
PMDOTExporter().exportFile(parser.parser_model,"PM.dot")
PTDOTExporter().exportFile(parseTree,"PT.dot")

myAST = visit_parse_tree(parseTree,SmurfVisitor(debug=False))
#AST.evaluate(Binding())
binding = Binding({})
print(myAST);
myAST.evaluate()

# nodeList = []
# parseNode(parseTree,nodeList)
# print(nodeList)