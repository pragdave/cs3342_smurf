from arpeggio.cleanpeg import ParserPEG, visit_parse_tree
import sys

sys.path.append("~/Desktop/Junior_Year/ProgLang/finalproject/cs3342_smurf/")
from ast import Visitor
from interpreter import *

grammar = ""
file = open("./grammar.txt", "r")
grammar = file.read()

def runGrammar(program):
  parser = ParserPEG(grammar, "program", "comment", debug=False)
  tree = parser.parse(program)
  solution = visit_parse_tree(tree, Visitor(debug=False))
  solution.evaluate(Interpreter())
