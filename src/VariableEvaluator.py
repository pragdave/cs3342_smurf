from src.LangEvaluator import Context


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
