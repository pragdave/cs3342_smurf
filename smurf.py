from sys import argv
import grammar
with open(argv[1]) as file:
    content = file.read()

grammar.runGrammar(content)

# All grammar is defined in grammar.txt and imported/ parsed in grammar.py
