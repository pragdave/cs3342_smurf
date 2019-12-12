from arpeggio import *
from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython
from arpeggio.export import PTDOTExporter
import sys
from arpeggio.cleanpeg import ParserPEG
from visitorAlg import SmurfVisitor
from grammar import *
import os

def main(debug = False):

    #declare the arpeggio parser
    parser = ParserPython(program, comment, debug = debug)

    #command line argument is stored in smurfCode
    smurfCode =""

    #if a command line argument was provided, check if it is a file. If it is, then it will parse, and interpret correctly
    if(len(sys.argv) > 1):
        smurfCode = sys.argv[1]
        try:
            file_object = open(smurfCode, "r")
            smurfCode = file_object.read()
            parsing_tree = parser.parse(smurfCode)
            #this is used if you want to make the png of the tree
            PTDOTExporter().exportFile(parsing_tree, "parse_tree.dot")

            #this will store the AST in result
            result = visit_parse_tree(parsing_tree, SmurfVisitor(debug=False))

            #interprets the AST
            result.eval()
        except:
            try:
                #this block of code will allow the command line arguement to be printed to the console
                smurfCode = smurfCode.replace(" ", "")
                if("#" in smurfCode):
                    smurfCode = smurfCode[:smurfCode.find("#")]
                smurfCode= "print(" + smurfCode +")"
                parsing_tree = parser.parse(smurfCode)
                #this is used if you want to make the png of the tree
                PTDOTExporter().exportFile(parsing_tree, "parse_tree.dot")

                #this will store the AST in result
                result = visit_parse_tree(parsing_tree, SmurfVisitor(debug=False))

                #interprets the AST
                result.eval()
            except:
                print("File does not exist or the smurf syntax was incorrect")
        
if __name__ == "__main__":
    main(debug=False)
