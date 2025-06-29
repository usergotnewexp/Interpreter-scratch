## Basic Interpreter with tokenizer
env = {}

def tokenize(code):
    return code.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(tokens):
    if tokens[0] == 'print':
        tokens.pop(0)
    
        if tokens[0] == '(':
            tokens.pop(0)  
            tokens.pop()   
        expr = parse_expr(tokens)
        return ('print', expr)
    elif '=' in tokens:
        var = tokens[0]
        tokens.pop(0)  
        tokens.pop(0)
        expr = parse_expr(tokens)
        return ('assign', var, expr)
    else:
        return parse_expr(tokens)

def parse_expr(tokens):
    if len(tokens) == 1:
        try:
            return int(tokens[0])
        except:
            return ('var', tokens[0])
    else:
        left = tokens[0]
        op = tokens[1]
        right = tokens[2]
        left = int(left) if left.isdigit() else ('var', left)
        right = int(right) if right.isdigit() else ('var', right)
        return (op, left, right)

def evaluation_node(node):
    if isinstance(node, int):
        return node
    if isinstance(node, tuple):
        if node[0] == '+':
            return evaluation_node(node[1]) + evaluation_node(node[2])
        elif node[0] == '*':
            return evaluation_node(node[1]) * evaluation_node(node[2])
        elif node[0] == 'var':
            return env[node[1]]
    return None

def run(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    if ast[0] == 'assign':
        env[ast[1]] = evaluation_node(ast[2])
    elif ast[0] == 'print':
        result = evaluation_node(ast[1])
        print(result)

# Testing the interpreter with a basic syntax 
run("x = 2 + 3")
run("product_all = x * 234")
run("print(product_all)")
print(f"Environment: {env}")  