from arpeggio.cleanpeg import ParserPEG
from arpeggio import ParserPython, visit_parse_tree
from arpeggio.export import PMDOTExporter, PTDOTExporter
import grammar as Grammar
import visitor as Visitor


debug=True

parser = ParserPython(Grammar.program, debug=debug)

parse_tree = parser.parse("let b = 1")

tree = visit_parse_tree(parse_tree, Visitor.Visitor(debug=debug))



