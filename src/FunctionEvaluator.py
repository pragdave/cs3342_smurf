from LangContext import Context


class PrintFunction:
    # used for the print(..) function built into Smurf
    def __init__(self, statement):
        self.statement = statement

    def eval(self, context):
        # evaluate the output in the current context to get a
        # terminal that can be printed to screen
        output = self.statement.eval(context)
        text = ""
        # format output with pipes delimiting multiple items
        for x in range(0, len(output)-1):
            text += str(output[x]) + "|"
        text += str(output[len(output)-1])
        print(("Print: " + text))
        return 0


class FunctionDefinition:
    # Represents a function definition, has parameters (zero or more) and a body of code

    def __init__(self, params, body):
        self.params = params
        self.body = body

    def eval(self, context):
        # Return the definition with its context (as a tuple),
        # this allows the FunctionCall to execute closures
        return (self.body, self.params, context)


class ParamList:
    # A list of function parameters

    def __init__(self, params):
        self.params = params

    def eval(self, parentContext):
        # Explicit function parameters have their own context, but may reference
        # the parent (calling) context
        paramContext = Context(parentContext)
        for param in self.params:
            # assign the variable inside of the new context
            paramContext.setVar(param.eval(paramContext), None)

        return paramContext


class CallArguments:
    # Parameters specified during the call of a function

    def __init__(self, argList):
        self.argList = argList

    def eval(self, context):
        # Represent the values as a list of outputs
        outputList = []
        for arg in self.argList:
            # evaluate each value to a terminal and add to the outputList
            outputList.append(arg.eval(context))

        return outputList


class FunctionCall:
    # a function call

    def __init__(self, id, args):
        # id is the variable name of the function, used to reference a thunk
        self.id = id
        self.args = args

    def eval(self, parentContext):
        # get the thunk by evaluating the function reference
        thunk = self.id.eval(parentContext)
        # thunk[1] contains the "context" of the parameters,
        # in which the var names are present but all are mapped to 'None' value
        argKeys = thunk[1].eval(parentContext).context
        argVals = self.args.eval(parentContext)

        # raise exception if function is called without the proper number of parameters
        if len(argKeys) != len(argVals):
            raise Exception(
                "Parameter list length did not match function definition.")

        # create a new context for the function execution, parent is the closure / context
        # from the FunctionDefinition
        fContext = Context(thunk[2])

        # map params to context
        i = 0
        for key in argKeys:
            fContext.setVar(key, argVals[i])
            i = i + 1

        # now evaluate the body (thunk[0]) in the fContext
        return thunk[0].eval(fContext)
