from src.LangEvaluator import Context


class PrintFunction:
    def __init__(self, statement):
        self.statement = statement

    def eval(self, context):
        print(self.statement.eval(context))
        return 0


class FunctionDefinition:
    def __init__(self, params, id):
        self.id = id
        self.params = params

    def eval(self, context):
        params = self.params.eval(context)
        var = self.id.eval(context)
        funcContext = Context(var.parent)


class ParamList:
    def __init__(self, params):
        self.params = params

    def eval(self, parentContext):
        paramContext = Context(parentContext)
        for param in self.params:
            paramContext.setVar(param.eval(paramContext))
        return paramContext


class CallArguments:
    def __init__(self, argList):
        self.argList = argList

    def eval(self, context):
        return list(map(lambda arg: arg.eval(context), self.argList))


class FunctionCall:
    def __init__(self, id, args):
        self.id = id
        self.args = args

    def eval(self, parentContext):
        id = self.id.eval(parentContext)
        args = self.args.eval(parentContext)
        funContext = Context(parentContext)
        for arg in args:
            print(arg)
