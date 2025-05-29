; Asignación a = 5
LDI R16, 5
STS a, R16
; Asignación x = 10
LDI R16, 10
STS x, R16
; Asignación y = 10
LDI R16, 10
STS y, R16
; if (x EQ y)
LDI R16, x
LDI R17, y
CP R16, R17
BRNE ELSE_0
; Asignación z = x * 2
LDS R16, x
LDI R17, 2
MUL R16, R17
STS z, R16
RJMP ENDIF_0
ELSE_0:
; Asignación z = y / 2
LDS R16, y
LDI R17, 2
; División: resultado en R0, R1 tras MUL
; (Implementar división real si es necesario)
STS z, R16
ENDIF_0:
; Asignación i = 0
LDI R16, 0
STS i, R16
; Asignación j = 0
LDI R16, 0
STS j, R16
WHILE_1:
; while (i LT 2)
LDI R16, i
LDI R17, 2
CP R16, R17
BRGE ENDWHILE_1
; Asignación j = 0
LDI R16, 0
STS j, R16
WHILE_2:
; while (j LT 2)
LDI R16, j
LDI R17, 2
CP R16, R17
BRGE ENDWHILE_2
; Asignación j = j + 1
LDS R16, j
LDI R17, 1
ADD R16, R17
STS j, R16
RJMP WHILE_2
ENDWHILE_2:
; Asignación i = i + 1
LDS R16, i
LDI R17, 1
ADD R16, R17
STS i, R16
RJMP WHILE_1
ENDWHILE_1:
; if (a LT y)
LDI R16, a
LDI R17, y
CP R16, R17
BRGE ELSE_3
; Asignación z = a + y
LDS R16, a
LDS R17, y
ADD R16, R17
STS z, R16
RJMP ENDIF_3
ELSE_3:
; Asignación z = a - y
LDS R16, a
LDS R17, y
SUB R16, R17
STS z, R16
ENDIF_3:
