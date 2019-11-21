from grammar import *
from visitor import *


parser = ParserPython(program,comment)

fileList = [
    "./test_cases/00_expr.smu",
    "./test_cases/01_variables.smu",
    # "./test_cases/02_let.smu",
    "./test_cases/10_if.smu",
    # "./test_cases/20_fn_basic.smu",
    # "./test_cases/21_recursive_fns.smu",
    # "./test_cases/22_closures.smu",
    # "./test_cases/99_fib.smu"
]

for f in fileList:
    file = open(f,"r")
    contents = file.read()


    parse_tree = parser.parse(contents)

    print(parse_tree)

    PTDOTExporter().exportFile(parse_tree,"my_parse_tree.dot")

    solution = visit_parse_tree(parse_tree, SmurfVisitor(debug=False))

    print(solution.evaluate())

# parse_tree = parser.parse("print(99)")

# print(parse_tree)

# PTDOTExporter().exportFile(parse_tree,"my_parse_tree.dot")

# solution = visit_parse_tree(parse_tree, SmurfVisitor(debug=False))

# print(solution.evaluate())
