from LangContext import Context


class VariableDeclaration:
    def __init__(self, declarations):
        self.declarations = declarations

    def eval(self, context):
        for decl in self.declarations:
            val = decl.eval(context)
        return val


class Declaration:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def eval(self, context):
        return context.setVar(self.id.eval(context), self.value.eval(context))


class VarReference:
    def __init__(self, id):
        self.id = id

    def eval(self, context):
        return context.getVar(self.id)
