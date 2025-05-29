; Asignación a = 10
LDI R16, 10
STS a, R16
; Asignación b = 5
LDI R16, 5
STS b, R16
; Asignación ch = 'X'
LDI R16, 'X'
STS ch, R16
; Asignación c = a + b
LDS R16, a
LDS R17, b
ADD R16, R17
STS c, R16
; Asignación resultado = a * b
LDS R16, a
LDS R17, b
MUL R16, R17
STS resultado, R16
; Asignación resultado = resultado / 2
LDS R16, resultado
LDI R17, 2
; División: resultado en R0, R1 tras MUL
; (Implementar división real si es necesario)
STS resultado, R16
; Asignación resultado = resultado - 3
LDS R16, resultado
LDI R17, 3
SUB R16, R17
STS resultado, R16
; Asignación flag1 = 1
LDI R16, 1
STS flag1, R16
; Asignación flag2 = 0
LDI R16, 0
STS flag2, R16
; Asignación i = 0
LDI R16, 0
STS i, R16
; Asignación __tmp_cond = R16
LDI R16, R16
STS __tmp_cond, R16
WHILE_0:
; while (__tmp_cond EQ 0)
LDI R16, __tmp_cond
LDI R17, 0
CP R16, R17
BRNE ENDWHILE_0
; Asignación resultado = resultado + i
LDS R16, resultado
LDS R17, i
ADD R16, R17
STS resultado, R16
; Asignación i = i + 1
LDS R16, i
LDI R17, 1
ADD R16, R17
STS i, R16
RJMP WHILE_0
ENDWHILE_0:
; Asignación __tmp_cond = R16
LDI R16, R16
STS __tmp_cond, R16
; if (__tmp_cond EQ 0)
LDS R16, __tmp_cond
LDI R17, 0
CP R16, R17
BRNE ELSE_1
; Asignación c = 100
LDI R16, 100
STS c, R16
RJMP ENDIF_1
ELSE_1:
; Asignación c = 200
LDI R16, 200
STS c, R16
ENDIF_1:
