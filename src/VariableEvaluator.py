from LangContext import Context


class VariableDeclaration:
    # A variable declaration or list of var declarations

    def __init__(self, declarations):
        self.declarations = declarations

    def eval(self, context):
        for decl in self.declarations:
            # get the terminal value by eval() for the current context
            val = decl.eval(context)
        # return the most recent evaluated val
        return val


class Declaration:
    # A single variable declaration

    def __init__(self, id, value):
        self.id = id
        self.value = value

    def eval(self, context):
        # Set the evaluated var ID and value in the current context
        return context.setVar(self.id.eval(context), self.value.eval(context))


class VarReference:
    # A reference to a variable

    def __init__(self, id):
        self.id = id

    def eval(self, context):
        # get the variable as named from the nearest context
        return context.getVar(self.id)
