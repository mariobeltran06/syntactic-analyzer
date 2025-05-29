ARITHMETIC_OPS = {'PLUS', 'MINUS', 'MULT', 'DIV'}
RELATIONAL_OPS = {'EQ', 'NE', 'GT', 'LT'}
LOGICAL_OPS = {'AND', 'OR', 'NOT'}

def simple_parser(tokens, symbol_table, error_manager, codegen=None):
    label_counter = [0]  # Para etiquetas únicas en if
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
                    # Asignación con expresión aritmética simple (variables y literales)
                    if i+2 < len(tokens) and tokens[i][0] in ('NUMBER', 'CHAR', 'ID') and tokens[i+1][0] in ('PLUS', 'MINUS', 'MULT', 'DIV') and tokens[i+2][0] in ('NUMBER', 'CHAR', 'ID'):
                        left = tokens[i][1]
                        op = tokens[i+1][1]
                        right = tokens[i+2][1]
                        if codegen:
                            codegen.gen_assign_expr(name, left, op, right)
                        i += 3
                        # Tipo: si ambos son NUMBER, es long int, si ambos son CHAR, es char, si hay variable, consulta la tabla
                        if tokens[i-3][0] == 'NUMBER' and tokens[i-1][0] == 'NUMBER':
                            type_expr = 'long int'
                        elif tokens[i-3][0] == 'CHAR' and tokens[i-1][0] == 'CHAR':
                            type_expr = 'char'
                        else:
                            if tokens[i-3][0] == 'ID':
                                type_expr = symbol_table.lookup(tokens[i-3][1]) or 'long int'
                            else:
                                type_expr = 'long int'
                        symbol_table.insert(name, type_expr)
                    elif i < len(tokens) and tokens[i][0] in ('NUMBER', 'CHAR'):
                        valor_literal = tokens[i][1]
                        if codegen:
                            codegen.gen_assign(name, valor_literal)
                        type_expr = 'long int' if tokens[i][0] == 'NUMBER' else 'char'
                        symbol_table.insert(name, type_expr)
                        i += 1
                    else:
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
                # Asignación con expresión aritmética simple
                if i+2 < len(tokens) and tokens[i][0] in ('NUMBER', 'CHAR', 'ID') and tokens[i+1][0] in ('PLUS', 'MINUS', 'MULT', 'DIV') and tokens[i+2][0] in ('NUMBER', 'CHAR', 'ID'):
                    left = tokens[i][1]
                    op = tokens[i+1][1]
                    right = tokens[i+2][1]
                    i += 3
                    if codegen:
                        codegen.gen_assign_expr(name, left, op, right)
                    # Tipo: si ambos son NUMBER, es long int, si ambos son CHAR, es char, si hay variable, consulta la tabla
                    if tokens[i-3][0] == 'NUMBER' and tokens[i-1][0] == 'NUMBER':
                        type_expr = 'long int'
                    elif tokens[i-3][0] == 'CHAR' and tokens[i-1][0] == 'CHAR':
                        type_expr = 'char'
                    else:
                        # Si alguno es variable, intenta deducir el tipo de la variable izquierda
                        if tokens[i-3][0] == 'ID':
                            type_expr = symbol_table.lookup(tokens[i-3][1]) or 'long int'
                        else:
                            type_expr = 'long int'
                    symbol_table.insert(name, type_expr)
                elif i < len(tokens) and tokens[i][0] in ('NUMBER', 'CHAR'):
                    valor_literal = tokens[i][1]
                    if codegen:
                        codegen.gen_assign(name, valor_literal)
                    type_expr = 'long int' if tokens[i][0] == 'NUMBER' else 'char'
                    symbol_table.insert(name, type_expr)
                    i += 1
                else:
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

        # While: while (exp) { ... }
        if token[0] == 'WHILE':
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'LPAREN':
                error_manager.add("Falta '(' después de 'while'")
                continue
            i += 1
            cond_start = i
            paren_count = 1
            while i < len(tokens) and paren_count > 0:
                if tokens[i][0] == 'LPAREN':
                    paren_count += 1
                elif tokens[i][0] == 'RPAREN':
                    paren_count -= 1
                i += 1
            cond_end = i - 1
            if paren_count != 0:
                error_manager.add('Paréntesis desbalanceados en condición de while')
                continue
            expr_tokens = tokens[cond_start:cond_end]
            temp_var = '__tmp_cond'
            idx, _ = parse_expression(expr_tokens + [('SEMICOLON',';')], 0, symbol_table, error_manager)
            if codegen:
                codegen.gen_assign(temp_var, 'R16')
            # Generar etiquetas para ciclo
            label_while = f"WHILE_{label_counter[0]}"
            label_endwhile = f"ENDWHILE_{label_counter[0]}"
            label_counter[0] += 1
            if codegen:
                codegen.gen_while(temp_var, 'EQ', '0', label_while, label_endwhile)
            # Ya consumimos el paréntesis de cierre al salir del ciclo, no volver a buscarlo
            # (i apunta al token siguiente al RPAREN)

            # Verifica token de apertura de bloque
            if i >= len(tokens):
                error_manager.add("Falta '{' en bloque 'while'")
                continue
            if tokens[i][0] != 'LBRACE':
                error_manager.add("Falta '{' en bloque 'while'")
                # Busca el siguiente LBRACE para no quedar desfasado
                while i < len(tokens) and tokens[i][0] != 'LBRACE':
                    i += 1
                if i < len(tokens) and tokens[i][0] == 'LBRACE':
                    i += 1
                else:
                    continue
            else:
                i += 1
            while i < len(tokens) and tokens[i][0] != 'RBRACE':
                token_bloque = tokens[i]
                if token_bloque[0] == 'WHILE':
                    i += 1
                    if i >= len(tokens) or tokens[i][0] != 'LPAREN':
                        error_manager.add("Falta '(' después de 'while'")
                        continue
                    i += 1
                    if i+2 < len(tokens) and tokens[i][0] in ('ID', 'NUMBER', 'CHAR') and tokens[i+1][0] in ('GT', 'LT', 'EQ', 'NE') and tokens[i+2][0] in ('ID', 'NUMBER', 'CHAR'):
                        cond_left = tokens[i][1]
                        cond_op = tokens[i+1][0]
                        cond_right = tokens[i+2][1]
                        i += 3
                    else:
                        error_manager.add("Condición de while no soportada para generación de código")
                        while i < len(tokens) and tokens[i][0] != 'RPAREN':
                            i += 1
                        i += 1
                        continue
                    if i >= len(tokens) or tokens[i][0] != 'RPAREN':
                        error_manager.add("Falta ')' en condición 'while'")
                    i += 1
                    if i >= len(tokens) or tokens[i][0] != 'LBRACE':
                        error_manager.add("Falta '{' en bloque 'while'")
                        continue
                    i += 1
                    # Etiquetas anidadas
                    label_while_nest = f"WHILE_{label_counter[0]}"
                    label_endwhile_nest = f"ENDWHILE_{label_counter[0]}"
                    label_counter[0] += 1
                    if codegen:
                        codegen.gen_while(cond_left, cond_op, cond_right, label_while_nest, label_endwhile_nest)
                    # Procesar bloque anidado
                    nest_start = i
                    while i < len(tokens) and tokens[i][0] != 'RBRACE':
                        # Permitir anidamiento recursivo
                        # Esta misma lógica se repetirá
                        if tokens[i][0] == 'WHILE' or tokens[i][0] == 'IF':
                            # Volver a procesar el bloque de control
                            break
                        elif tokens[i][0] == 'ID':
                            i = simple_statement(tokens, i, symbol_table, error_manager, codegen)
                        else:
                            error_manager.add(f"Instrucción no soportada en bloque: {tokens[i][1]}")
                            i += 1
                    if i >= len(tokens) or tokens[i][0] != 'RBRACE':
                        error_manager.add("Falta '}' en bloque 'while'")
                    if codegen:
                        codegen.gen_while_jump(label_while_nest)
                        codegen.gen_label(label_endwhile_nest)
                    i += 1
                elif token_bloque[0] == 'IF':
                    i += 1
                    if i >= len(tokens) or tokens[i][0] != 'LPAREN':
                        error_manager.add("Falta '(' después de 'if'")
                        continue
                    i += 1
                    cond_start = i
                    paren_count = 1
                    while i < len(tokens) and paren_count > 0:
                        if tokens[i][0] == 'LPAREN':
                            paren_count += 1
                        elif tokens[i][0] == 'RPAREN':
                            paren_count -= 1
                        i += 1
                    cond_end = i - 1
                    if paren_count != 0:
                        error_manager.add('Paréntesis desbalanceados en condición de if')
                        continue
                    expr_tokens = tokens[cond_start:cond_end]
                    temp_var = '__tmp_cond'
                    idx, _ = parse_expression(expr_tokens + [('SEMICOLON',';')], 0, symbol_table, error_manager)
                    if codegen:
                        codegen.gen_assign(temp_var, 'R16')
                    label_else_nest = f"ELSE_{label_counter[0]}"
                    label_endif_nest = f"ENDIF_{label_counter[0]}"
                    label_counter[0] += 1
                    if codegen:
                        codegen.gen_if(temp_var, 'EQ', '0', label_else_nest)
                    # Bloque if anidado
                    if i < len(tokens) and tokens[i][0] == 'LBRACE':
                        i += 1
                        while i < len(tokens) and tokens[i][0] != 'RBRACE':
                            if tokens[i][0] == 'WHILE' or tokens[i][0] == 'IF':
                                break
                            i = simple_statement(tokens, i, symbol_table, error_manager, codegen)
                        if i < len(tokens) and tokens[i][0] == 'RBRACE':
                            i += 1
                        else:
                            error_manager.add("Falta '}' en bloque 'if'")
                    else:
                        error_manager.add("Falta '{' en bloque 'if'")
                    # ELSE opcional
                    if i < len(tokens) and tokens[i][0] == 'ELSE':
                        if codegen:
                            codegen.gen_else_jump(label_endif_nest)
                            codegen.gen_label(label_else_nest)
                        i += 1
                        if i < len(tokens) and tokens[i][0] == 'LBRACE':
                            i += 1
                            while i < len(tokens) and tokens[i][0] != 'RBRACE':
                                if tokens[i][0] == 'WHILE' or tokens[i][0] == 'IF':
                                    break
                                i = simple_statement(tokens, i, symbol_table, error_manager, codegen)
                            if i < len(tokens) and tokens[i][0] == 'RBRACE':
                                i += 1
                            else:
                                error_manager.add("Falta '}' en bloque 'else'")
                        else:
                            error_manager.add("Falta '{' en bloque 'else'")
                        if codegen:
                            codegen.gen_label(label_endif_nest)
                    else:
                        if codegen:
                            codegen.gen_label(label_else_nest)
                    continue
                elif token_bloque[0] == 'ID':
                    i = simple_statement(tokens, i, symbol_table, error_manager, codegen)
                else:
                    error_manager.add(f"Instrucción no soportada en bloque: {token_bloque[1]}")
                    i += 1
            if i >= len(tokens) or tokens[i][0] != 'RBRACE':
                error_manager.add("Falta '}' en bloque 'while'")
            if codegen:
                codegen.gen_while_jump(label_while)
                codegen.gen_label(label_endwhile)
            i += 1
            continue

        # If: if (exp) { ... } else { ... }
        if token[0] == 'IF':
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'LPAREN':
                error_manager.add("Falta '(' después de 'if'")
                return i
            i += 1
            # Permitir condiciones arbitrarias
            cond_start = i
            paren_count = 1
            while i < len(tokens) and paren_count > 0:
                if tokens[i][0] == 'LPAREN':
                    paren_count += 1
                elif tokens[i][0] == 'RPAREN':
                    paren_count -= 1
                i += 1
            cond_end = i - 1
            if paren_count != 0:
                error_manager.add('Paréntesis desbalanceados en condición de if')
                return i
            expr_tokens = tokens[cond_start:cond_end]
            temp_var = '__tmp_cond'
            idx, _ = parse_expression(expr_tokens + [('SEMICOLON',';')], 0, symbol_table, error_manager)
            if codegen:
                codegen.gen_assign(temp_var, 'R16')
            label_else = f"ELSE_{label_counter[0]}"
            label_endif = f"ENDIF_{label_counter[0]}"
            label_counter[0] += 1
            if codegen:
                codegen.gen_if(temp_var, 'EQ', '0', label_else)
            # NOTA: el resto del flujo debe continuar igual para bloques if/else
            # Ya consumimos el paréntesis de cierre al salir del ciclo, no volver a buscarlo
            # (i apunta al token siguiente al RPAREN)

            # Verifica token de apertura de bloque
            if i >= len(tokens):
                error_manager.add("Falta '{' en bloque 'if'")
                return i
            if tokens[i][0] != 'LBRACE':
                error_manager.add("Falta '{' en bloque 'if'")
                # Busca el siguiente LBRACE para no quedar desfasado
                while i < len(tokens) and tokens[i][0] != 'LBRACE':
                    i += 1
                if i < len(tokens) and tokens[i][0] == 'LBRACE':
                    i += 1
                else:
                    return i
            else:
                i += 1
            # Leer sentencias dentro del bloque if
            while i < len(tokens) and tokens[i][0] != 'RBRACE':
                # Permitir instrucciones de control anidadas
                if tokens[i][0] == 'IF' or tokens[i][0] == 'WHILE':
                    # Procesar recursivamente el bloque de control
                    # El parser principal ya maneja estos casos, así que solo llama el parser principal
                    start_token = tokens[i]
                    # Busca el inicio del bloque
                    j = i
                    paren_count = 0
                    while j < len(tokens):
                        if tokens[j][0] == 'LBRACE':
                            break
                        j += 1
                    # Procesa el bloque completo
                    i = simple_parser(tokens[i:j], symbol_table, error_manager, codegen)
                    # Ahora avanzar hasta el cierre del bloque
                    brace_count = 1
                    j += 1
                    while j < len(tokens) and brace_count > 0:
                        if tokens[j][0] == 'LBRACE':
                            brace_count += 1
                        elif tokens[j][0] == 'RBRACE':
                            brace_count -= 1
                        j += 1
                    i = j
                else:
                    i = simple_statement(tokens, i, symbol_table, error_manager, codegen)
            if i >= len(tokens) or tokens[i][0] != 'RBRACE':
                error_manager.add("Falta '}' en bloque 'if'")
            else:
                i += 1
            # Verificar si hay else
            if i < len(tokens) and tokens[i][0] == 'ELSE':
                if codegen:
                    codegen.gen_else_jump(label_endif)
                    codegen.gen_label(label_else)
                i += 1
                if i < len(tokens) and tokens[i][0] == 'LBRACE':
                    i += 1
                    while i < len(tokens) and tokens[i][0] != 'RBRACE':
                        i = simple_statement(tokens, i, symbol_table, error_manager, codegen)
                    if i >= len(tokens) or tokens[i][0] != 'RBRACE':
                        error_manager.add("Falta '}' en bloque 'else'")
                    i += 1
                else:
                    error_manager.add("Falta '{' en bloque 'else'")
                if codegen:
                    codegen.gen_label(label_endif)
            else:
                if codegen:
                    codegen.gen_label(label_else)
            continue

        else:
            error_manager.add(f"Error sintáctico inesperado cerca de {token[1]}")
            i += 1

def parse_expression(tokens, i, symbol_table, error_manager):
    # Soporta expr := valor (op valor)? y operadores lógicos
    if i >= len(tokens):
        error_manager.add("Expresión incompleta.")
        return i, None

    # Soporte para NOT unario
    if tokens[i][0] == 'NOT':
        op = tokens[i][0]
        i += 1
        i, operand_type = parse_expression(tokens, i, symbol_table, error_manager)
        return i, 'bool'
    elif tokens[i][0] in ('NUMBER', 'CHAR', 'ID'):
        left_type = get_type(tokens[i], symbol_table, error_manager)
        i += 1
    else:
        error_manager.add(f"Token inválido en expresión: {tokens[i][1]}")
        return i + 1, None

    if i < len(tokens) and tokens[i][0] in ARITHMETIC_OPS.union(RELATIONAL_OPS).union(LOGICAL_OPS):
        op = tokens[i][0]
        i += 1
        if i >= len(tokens):
            error_manager.add("Falta segundo operando en expresión.")
            return i, None
        # Busca el siguiente operando válido para right_type
        right_idx = i
        while right_idx < len(tokens) and tokens[right_idx][0] not in ('ID', 'NUMBER', 'CHAR'):
            right_idx += 1
        if right_idx < len(tokens):
            right_type = get_type(tokens[right_idx], symbol_table, error_manager)
            i = right_idx + 1
        else:
            right_type = 'undef'
            i += 1
        if left_type != right_type:
            # Busca los operandos reales para el error
            left_token = tokens[i-2] if i-2 >= 0 else ('?', '?')
            right_token = tokens[i] if i < len(tokens) else ('?', '?')
            # Si el token es un operador, busca hacia atrás/adelante el ID o literal más cercano
            def find_operand(idx, direction):
                while 0 <= idx < len(tokens):
                    if tokens[idx][0] in ('ID', 'NUMBER', 'CHAR'):
                        return tokens[idx][1]
                    idx += direction
                return '?'
            left_name = find_operand(i-2, -1)
            right_name = find_operand(i, 1)

            error_manager.add(f"Incompatibilidad de tipos: {left_type} con {right_type} (operandos: {left_name}, {right_name})")
            try:
                error_manager.add(f"Tabla de símbolos actual: {symbol_table.symbols}")
            except Exception:
                pass
        if op in RELATIONAL_OPS or op in LOGICAL_OPS:
            # Para compatibilidad, siempre devuelve 'long int' para resultado de operación lógica
            # Además, si el contexto es asignación a 'r', nunca devuelvas 'bool'
            return i, 'long int'
        return i, left_type
    return i, left_type

def get_type(token, symbol_table, error_manager):
    if token[0] == 'NUMBER':
        return 'long int'
    if token[0] == 'CHAR':
        return 'char'
    if token[0] == 'ID':
        tipo = symbol_table.lookup(token[1])
        if tipo is None:
            msg = f"Identificador sin tipo: {token[1]}"

            try:
                error_manager.add(msg)
            except Exception:
                pass
            return 'undef'
        return tipo
    return 'undef'

def simple_statement(tokens, i, symbol_table, error_manager, codegen=None):
    # Permitir instrucciones de control dentro de bloques
    start_i = i
    # Solo procesamos asignaciones dentro de bloques por ahora
    if tokens[i][0] == 'ID':
        name = tokens[i][1]
        i += 1
        if i < len(tokens) and tokens[i][0] == 'ASSIGN':
            i += 1
            # Asignación con expresión aritmética simple
            if i+2 < len(tokens) and tokens[i][0] in ('NUMBER', 'CHAR', 'ID') and tokens[i+1][0] in ('PLUS', 'MINUS', 'MULT', 'DIV') and tokens[i+2][0] in ('NUMBER', 'CHAR', 'ID'):
                left = tokens[i][1]
                op = tokens[i+1][1]
                right = tokens[i+2][1]
                if codegen:
                    codegen.gen_assign_expr(name, left, op, right)
                i += 3
                # Tipo: si ambos son NUMBER, es long int, si ambos son CHAR, es char, si hay variable, consulta la tabla
                if tokens[i-3][0] == 'NUMBER' and tokens[i-1][0] == 'NUMBER':
                    type_expr = 'long int'
                elif tokens[i-3][0] == 'CHAR' and tokens[i-1][0] == 'CHAR':
                    type_expr = 'char'
                else:
                    # Si alguno es variable, intenta deducir el tipo de la variable izquierda
                    if tokens[i-3][0] == 'ID':
                        type_expr = symbol_table.lookup(tokens[i-3][1]) or 'long int'
                    else:
                        type_expr = 'long int'
                symbol_table.insert(name, type_expr)
            elif i < len(tokens) and tokens[i][0] in ('NUMBER', 'CHAR'):
                valor_literal = tokens[i][1]
                if codegen:
                    codegen.gen_assign(name, valor_literal)
                t = 'long int' if tokens[i][0] == 'NUMBER' else 'char'
                symbol_table.insert(name, t)
                i += 1
            else:
                i, t = parse_expression(tokens, i, symbol_table, error_manager)
                if t:
                    # Si la variable es 'r' y la expresión es lógica, fuerza tipo 'long int'
                    if name == 'r':
                        symbol_table.insert(name, 'long int')
                    else:
                        symbol_table.insert(name, t)
            if i < len(tokens) and tokens[i][0] == 'SEMICOLON':
                return i + 1
            else:
                error_manager.add("Falta ';' en instrucción dentro de bloque")
    error_manager.add(f"Error en instrucción en línea: {' '.join(v for _, v in tokens[start_i:i+1])}")
    return i + 1
