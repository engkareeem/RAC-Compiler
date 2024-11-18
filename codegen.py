from ast_1 import *
def ast_to_json(ast):
    if isinstance(ast, Block):
        return [ast_to_json(statement) for statement in ast.statements]
    elif isinstance(ast, IfStatement):
        return {
            "typ": "if",
            "cond": ast_to_json(ast.condition),
            "true": ast_to_json(ast.true_block),
            "false": ast_to_json(ast.false_block) if ast.false_block else None
        }
    elif isinstance(ast, WhileStatement):
        return {
            "typ": "while",
            "cond": ast_to_json(ast.condition),
            "blk": ast_to_json(ast.body)
        }
    elif isinstance(ast, Break):
        return {
            "typ": "break",
        }
    elif isinstance(ast, FunctionDeclaration):
        return {
            "typ": "func_dcl",
            "nm": ast.name,
            "bdy": ast_to_json(ast.body)
        }
    elif isinstance(ast, FunctionCall):
        return {
            "typ": "func_cll",
            "act": ast.name,
        }
    elif isinstance(ast, GlobalFunctionCall):
        return {
            "typ": "gfunc_cll",
            "act": ast.name,
            "params": [ast_to_json(arg) for arg in ast.arguments]
        }
    elif isinstance(ast, VariableDeclaration):
        return {
            "typ": "var_dcl",
            "d_typ": ast.type,
            "nm": ast.name,
            "val": ast_to_json(ast.value)
        }
    elif isinstance(ast, Assignment):
        return {
            "typ": "assign",
            "nm": ast.name,
            "val": ast_to_json(ast.value)
        }
    elif isinstance(ast, BinaryOp):
        return {
            "lf": ast_to_json(ast.left),
            "op": ast.op,
            "rt": ast_to_json(ast.right)
        }
    elif isinstance(ast, Number):
        return ast.value
    elif isinstance(ast, Identifier):
        return ast.name
    elif isinstance(ast, str) or isinstance(ast, int) or isinstance(ast, float) or isinstance(ast, bool):
        return ast
    else:
        raise ValueError("Unknown AST node type")
