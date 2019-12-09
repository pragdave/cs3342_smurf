from arpeggio.cleanpeg import ParserPEG
from arpeggio import ParserPython, visit_parse_tree
from arpeggio.export import PMDOTExporter, PTDOTExporter
import grammar as Grammar
import visitor as Visitor


debug=False

with open('00_expr.smu') as f:
    source = f.read

parser = ParserPython(Grammar.program, debug=debug)

parse_tree = parser.parse("1 + 1")

tree = visit_parse_tree(parse_tree, Visitor.Visitor(debug=debug))



