import os
from lexer import lexer
from symbol_table import SymbolTable
from errors import ErrorManager
from parser import simple_parser
from codegen import CodeGenerator

with open('input.txt', 'r') as f:
    code = f.read()

symbol_table = SymbolTable()
error_manager = ErrorManager()
codegen = CodeGenerator()

# Eliminar archivo de errores de compilaciones anteriores
if os.path.exists('errors.err'):
    os.remove('errors.err')

try:
    tokens = lexer(code)
    print('TOKENS:', tokens)  # DEBUG: imprimir tokens generados
    simple_parser(tokens, symbol_table, error_manager, codegen)
except SyntaxError as e:
    error_manager.add(str(e))

if error_manager.has_errors():
    print("Errores encontrados. Revisar errors.err")
    error_manager.save_to_file()
else:
    print("Análisis exitoso. Tabla de símbolos:")
    print(symbol_table)
    codegen.save()
    print("Código ensamblador generado en output.asm")