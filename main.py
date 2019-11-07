from smurf import *
    

def parseNode(node,baseList):
    if type(node) is NonTerminal:
        nodeList = []
        for x in node:
            n = parseNode(x,nodeList)
            if n:
                nodeList.append(n)
        baseList.append(nodeList)        
    else:
        return (node.value,node.rule_name)

parser = ParserPython(program,comment, reduce_tree=True)

result = parser.parse("let fib = fn(n) {\n  if n < 2 {\n    n\n  }\n  else {\n    fib(n-1) + fib(n-2)\n  }\n}\nprint(fib(10))   #=> 55\n")

print(result)
PMDOTExporter().exportFile(parser.parser_model,"PM.dot")
PTDOTExporter().exportFile(result,"PT.dot")

value = visit_parse_tree(result,PTNodeVisitor(debug=False))
print(value)

nodeList = []
parseNode(result,nodeList)
print(nodeList)