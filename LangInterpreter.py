class Context:
    def __init__(self, parent):
        self.context = {}
        self.parent = parent

    def setVar(self, name, val):
        self.context[name] = val

    def getVar(self, name):
        if name in self.context:
            return self.context[name]
        else:
            raise Exception("Undefined reference encountered.")


class Terminal:
    def __init__(self, val):
        self.value = val

    def evaluate(self, context):
        return self.value


class AddOpEvaluator:
    def __init__(self, lhs, rhs, symbol):
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        if self.symbol == "+":
            ans = self.lhs.eval(context) + self.rhs.eval(context)
            return int(ans)
        elif self.symbol == "-":
            ans = self.lhs.eval(context) - self.rhs.eval(context)
            return int(ans)
        else:
            raise Exception("Invalid add op encountered.")


class MulOpEvaluator:
    def __init__(self, lhs, rhs, symbol):
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        if self.symbol == "*":
            ans = self.lhs.eval(context) * self.rhs.eval(context)
            return int(ans)
        elif self.symbol == "/":
            ans = self.lhs.eval(context) / self.rhs.eval(context)
            return int(ans)
        else:
            raise Exception("Invalid mul op encountered.")


class BooleanEvaluator:
    def __init__(self, lhs, rhs, symbol):
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        lhs = int(context.eval(lhs))
        rhs = int(context.eval(rhs))
        if self.symbol == "==":
            if lhs == rhs:
                return 1
        elif self.symbol == "<=":
            if lhs <= rhs:
                return 1
        elif self.symbol == ">=":
            if lhs >= rhs:
                return 1
        elif self.symbol == "!=":
            if lhs != rhs:
                return 1
        elif self.symbol == "<":
            if lhs < rhs:
                return 1
        elif self.symbol == ">":
            if lhs > rhs:
                return 1
        return 0
