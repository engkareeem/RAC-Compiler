import sys
from lexer import Lexer
from parser import Parser
from codegen import ast_to_json
import json
import pyperclip






code = """
function test() {
__setArm(1,2,3,4,5);
}
number x = 0;
bool flag = 1;

while(true) {
test();
if(flag) {
x = x + 1;
} else {
x = x - 1;
}
if(flag >= 10) {
flag = false;
}
__set_arm(x, 10, 0);
__delay(100);
}

"""



lexer = Lexer().get_lexer()
tokens = lexer.lex(code)
pg = Parser()
pg.parse()
parser = pg.get_parser()
ast = parser.parse(tokens)
parsed_json = ast_to_json(ast)
print(json.dumps(parsed_json))    