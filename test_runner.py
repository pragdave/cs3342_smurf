# python test_runner.py «path to interpreter»
import sys, re
import os, os.path
from subprocess import Popen, PIPE
import shlex

def get_expected(path):
  print(f"Got to get_expected!")
  with open(path) as f:
    content = f.read()
  return [ v for _,v in re.findall(r'(#=>\s*)(.+)', content, re.M) ]

def normalize(output):
  print(f"Got to normalize!")
  return [ v for _,v in re.findall(r'(Print:\s*)(.+)\n', output, re.M) ]

def compare(stdout, expected):
  print("Got to compare!")
  output = normalize(stdout)
  if output != expected:
    print("Expected:", expected)
    print("Actual:  ", output)
    print("\n")



interpreter = shlex.split(sys.argv[1])
print(f"interpreter: {interpreter}")
test_files  = [
  path
  for path in os.listdir(".")
  if os.path.isfile(path) and re.search(r'\.smu$', path)
]

for program in test_files:
  print(f"Got to testing")
  expected = get_expected(program)
  process = Popen(interpreter + [ program], stdout=PIPE, stderr=PIPE)
  stdout, stderr = process.communicate()
  print(program)
  if len(stderr) > 0:
    print(stderr.decode("ASCII"))
    print("\n")
  else:
    compare(stdout.decode('ASCII'), expected)
