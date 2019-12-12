from bindings import binding

class program:
	#overall code
	def __init__(self, code):
		self.code = code

	def process(self):
		#create starting empty binding that all will be inheriting from
		base = binding(None)
		return self.code.process(base)

class code:
	def __init__(self, statements):
		self.statements = statements

	def process(self, binding):
		for statement in self.statements:
			val = statement.process(binding)
		return val

class terminal:
	#terminal value in the code (integers/literals)
	def __init__(self, val):
		self.val = val

	def process(self, binding):
		return self.val

class conditional:
	#if-else statements
	#decides which is the correct option to run
	def __init__(self, statement, body, alt = None):
		#give a base value of none to alternative so that you can have if without an else
		self.statement = statement
		self.body = body
		self.alt = alt

	def process(self, binding):
		if self.statement.process(binding) != 0:
			return self.body.process(binding)
			#goes through and checks the condition and if true then runs the body
		else:
			if self.alt is not None:
				#make sure there's actually an else statement before trying to run it
				return self.alt.process(binding)

class Assignment:
	def __init__(self, id, expr):
		self.id = id
		self.expr = expr

	def process(self,binding):
		if binding.getVar(self.id.process(binding)) is not None:
			return binding.addVar(self.id.process(binding), self.expr.process(binding))
		else:
			raise Exception("variable not declared")