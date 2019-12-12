from bindings import binding
#file with definitions for all the things that are needed for everything

class arithmetic_expression:
	#evaluates mathmatical expressions

	#define the left and right sides and the symbol to evaluate them on
	def __init__(self, left, right, symbol):
		self.left = left
		self.right = right
		self.symbol = symbol

	def process(self, binding):
		#evaluate the statement based on symbol
		if self.symbol == "+":
			ans = self.left.process(binding) + self.right.process(binding)
			return int(ans)
		elif self.symbol == "-":
			ans = self.left.process(binding) - self.right.process(binding)
			return int(ans)
		elif self.symbol == "*":
			ans = self.left.process(binding) * self.right.process(binding)
			return int(ans)
		elif self.symbol == "/":
			ans = self.left.process(binding) / self.right.process(binding)
			return int(ans)
		else:
			raise Exception("invalid operation found")

class booleval:
	#evaluates boolean expressions

	#define the left and right sides and the symbol to evaluate them on
	def __init__(self, left, right, symbol):
		self.left = left
		self.right = right
		self.symbol = symbol

	def process(self,binding):
		#evaluate both sides so you dont need to reevaluate for each check
		left = int(self.left.process(binding))
		right = int(self.right.process(binding))

		#go through possible symbols and evaluate if correct
		#return 1 if true and 0 if false
		if self.symbol == "==":
			if left == right:
				return 1
		elif self.symbol == "!=":
			if left != right:
				return 1
		elif self.symbol == ">=":
			if left >= right:
				return 1
		elif self.symbol == "<=":
			if left <= right:
				return 1
		elif self.symbol == "<":
			if left < right:
				return 1
		elif self.symbol == ">":
			if left > right:
				return 1
		#if you made it all the way through the if-else statements and didnt already return then you were false
		return 0

class varDec:
	def __init__(self,decls):
		self.decls = decls

	def process(self, binding):
		for decl in self.decls:
			val = decl.process(binding)
		return val

class Declaration:
	def __init__(self, id, val):
		self.id = id
		self.val = val

	def process(self, binding):
		return binding.setVar(self.id.process(binding), self.val.process(binding))

class Ref:
	def __init__(self, id):
		self.id = id
	def process(self, binding):
		return binding.getVar(self.id)

class PrintFunction:
    def __init__(self, statement):
        self.statement = statement

    def process(self, binding):
        info = self.statement.process(binding)
        out = ""
		#put text in correct formatting
        for spot in range(0, len(info)-1):
            out += str(info[spot]) + "|"
        out += str(info[len(info)-1])
        print(("Print: " + out))
        return 0


class FunctionDefinition:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def process(self, binding):
        return (self.body, self.params, binding)


class ParamList:
    def __init__(self, params):
        self.params = params

    def process(self, ownerbinding):
        parambinding = binding(ownerbinding)
        for param in self.params:
            parambinding.setVar(param.process(parambinding), None)

        return parambinding


class CallArguments:
    def __init__(self, argList):
        self.argList = argList

    def process(self, binding):
        info = []
        for arg in self.argList:
            info.append(arg.process(binding))

        return info


class FunctionCall:

    def __init__(self, id, args):
        self.id = id
        self.args = args

    def process(self, ownerbinding):
        id_info = self.id.process(ownerbinding)
        argnames = id_info[1].process(ownerbinding).binding
        argVals = self.args.process(ownerbinding)

 
        if len(argnames) != len(argVals):
            raise Exception("wrong number of params")

        functionbinding = binding(id_info[2])

        # add parameters to the new binding
		#need the extra variable to keep track of correct position
        i = 0
        for name in argnames:
            functionbinding.setVar(name, argVals[i])
            i = i + 1

        #finally calculate in the actual correct binding
        return id_info[0].process(functionbinding)