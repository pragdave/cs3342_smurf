from LangVisitor import *
from SmurfGrammar import *
import sys

# calc is the root rule of your grammar
parser = ParserPython(program, comment)
# Use param debug=True for verbose debugging
# messages and grammar and parse tree visualization
# using graphviz and dot
# add debug=True for thorough print and .dot file
# dot -Tpng -O .\program_parse_tree.dot to turn dot to png


f = sys.argv[1]
file = open(f, 'rU')
contents = file.read()
parse_tree = parser.parse(contents)


AST = visit_parse_tree(parse_tree, LangVisitor(debug=False))
AST.eval()
