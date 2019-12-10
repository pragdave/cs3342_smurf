from LangInterpreter import Context


class Program:
    def __init__(self, script):
        self.script = script

    def eval(self):
        baseContext = Context(None)
        return self.script.eval(baseContext)


class Code:
    def __init__(self, statements):
        self.statements = statements

    def eval(self, context):
        for s in self.statements:
            value = s.eval(context)
        return value
