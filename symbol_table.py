class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, type_):
        self.symbols[name] = type_

    def lookup(self, name):
        return self.symbols.get(name)

    def __repr__(self):
        return str(self.symbols)