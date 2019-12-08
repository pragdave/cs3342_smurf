class BinopNode:
    def __init__(self, left, verb, right):
        self.left = left
        self.verb = verb
        self.right = right

    def __str__(self):
        return f"{self.verb} {self.left} {self.right}"

class IntegerNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value
        
    def __str__(self):
        return str(self.value)

