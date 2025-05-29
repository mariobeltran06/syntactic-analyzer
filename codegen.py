class CodeGenerator:
    def __init__(self):
        self.lines = []

    def emit(self, line):
        self.lines.append(line)

    def save(self, filename="output.asm"):
        with open(filename, "w") as f:
            for line in self.lines:
                f.write(line + "\n")

    def gen_assign(self, var, value):
        # Asignación simple: variable = valor
        self.emit(f"; Asignación {var} = {value}")
        self.emit(f"LDI R16, {value}")
        self.emit(f"STS {var}, R16")

    def gen_expression(self, left, op=None, right=None):
        # Permite operandos que sean literales o variables
        def operand_code(operand, reg):
            if isinstance(operand, str) and (operand.isdigit() or (operand.startswith("'") and operand.endswith("'"))):
                self.emit(f"LDI {reg}, {operand}")
            else:
                self.emit(f"LDS {reg}, {operand}")
        if op is None:
            operand_code(left, "R16")
            return "R16"
        operand_code(left, "R16")
        operand_code(right, "R17")
        if op == '+':
            self.emit("ADD R16, R17")
        elif op == '-':
            self.emit("SUB R16, R17")
        elif op == '*':
            self.emit("MUL R16, R17")
        elif op == '/':
            self.emit("; División: resultado en R0, R1 tras MUL")
            self.emit("; (Implementar división real si es necesario)")
        return "R16"

    def gen_assign_expr(self, var, left, op=None, right=None):
        self.emit(f"; Asignación {var} = {left} {op if op else ''} {right if right else ''}")
        self.gen_expression(left, op, right)
        self.emit(f"STS {var}, R16")

    def gen_while(self, cond_left, cond_op, cond_right, label_while, label_endwhile):
        self.emit(f"{label_while}:")
        self.emit(f"; while ({cond_left} {cond_op} {cond_right})")
        self.emit(f"LDI R16, {cond_left}")
        self.emit(f"LDI R17, {cond_right}")
        if cond_op == 'GT':
            self.emit("CP R16, R17")
            self.emit(f"BRLE {label_endwhile}")
        elif cond_op == 'LT':
            self.emit("CP R16, R17")
            self.emit(f"BRGE {label_endwhile}")
        elif cond_op == 'EQ':
            self.emit("CP R16, R17")
            self.emit(f"BRNE {label_endwhile}")
        elif cond_op == 'NE':
            self.emit("CP R16, R17")
            self.emit(f"BREQ {label_endwhile}")

    def gen_while_jump(self, label_while):
        self.emit(f"RJMP {label_while}")

    def gen_if(self, cond_left, cond_op, cond_right, label_else):
        # Soporte para if con else: salta a label_else si la condición es falsa
        self.emit(f"; if ({cond_left} {cond_op} {cond_right})")
        self.emit(f"LDI R16, {cond_left}")
        self.emit(f"LDI R17, {cond_right}")
        # cond_op puede ser el nombre del token: 'GT', 'LT', 'EQ', 'NE'
        if cond_op == 'GT':
            self.emit("CP R16, R17")
            self.emit(f"BRLE {label_else}")
        elif cond_op == 'LT':
            self.emit("CP R16, R17")
            self.emit(f"BRGE {label_else}")
        elif cond_op == 'EQ':
            self.emit("CP R16, R17")
            self.emit(f"BRNE {label_else}")
        elif cond_op == 'NE':
            self.emit("CP R16, R17")
            self.emit(f"BREQ {label_else}")

    def gen_else_jump(self, label_endif):
        self.emit(f"RJMP {label_endif}")

    def gen_label(self, label):
        self.emit(f"{label}:")

    def gen_comment(self, comment):
        self.emit(f"; {comment}")
