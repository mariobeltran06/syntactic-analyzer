from lexer import lexer
from symbol_table import SymbolTable
from errors import ErrorManager
from parser import simple_parser

with open('input.txt', 'r') as f:
    code = f.read()

symbol_table = SymbolTable()
error_manager = ErrorManager()

try:
    tokens = lexer(code)
    simple_parser(tokens, symbol_table, error_manager)
except SyntaxError as e:
    error_manager.add(str(e))

if error_manager.has_errors():
    print("Errores encontrados. Revisar errors.err")
    error_manager.save_to_file()
else:
    print("Análisis exitoso. Tabla de símbolos:")
    print(symbol_table)