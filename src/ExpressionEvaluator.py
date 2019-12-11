from LangContext import Context


class AddOpEvaluator:
    # Evaluates add or subtract operations

    def __init__(self, lhs, rhs, symbol):
        # take in the values of the expression (lhs and rhs) as well
        # as the symbol specifying the operation
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        # evaluate and return the mathematical result according to the specified symbol
        if self.symbol == "+":
            ans = self.lhs.eval(context) + self.rhs.eval(context)
            return int(ans)
        elif self.symbol == "-":
            ans = self.lhs.eval(context) - self.rhs.eval(context)
            return int(ans)
        else:
            # symbol was not + or -; throw an exception
            raise Exception("Invalid add op encountered.")


class MulOpEvaluator:
    # Evaluates multiply or divide operations

    def __init__(self, lhs, rhs, symbol):
        # take in the values of the expression (lhs and rhs) as well
        # as the symbol specifying the operation
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        # evaluate and return the mathematical result according to the specified symbol
        if self.symbol == "*":
            ans = self.lhs.eval(context) * self.rhs.eval(context)
            return int(ans)
        elif self.symbol == "/":
            ans = self.lhs.eval(context) / self.rhs.eval(context)
            return int(ans)
        else:
            # symbol was not * or /; throw an exception
            raise Exception("Invalid mul op encountered.")


class BooleanEvaluator:
    # Evaluates boolean expressions

    def __init__(self, lhs, rhs, symbol):
        # take in the values of the expression (lhs and rhs) as well
        # as the symbol specifying the operation
        self.lhs = lhs
        self.rhs = rhs
        self.symbol = symbol

    def eval(self, context):
        lhs = int(self.lhs.eval(context))
        rhs = int(self.rhs.eval(context))
        # Based on symbol, check each case, returning the result of
        # the correct comparison
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
