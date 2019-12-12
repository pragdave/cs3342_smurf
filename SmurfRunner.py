from arpeggio import ParserPython, visit_parse_tree

from grammarDef import program, comment
from ASTPather import smurfVisitor

import sys

#create the parser that arpeggio automatically has implemented
arpegParser = ParserPython(program, comment)

#open the given file to run
fileName = sys.argv[1]
file = open(fileName, "r", newline=None)
data = file.read()

#actually parse the file using the parser
program = arpegParser.parse(data)

#create an ast using arpeggios built in code
tree = visit_parse_tree(program, smurfVisitor(debug=False))
#goes through the ast and evaluates each step
tree.process()