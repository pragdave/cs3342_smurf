from arpeggio.cleanpeg import ParserPEG
from arpeggio import ParserPython, visit_parse_tree
from arpeggio.export import PMDOTExporter, PTDOTExporter
import grammar as Grammar
import visitor as Visitor
from interpreter import Interpreter


debug=False

with open('00_expr.smu', 'r') as f:
    source = f.read()
    #print(source)

parser = ParserPython(Grammar.program, Grammar.comment, debug=debug)

parse_tree = parser.parse(source)

tree = visit_parse_tree(parse_tree, Visitor.Visitor(debug=debug))

tree.accept(Interpreter(), {})

