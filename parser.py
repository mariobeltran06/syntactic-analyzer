def simple_parser(tokens, symbol_table, error_manager):
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'ID':
            name = token[1]
            i += 1
            if i < len(tokens) and tokens[i][0] == 'ASSIGN':
                i += 1
                if i < len(tokens) and tokens[i][0] in ('NUMBER', 'CHAR'):
                    symbol_table.insert(name, 'long int' if tokens[i][0] == 'NUMBER' else 'char')
                    i += 1
                    if i < len(tokens) and tokens[i][0] == 'SEMICOLON':
                        i += 1
                        continue
                error_manager.add(f"Error semántico en asignación de {name}")
        else:
            error_manager.add(f"Error sintáctico cerca de {token[1]}")
        i += 1
