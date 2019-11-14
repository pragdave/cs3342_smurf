from arpeggio import ParserPython, visit_parse_tree
import Visitor as visitor
import Grammar as grammar

def main(debug=True):
    parser = ParserPython(grammar.runner, debug=debug)
    
    f = open("code.smu", "r")
    contents = f.read()
    
    parse_tree = parser.parse(contents)
    
    result = visit_parse_tree(parse_tree, visitor.Visitor(debug=debug))
    
if __name__ == "__main__":
    #main(debug=False)
    main()