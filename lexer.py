import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+'),
    ('CHAR',     r"'[a-zA-Z]'"),
    ('ID',       r'[a-zA-Z_]\w*'),
    ('ASSIGN',   r'='),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MULT',     r'\*'),
    ('DIV',      r'/'),
    ('EQ',       r'=='),
    ('NE',       r'!='),
    ('GT',       r'>'),
    ('LT',       r'<'),
    ('AND',      r'&&'),
    ('OR',       r'\|\|'),
    ('NOT',      r'!'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('SEMICOLON',r';'),
    ('COMMENT',  r'//.*'),
    ('SKIP',     r'\s+'),
    ('MISMATCH', r'.')
]

KEYWORDS = {
    'if', 'else', 'while', 'for', 'char', 'int', 'long', 'float', 'double', 'return'
}

token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPEC)

def lexer(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'ID' and value in KEYWORDS:
            kind = value.upper()  # Ej: 'if' -> 'IF', 'char' -> 'CHAR'
        if kind == 'SKIP' or kind == 'COMMENT':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Carácter inesperado: {value}')
        tokens.append((kind, value))
    return tokens