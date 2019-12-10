class AddOpEvaluator:
    lhs = None
    rhs = None
    symbol = None

    def __init__(self, lhs, rhs, symbol):
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        if self.symbol == ""


class BooleanEvaluator:
    lhs = None
    rhs = None
    symbol = None

    def __init__(self, lhs, rhs, symbol):
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        lhs = context.eval(lhs)
        rhs = context.eval(rhs)
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
