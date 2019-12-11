from LangContext import Context


class Program:
    # Represents the root node of the program
    def __init__(self, script):
        # Script includes contents of the .smu file
        self.script = script

    def eval(self):
        # create a base "Context" which holds current bindings; it has no parent
        # as this is the root of code execution
        baseContext = Context(None)
        # evaluate script with the base context
        return self.script.eval(baseContext)


class Code:
    # Represents the interpretable code of the .smu file
    def __init__(self, statements):
        self.statements = statements

    def eval(self, context):
        # Execute statements sequentially, return the last thing that is
        # evaluated
        for s in self.statements:
            value = s.eval(context)
        return value


class Terminal:
    # terminal value will be an integer or literal
    def __init__(self, val):
        self.value = val

    def eval(self, context):
        # the end of all eval() recursions (from the AST nodes);
        # this now returns the literal value
        return self.value


class Conditional:
    # if statement with a body and optional alternative
    def __init__(self, condition, body, alternative=None):
        # Note that the default alternative is None; it will only be executed
        # if code is required for the "else" clause
        self.condition = condition
        self.body = body
        self.alternative = alternative

    def eval(self, context):
        if self.condition.eval(context) != 0:
            # check if the condition is true (nonzero)
            return self.body.eval(context)
        else:
            if self.alternative is not None:
                # an "else" body has been provided; evaluate that
                return self.alternative.eval(context)


class Assignment:
    # assignment of var or function; note the id should already be declared
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

    def eval(self, context):
        # Check that the ID is inside the dictionary
        if(context.getVar(self.id.eval(context)) is not None):
            # Set variable inside dictionary of executing context
            return context.setVar(self.id.eval(context), self.expr.eval(context))
        else:
            # Note that this statement should never execute unless a context failed to recognize
            # an undefined var reference (the context should throw the exception; this is a failsafe)
            raise Exception(
                "Variable assignment attempted without declaration.")
