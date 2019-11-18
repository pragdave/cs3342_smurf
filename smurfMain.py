from smurfGrammar import *
from smurfVisitor import *

fileList = [
    "test_cases/00_expr.smu",
    "test_cases/01_variables.smu",
    "test_cases/02_let.smu",
    "test_cases/10_if.smu",
    "test_cases/20_fn_basic.smu",
    "test_cases/21_recursive_fns.smu",
    "test_cases/22_closures.smu",
    "test_cases/99_fib.smu"
]

parser = ParserPython(program,comment,reduce_tree=False)

for f in fileList:
    print()
    file = open(f,"r")
    contents = file.read()

    parseTree = parser.parse(contents)
    myAST = visit_parse_tree(parseTree,SmurfVisitor(debug=False))
    myAST.evaluate()