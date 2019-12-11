from src.LangEvaluator import Context


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


class Conditional:
    # if statement with a body and optional alternative
    def __init__(self, condition, body, alternative=None):
        self.condition = condition
        self.body = body
        self.alternative = alternative

    def eval(self, context):
        if self.condition.eval(context) != 0:
            return self.body.eval(context)
        else:
            if self.alternative is not None:
                return self.alternative.eval(context)


class Assignment:
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def eval(self, context):
        return context.setVar(self.id.eval(context), self.expr.eval(context))
