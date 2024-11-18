from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('NUMBER', r'\bnumber\b')
        self.lexer.add('BOOLEAN', r'\bbool\b')
        self.lexer.add('FUNCTION', r'\bfunction\b')
        self.lexer.add('IF', r'\bif\b')
        self.lexer.add('ELSE', r'\belse\b')
        self.lexer.add('WHILE', r'\bwhile\b')
        self.lexer.add('BREAK', r'\bbreak\b')
        self.lexer.add('UNDERSCORE', r'_')
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*')
        self.lexer.add('LITERAL', r'-?\d+(\.\d+)?|true|false')
        self.lexer.add('TRUE', r'\btrue\b')
        self.lexer.add('FALSE', r'\bfalse\b')
        self.lexer.add('EQ', r'==')
        self.lexer.add('NE', r'!=')
        self.lexer.add('LE', r'<=')
        self.lexer.add('GE', r'>=')
        self.lexer.add('LT', r'<')
        self.lexer.add('GT', r'>')
        self.lexer.add('AND', r'\&\&')
        self.lexer.add('OR', r'\|\|')
        self.lexer.add('ASSIGN', r'=')
        self.lexer.add('LPAREN', r'\(')
        self.lexer.add('RPAREN', r'\)')
        self.lexer.add('LBRACE', r'\{')
        self.lexer.add('RBRACE', r'\}')
        self.lexer.add('SEMICOLON', r';')
        self.lexer.add('COMMA', r',')
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'-')
        self.lexer.add('TIMES', r'\*')
        self.lexer.add('DIVIDE', r'/')
        self.lexer.add('MOD', r'%')
        self.lexer.add('COMMENT', r'//.*')
        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'//.*')  # Ignore single-line comments

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()