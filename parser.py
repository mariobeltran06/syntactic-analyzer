ARITHMETIC_OPS = {'PLUS', 'MINUS', 'MULT', 'DIV'}
RELATIONAL_OPS = {'EQ', 'NE', 'GT', 'LT'}

def simple_parser(tokens, symbol_table, error_manager):
    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Declaración de variable: tipos compuestos (ej: LONG INT a = ...;)
        type_tokens = []
        while token[0] in ('INT', 'CHAR', 'LONG', 'FLOAT', 'DOUBLE', 'UNSIGNED', 'SIGNED', 'SHORT'):
            type_tokens.append(token[1])
            i += 1
            if i < len(tokens):
                token = tokens[i]
            else:
                break
        if type_tokens:
            var_type = ' '.join(type_tokens).lower()
            if i < len(tokens) and tokens[i][0] == 'ID':
                name = tokens[i][1]
                i += 1
                # Soporta declaración con o sin asignación
                if i < len(tokens) and tokens[i][0] == 'ASSIGN':
                    i += 1
                    i, type_expr = parse_expression(tokens, i, symbol_table, error_manager)
                    if type_expr:
                        symbol_table.insert(name, type_expr)
                    else:
                        symbol_table.insert(name, var_type)
                else:
                    symbol_table.insert(name, var_type)
                if i < len(tokens) and tokens[i][0] == 'SEMICOLON':
                    i += 1
                    continue
                else:
                    error_manager.add("Falta ';' al final de la declaración.")
                    continue
            else:
                error_manager.add("Declaración de variable sin nombre válido.")
                i += 1
                continue

        # Asignación: ID = expresión ;
        if token[0] == 'ID':
            name = token[1]
            i += 1
            if i < len(tokens) and tokens[i][0] == 'ASSIGN':
                i += 1
                i, type_expr = parse_expression(tokens, i, symbol_table, error_manager)
                if type_expr:
                    symbol_table.insert(name, type_expr)
                if i < len(tokens) and tokens[i][0] == 'SEMICOLON':
                    i += 1
                    continue
                else:
                    error_manager.add("Falta ';' al final de la asignación.")
            else:
                error_manager.add(f"Asignación inválida para variable {name}")
                i += 1
            continue

        # If: if (exp) { ... }
        if token[0] == 'IF':
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'LPAREN':
                error_manager.add("Falta '(' después de 'if'")
                continue
            i += 1
            i, _ = parse_expression(tokens, i, symbol_table, error_manager)
            if i >= len(tokens) or tokens[i][0] != 'RPAREN':
                error_manager.add("Falta ')' en condición 'if'")
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'LBRACE':
                error_manager.add("Falta '{' en bloque 'if'")
                continue
            i += 1
            # Leer sentencias dentro del bloque
            while i < len(tokens) and tokens[i][0] != 'RBRACE':
                i = simple_statement(tokens, i, symbol_table, error_manager)
            if i >= len(tokens) or tokens[i][0] != 'RBRACE':
                error_manager.add("Falta '}' en bloque 'if'")
            i += 1
            continue

        else:
            error_manager.add(f"Error sintáctico inesperado cerca de {token[1]}")
            i += 1

def parse_expression(tokens, i, symbol_table, error_manager):
    # Solo soportamos expr := valor (op valor)? para ahora
    if i >= len(tokens):
        error_manager.add("Expresión incompleta.")
        return i, None

    if tokens[i][0] in ('NUMBER', 'CHAR', 'ID'):
        left_type = get_type(tokens[i], symbol_table)
        i += 1
    else:
        error_manager.add(f"Token inválido en expresión: {tokens[i][1]}")
        return i + 1, None

    if i < len(tokens) and tokens[i][0] in ARITHMETIC_OPS.union(RELATIONAL_OPS):
        op = tokens[i][0]
        i += 1
        if i >= len(tokens):
            error_manager.add("Falta segundo operando en expresión.")
            return i, None
        right_type = get_type(tokens[i], symbol_table)
        i += 1
        # Validación semántica simple
        if left_type != right_type:
            error_manager.add(f"Incompatibilidad de tipos: {left_type} con {right_type}")
        if op in RELATIONAL_OPS:
            return i, 'bool'
        return i, left_type
    return i, left_type

def get_type(token, symbol_table):
    if token[0] == 'NUMBER':
        return 'long int'
    if token[0] == 'CHAR':
        return 'char'
    if token[0] == 'ID':
        return symbol_table.lookup(token[1]) or 'undef'
    return 'undef'

def simple_statement(tokens, i, symbol_table, error_manager):
    # Solo procesamos asignaciones dentro de bloques por ahora
    start_i = i
    if tokens[i][0] == 'ID':
        name = tokens[i][1]
        i += 1
        if i < len(tokens) and tokens[i][0] == 'ASSIGN':
            i += 1
            i, t = parse_expression(tokens, i, symbol_table, error_manager)
            if i < len(tokens) and tokens[i][0] == 'SEMICOLON':
                symbol_table.insert(name, t)
                return i + 1
            else:
                error_manager.add("Falta ';' en instrucción dentro de bloque")
    error_manager.add(f"Error en instrucción en línea: {' '.join(v for _, v in tokens[start_i:i+1])}")
    return i + 1
