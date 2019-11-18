from smurf import *
from smurfVisitor import *

# def parseNode(node,baseList):
#     if type(node) is NonTerminal:
#         nodeList = []
#         for x in node:
#             n = parseNode(x,nodeList)
#             if n:
#                 nodeList.append(n)
#         baseList.append(nodeList)        
#     else:
#         return (node.value,node.rule_name)

parser = ParserPython(program,comment,reduce_tree=False)

parseTree = parser.parse("")

# print(parseTree)
PMDOTExporter().exportFile(parser.parser_model,"PM.dot")
PTDOTExporter().exportFile(parseTree,"PT.dot")

myAST = visit_parse_tree(parseTree,SmurfVisitor(debug=False))
#AST.evaluate(Binding())
binding = {}
print(myAST);
print(myAST.evaluate(binding));

# nodeList = []
# parseNode(parseTree,nodeList)
# print(nodeList)