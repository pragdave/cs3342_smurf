from token.py import Token

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[pos] if self.pos < len(self.text) else None
        
    def read(self):
        self.pos += 1
        #update the current character if the file still has remaining characters
        self.current_char = self.text[pos] if self.pos < len(self.text) else None

    # def token_generator(self):
    #     tokens = []
    #     while 


    #     return tokens