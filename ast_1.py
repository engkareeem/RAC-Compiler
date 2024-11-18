class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

class Identifier:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left}, '{self.op}', {self.right})"

class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment({self.name}, {self.value})"

class VariableDeclaration:
    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        if isinstance(value, Number):
            self.value = value
        else:
            self.value = None

    def __repr__(self):
        return f"VariableDeclaration('{self.type}', {self.name}, {self.value})"

class FunctionDeclaration:
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __repr__(self):
        return f"FunctionDeclaration('{self.return_type}', {self.name}, {self.parameters}, {self.body})"
class GlobalFunctionCall:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments
    def __repr__(self):
        return f"GlobalFunctionCall({self.name})"
class FunctionCall:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"FunctionCall({self.name})"

class IfStatement:
    def __init__(self, condition, true_block, false_block):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def __repr__(self):
        return f"IfStatement({self.condition}, {self.true_block}, {self.false_block})"

class WhileStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WhileStatement({self.condition}, {self.body})"

class Block:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Block({self.statements})"
class Break:
    def __repr__(self):
        return "Break()"