from rply import ParserGenerator
from ast_1 import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'BOOLEAN', 'FUNCTION', 'BREAK', 'IF', 'ELSE', 'WHILE','UNDERSCORE', 'IDENTIFIER', 'LITERAL', 'TRUE', 'FALSE',
             'EQ', 'NE', 'LT', 'GT', 'LE', 'GE', 'AND', 'OR', 'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD'],
            precedence=[
              ('left', ['PLUS', 'MINUS']),
              ('left', ['TIMES', 'DIVIDE', 'MOD']),
               ('left', ['EQ', 'NE', 'LT', 'GT', 'LE', 'GE'])
         ]
)

    def parse(self):
        # Parsing rules 1111
        @self.pg.production('program : statements')
        def program(p):
            return Block(p[0])

        @self.pg.production('statements : statements statement')
        def statements(p):
            return p[0] + [p[1]]

        @self.pg.production('statements : statement')
        def statements_single(p):
            return [p[0]]

        @self.pg.production('statement : variable_declaration SEMICOLON')
        def statement_variable_declaration(p):
            return p[0]

        @self.pg.production('statement : assignment SEMICOLON')
        def statement_assignment(p):
            return p[0]

        @self.pg.production('statement : function_declaration')
        def statement_function_declaration(p):
            return p[0]
        
        @self.pg.production('statement : BREAK SEMICOLON')
        def statement_break(p):
            return Break()
        
        @self.pg.production('statement : global_function_call SEMICOLON')
        def statement_global_function_call(p):
            return p[0]
        
        @self.pg.production('statement : function_call SEMICOLON')
        def statement_function_call(p):
            return p[0]

        @self.pg.production('statement : if_statement')
        def statement_if(p):
            return p[0]

        @self.pg.production('statement : while_statement')
        def statement_while(p):
            return p[0]
        
        @self.pg.production('statement : block')
        def statement_block(p):
            return p[0]
        


        @self.pg.production('block : LBRACE statements RBRACE')
        def block(p):
            return Block(p[1])
        
        


        @self.pg.production('variable_declaration : type IDENTIFIER ASSIGN expression')
        def variable_declaration(p):
            return VariableDeclaration(p[0].getstr(), p[1].getstr(), p[3])

        @self.pg.production('assignment : IDENTIFIER ASSIGN expression')
        def assignment(p):
            return Assignment(p[0].getstr(), p[2])
        
        
        
        @self.pg.production('function_declaration : FUNCTION IDENTIFIER LPAREN RPAREN block')
        def function_declaration(p):
            return FunctionDeclaration(p[1].getstr(), p[4])


 
        @self.pg.production('global_function_call : UNDERSCORE UNDERSCORE IDENTIFIER LPAREN arguments RPAREN')
        def global_function_call(p):
            return GlobalFunctionCall(p[2].getstr(), p[4])
        
        @self.pg.production('function_call : IDENTIFIER LPAREN arguments RPAREN')
        def function_call(p):
            return FunctionCall(p[0].getstr())

        @self.pg.production('arguments : expression COMMA arguments')
        def arguments(p):
            return [p[0]] + p[2]

        @self.pg.production('arguments : expression')
        def arguments_single(p):
            return [p[0]]

        @self.pg.production('arguments : ')
        def arguments_empty(p):
            return []

        @self.pg.production('if_statement : IF LPAREN expression RPAREN block else_block')
        def if_statement(p):
            return IfStatement(p[2], p[4], p[5])

        @self.pg.production('else_block : ELSE block')
        def else_block(p):
            return p[1]

        @self.pg.production('else_block : ')
        def else_block_empty(p):
            return None

        @self.pg.production('while_statement : WHILE LPAREN expression RPAREN block')
        def while_statement(p):
            return WhileStatement(p[2], p[4])
        
        
        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression TIMES expression')
        @self.pg.production('expression : expression DIVIDE expression')
        @self.pg.production('expression : expression MOD expression')
        @self.pg.production('expression : expression EQ expression')
        @self.pg.production('expression : expression NE expression')
        @self.pg.production('expression : expression LT expression')
        @self.pg.production('expression : expression GT expression')
        @self.pg.production('expression : expression LE expression')
        @self.pg.production('expression : expression GE expression')
        @self.pg.production('expression : expression AND expression')
        @self.pg.production('expression : expression OR expression')
        def expression_binary(p):
            return BinaryOp(p[0], p[1].getstr(), p[2])

        @self.pg.production('expression : LITERAL')
        def expression_number(p):
            return Number(p[0].getstr())
        
        @self.pg.production('expression : global_function_call')
        def expression_global_function_call(p):
            return p[0]

        @self.pg.production('expression : IDENTIFIER')
        def expression_identifier(p):
            if p[0].getstr() == 'true':
                return Number("1")
            elif p[0].getstr() == 'false':
                return Number("0")
            else:
                return Identifier(p[0].getstr())

        @self.pg.production('type : NUMBER')
        @self.pg.production('type : BOOLEAN')
        def type(p):
            return p[0]

    def get_parser(self):
        return self.pg.build()