from arpeggio import ParserPython, visit_parse_tree

from SmurfGrammar import program, comment
from LangVisitor import LangVisitor

import sys

# Create Arpeggio parser with grammar definition and comment structure
parser = ParserPython(program, comment)
# File name to run will be the 1st command line parameter
f = sys.argv[1]
# Open with newline=None to avoid carriage return problems on Windows
file = open(f, "r", newline=None)
contents = file.read()

# Parse file with Arpeggio
program = parser.parse(contents)
# Create program AST by visiting the parsed tree

AST = visit_parse_tree(program, LangVisitor(debug=False))
# Execute program by calling eval() on the top node; this will propagate down recursively
# down to the eval() function on terminals
AST.eval()
