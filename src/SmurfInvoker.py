from LangVisitor import *
from SmurfGrammar import *
import sys


parser = ParserPython(program, comment)
# add debug=True for thorough print and .dot file
# dot -Tpng -O .\program_parse_tree.dot to turn dot to png


f = sys.argv[1]
file = open(f, "r", newline=None)
contents = file.read()
parse_tree = parser.parse(contents)


AST = visit_parse_tree(parse_tree, LangVisitor(debug=True))
AST.eval()
