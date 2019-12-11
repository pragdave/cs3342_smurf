from src.LangEvaluator import Context


class PrintFunction:
    def __init__(self, statement):
        self.statement = statement

    def eval(self, context):
        print(self.statement.eval(context))
        return 0


class FunctionDefinition:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def eval(self, context):
        return (self.body, self.params, context)


class ParamList:
    def __init__(self, params):
        self.params = params

    def eval(self, parentContext):
        paramContext = Context(parentContext)
        for param in self.params:
            paramContext.setVar(param.eval(paramContext), None)
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
        thunk = self.id.eval(parentContext)
        # thunk[1] contains the "context" of the parameters,
        # in which the var names are present but all are mapped to 'None' value
        argKeys = thunk[1].eval(parentContext).context
        argVals = self.args.eval(parentContext)

        # raise exception if function is called without the proper number of parameters
        if len(argKeys) != len(argVals):
            raise Exception(
                "Parameter list length did not match function definition.")

        # create a new context for the function execution
        fContext = Context(thunk[2])
        i = 0
        for key in argKeys:
            fContext.setVar(key, argVals[i])
            i = i + 1
        return thunk[0].eval(fContext)
