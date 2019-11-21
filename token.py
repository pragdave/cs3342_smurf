class Token:
    token_int = 'token_int'
    token_plus = 'token_plus'
    token_minus = 'token_minus'
    token_mult = 'token_mult'
    token_divide = 'token_divide'
    token_equals = 'token_equals'
    token_notEquals = 'token_notEquals'
    token_greaterThenOrEquals = 'token_greaterThenOrEquals'
    token_greaterThen = 'token_lessThen'
    token_lessThenOrEquals = 'token_lessThenOrEquals'
    token_lessThen = 'token_lessThen'
    token_lParenthesis = 'token_lParenthesis'
    token_rParenthesis = 'token_rParenthesis'
    def __init__(self, tokenType, value):
        self.tokenType = tokenType
        self.value = value
    def __repr__(self):
        if self.value: return f'{self.tokenType}:{self.value}'
        return f'{self.tokenType}'
    
        
