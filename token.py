class Token:
    token_int = 'token_int'
    token_plus = 'token_plus'
    token_minus = 'token_minus'
    token_mult = 'token_mult'
    token_divide = 'token_divide'
    token_lParenthesis = 'token_lParenthesis'
    token_rParenthesis = 'token_rParenthesis'
    def __init__(self, tokenType, value):
        self.tokenType = tokenType
        self.value = value
    def __repr__(self):
        if self.value: return f'{self.tokenType}:{self.value}'
        return f'{self.tokenType}'
        
