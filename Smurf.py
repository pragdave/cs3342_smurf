from arpeggio import ParserPython, visit_parse_tree
import Grammar as grammar
from ASTGenerator import ASTGenerator
from Interpreter import Interpreter

def main():
    #Creates the arpeggio parser
    parser = ParserPython(grammar.code, grammar.comment)
    
    #Reads the smurf source code file
    f = open("code.smu", "r")
    contents = f.read()
    
    #Generates the parse tree
    parse_tree = parser.parse(contents)
    
    #Generates the ast tree
    ast = visit_parse_tree(parse_tree, ASTGenerator())
    
    #Runs the code
    ast.accept(Interpreter())
    
if __name__ == "__main__":
    main()