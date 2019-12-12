import Grammar
import sys

f = open(sys.argv[1],"r")
code = f.read()
Grammar.run(code)