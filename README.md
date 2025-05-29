
<div align="center">

# 🚀 Compilador Didáctico en Python / Educational Compiler in Python

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Visitas](https://visitor-badge.laobi.icu/badge?page_id=mariobeltran06.syntactic-analyzer)](https://github.com/mariobeltran06/syntactic-analyzer)

[🇪🇸 Español](#índice) | [🇬🇧 English](#table-of-contents)

Un compilador educativo desarrollado en Python para la materia de Autómatas y Compiladores. Implementa un lenguaje de programación estructurado con generación de código ensamblador.

An educational compiler developed in Python for the Automata and Compilers course. Implements a structured programming language with assembly code generation.

</div>

<a id="índice"></a>
## 📑 Índice / Table of Contents

### 📋 Introducción / Introduction
- [Características Principales / Key Features](#-características-principales--key-features)
- [Requisitos del Sistema / System Requirements](#-requisitos--requirements)
- [Instalación / Installation](#-instalación--installation)
- [Ejecución / Execution](#-ejecución--execution)

### 🛠️ Características Técnicas / Technical Features
- [Análisis Léxico / Lexical Analysis](#análisis-léxico--lexical-analysis)
- [Análisis Sintáctico / Syntactic Analysis](#análisis-sintáctico--syntactic-analysis)
- [Sistema de Tipos / Type System](#sistema-de-tipos--type-system)
- [Optimizaciones / Optimizations](#optimizaciones--optimizations)
- [Generación de Código / Code Generation](#generación-de-código--code-generation)

### 📚 Guías / Guides
- [Ejemplos de Uso / Usage Examples](#-ejemplos-avanzados--advanced-examples)
- [Manejo de Errores / Error Handling](#-manejo-de-errores--error-handling)
- [Flujo de Compilación / Compilation Flow](#-flujo-de-compilación-detallado--detailed-compilation-flow)

### 🤝 Contribución / Contributing
- [Política de Contribución / Contribution Policy](#-política-de-contribución--contribution-policy)
- [Código de Conducta / Code of Conduct](#-código-de-conducta--code-of-conduct)
- [Reportar Problemas / Report Issues](#soporte-y-contacto--support-and-contact)

### 📚 Documentación / Documentation
- [Documentación Técnica / Technical Documentation](#documentación-técnica--technical-documentation)
- [Referencias Rápidas / Quick References](#guías-de-referencia-rápida--quick-reference-guides)
- [Recursos de Aprendizaje / Learning Resources](#recursos-de-aprendizaje--learning-resources)

---

## 🎯 Características Principales / Key Features

### 📊 Tipos de Datos / Data Types
- **Tipos numéricos / Numeric Types**:
  - `int` - Enteros básicos / Basic integers
  - `long int` - Enteros de 64 bits / 64-bit integers
  - `float` - Números de punto flotante / Floating point numbers
  - `double` - Precisión doble / Double precision
  - `char` - Caracteres ASCII / ASCII characters

### 🔄 Requisitos del Sistema / System Requirements

#### 📋 Mínimos / Minimum
- Python 3.6 o superior / or higher
- 4GB RAM
- 500MB de espacio en disco / of disk space
- Sistema operativo: Windows 10/11, macOS 10.15+, o Linux / OS: Windows 10/11, macOS 10.15+, or Linux

#### 📊 Recomendados / Recommended
- Python 3.8+
- 8GB RAM
- 1GB de espacio en disco / of disk space
- Procesador de 4 núcleos / 4-core processor

#### 📦 Dependencias / Dependencies
```bash
# Instalación / Installation
pip install -r requirements.txt
```

Lista de dependencias principales / Main dependencies list:
- PLY (Python Lex-Yacc)
- colorama (para colores en consola / for console colors)
- pytest (para pruebas / for testing)

#### 🌐 Compatibilidad / Compatibility
| Sistema Operativo / OS | Versión Mínima / Min Version | Estado / Status |
|------------------------|----------------------------|-----------------|
| Windows               | 10                         | ✅ Soportado / Supported    |
| macOS                | 10.15 (Catalina)           | ✅ Soportado / Supported    |
| Linux                | Ubuntu 18.04+              | ✅ Soportado / Supported    |
| WSL                  | WSL 2                      | ✅ Soportado / Supported    |


#### 🔍 Prerequisitos / Prerequisites
1. Git instalado / Git installed
2. Python 3.6+ configurado correctamente / properly configured
3. Acceso a internet para descargar dependencias / Internet access for dependencies
4. Terminal o línea de comandos / Terminal or command line access

#### 🛠️ Configuración Adicional / Additional Setup
- **Variables de entorno / Environment variables**:
  ```bash
  # Ejemplo / Example
  export PYTHONPATH=$PYTHONPATH:/ruta/al/proyecto
  ```

- **Entorno virtual recomendado / Recommended virtual environment**:
  ```bash
  # Crear entorno / Create environment
  python -m venv venv
  # Activar / Activate
  # Windows
  .\venv\Scripts\activate
  # Unix/macOS
  source venv/bin/activate
  ```

### 📊 Tipos de Datos
- **Tipos numéricos**:
  - `int` - Enteros básicos
  - `long int` - Enteros de 64 bits
  - `float` - Números de punto flotante
  - `double` - Precisión doble
  - `char` - Caracteres individuales
  - `signed`/`unsigned` - Modificadores de tipo
- **Booleanos**: Soporte implícito en expresiones lógicas
- **Inferencia de tipos** en expresiones aritméticas
- **Conversión implícita** entre tipos numéricos

### 🎮 Estructuras de Control / Control Structures

#### Condicionales `if-else` / `if-else` Statements
```c
if (condición / condition) {
    // bloque de código si la condición es verdadera
    // code block if condition is true
} else {
    // bloque de código si la condición es falsa
    // code block if condition is false
}
```

#### Bucles `while` / `while` Loops
```c
while (condición / condition) {
    // bloque de código que se repite mientras la condición sea verdadera
    // code block that repeats while the condition is true
}
```

#### Bucles `for` / `for` Loops
```c
for (inicialización / initialization; 
     condición / condition; 
     actualización / update) {
    // bloque de código que se ejecuta en cada iteración
    // code block that runs on each iteration
}
```

#### Sentencia `switch` / `switch` Statement
```c
switch (expresión / expression) {
    case valor1 / value1:
        // código para valor1
        // code for value1
        break;
    case valor2 / value2:
        // código para valor2
        // code for value2
        break;
    default:
        // código por defecto si no hay coincidencias
        // default code if no matches
}
```

#### Características / Features:
- **Bloques de código / Code Blocks**: Delimitados por llaves `{ }` / Delimited by curly braces `{ }`
- **Anidamiento / Nesting**: Soporte para estructuras anidadas / Support for nested structures
- **Condiciones compuestas / Compound Conditions**: Uso de operadores lógicos (`&&`, `||`, `!`) / Using logical operators (`&&`, `||`, `!`)
- **Variables de control / Control Variables**: Soporte para variables de control en bucles / Support for loop control variables

### 🔧 Operadores / Operators

| Categoría / Category | Operadores / Operators          | Ejemplo de Uso / Usage Example         |
|----------------------|----------------------------------|----------------------------------------|
| Aritméticos / Arithmetic | `+`, `-`, `*`, `/`, `%`         | `a = b + c * 2;` (suma y multiplicación) / (addition and multiplication) |
| Relacionales / Relational | `==`, `!=`, `<`, `>`, `<=`, `>=` | `if (a > b && b != 0) { ... }` (comparaciones) / (comparisons) |
| Lógicos / Logical    | `&&` (AND), `||` (OR), `!` (NOT) | `if (flag1 || !flag2) { ... }` (operaciones lógicas) / (logical operations) |
| Asignación / Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | `a += 5;` (equivalente a `a = a + 5;`) / (equivalent to `a = a + 5;`) |
| Incremento/Decremento / Increment/Decrement | `++`, `--` | `i++;` o `--j;` (incremento/decremento) / (increment/decrement) |
| Ternario / Ternary   | `condición ? valor1 : valor2`     | `max = (a > b) ? a : b;` (operador condicional) / (conditional operator) |
| Tamaño / Sizeof     | `sizeof(tipo)`                   | `int size = sizeof(int);` (tamaño en bytes) / (size in bytes) |
| Agrupación / Grouping | `( )`                          | `result = (a + b) * c;` (forzar precedencia) / (force precedence) |

#### Notas / Notes:
- Los operadores siguen las reglas de precedencia estándar de C / Operators follow standard C precedence rules
- Se pueden usar paréntesis para forzar la precedencia / Parentheses can be used to force precedence
- Los operadores de asignación devuelven el valor asignado / Assignment operators return the assigned value

#### Precedencia de Operadores / Operator Precedence

| Nivel / Level | Operadores / Operators | Descripción / Description |
|--------------|------------------------|---------------------------|
| 1 | `( )` | Paréntesis / Parentheses |
| 2 | `!` `-` | Negación lógica, menos unario / Logical NOT, unary minus |
| 3 | `*` `/` `%` | Multiplicación, división, módulo / Multiplication, division, modulo |
| 4 | `+` `-` | Suma, resta / Addition, subtraction |
| 5 | `<` `<=` `>` `>=` | Comparaciones relacionales / Relational comparisons |
| 6 | `==` `!=` | Igualdad, desigualdad / Equality, inequality |
| 7 | `&&` | AND lógico / Logical AND |
| 8 | `||` | OR lógico / Logical OR |
| 9 | `=` `+=` `-=` `*=` `/=` `%=` | Asignación / Assignment |

**Nota / Note:** Los operadores en el mismo nivel tienen la misma precedencia y se evalúan de izquierda a derecha. / Operators in the same level have equal precedence and are evaluated left to right.

## ✨ Características Avanzadas / Advanced Features

### 📝 Sintaxis Clara / Clear Syntax
- Declaración de variables con/sin inicialización / Variable declaration with/without initialization
- Comentarios de una línea con `//` / Single-line comments with `//`
- Punto y coma (`;`) como terminador de instrucción / Semicolon (`;`) as statement terminator

### 🛠️ Características Técnicas Avanzadas / Advanced Technical Features

#### Análisis Léxico / Lexical Analysis
- **Patrones de tokens / Token Patterns**:
  ```python
  TOKEN_SPEC = [
      # Números y caracteres / Numbers and characters
      ('NUMBER',   r'\d+'),
      ('CHAR',     r'\'[a-zA-Z]\''),
      # Identificadores / Identifiers
      ('ID',       r'[a-zA-Z_]\w*'),
      # Operadores aritméticos / Arithmetic operators
      ('PLUS',     r'\+'),
      ('MINUS',    r'-'),
      ('MULT',     r'\*'),
      ('DIV',      r'/'),
      # Operadores de comparación / Comparison operators
      ('EQ',       r'=='),
      ('NE',       r'!='),
      ('LT',       r'<'),
      ('GT',       r'>'),
      # ... más tokens / more tokens
  ]
  ```
- **Palabras reservadas / Reserved words**:
  - Control de flujo / Flow control: `if`, `else`, `while`, `for`
  - Tipos de datos / Data types: `int`, `long`, `float`, `double`, `char`
  - Retorno / Return: `return`
  - Valores booleanos / Boolean values: `true`, `false`
  - Nulo / Null: `null`

#### Análisis Sintáctico / Syntax Analysis
- **Gramática soportada / Supported Grammar**:
  ```
  // Estructura del programa / Program structure
  program        → declaration* EOF;
  declaration    → varDecl | statement;
  
  // Declaraciones / Declarations
  varDecl        → type IDENTIFIER ("=" expression)? ";";
  
  // Sentencias / Statements
  statement      → exprStmt | ifStmt | whileStmt | block;
  exprStmt       → expression ";";
  ifStmt         → "if" "(" expression ")" statement ("else" statement)?;
  whileStmt      → "while" "(" expression ")" statement;
  block          → "{" declaration* "}";
  
  // Expresiones / Expressions
  expression     → assignment;
  assignment     → IDENTIFIER "=" assignment | equality;
  equality       → comparison ( ( "!=" | "==" ) comparison )*;
  comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )*;
  term          → factor ( ( "-" | "+" ) factor )*;
  factor        → unary ( ( "/" | "*" | "%" ) unary )*;
  unary         → ( "!" | "-" ) unary | primary;
  primary       → NUMBER | CHAR | IDENTIFIER | "true" | "false"
                 | "(" expression ")" | "null";
  ```

- **Manejo de precedencia / Precedence Handling**: 
  - Implementación del algoritmo de precedencia de operadores de Pratt
  - Implementation of Pratt's operator precedence parsing algorithm
  
- **Recuperación de errores / Error Recovery**:
  - Estrategias de sincronización / Synchronization strategies
  - Modo pánico para recuperación / Panic mode recovery
  - Mensajes de error descriptivos / Descriptive error messages

#### Sistema de Tipos / Type System
- **Tipado estático** con inferencia de tipos / **Static typing** with type inference
- **Reglas de conversión / Conversion rules**:
  - Promoción numérica implícita / Implicit numeric promotion
  - Verificación de tipos en tiempo de compilación / Compile-time type checking
  - Compatibilidad de tipos en operaciones binarias / Type compatibility in binary operations
  - Comprobación de tipos en asignaciones / Type checking in assignments
  - Conversiones explícitas requeridas donde sea necesario / Explicit casts required where needed
- **Tipos soportados / Supported types**:
  - `int`, `long`, `float`, `double` - Tipos numéricos / Numeric types
  - `char` - Caracteres individuales / Single characters
  - `bool` - Valores booleanos (`true`/`false`) / Boolean values
  - `void` - Tipo sin retorno / No return type
  - `null` - Valor nulo / Null value

#### Optimizaciones / Optimizations
- **Optimizaciones a nivel local / Local optimizations**:
  - Propagación de constantes / Constant propagation
  - Eliminación de código muerto / Dead code elimination
  - Simplificación algebraica / Algebraic simplification
  - Reducción de fuerza / Strength reduction
  - Plegado de constantes / Constant folding
  - Propagación de copias / Copy propagation

- **Optimizaciones de bucles / Loop optimizations**:
  - Movimiento de código invariante / Loop-invariant code motion
  - Desenrollado de bucles / Loop unrolling
  - Fusión de bucles / Loop fusion
  - Intercambio de bucles / Loop interchange
  - Fusión de bucles / Loop fusion
  - Extracción de invariantes / Loop-invariant code motion

- **Optimizaciones a nivel de función / Function-level optimizations**:
  - Inline de funciones pequeñas / Inlining of small functions
  - Eliminación de código inalcanzable / Unreachable code elimination
  - Propagación de constantes interprocedural / Interprocedural constant propagation

- **Optimizaciones de memoria / Memory optimizations**:
  - Asignación de registros / Register allocation
  - Reordenación de accesos a memoria / Memory access reordering
  - Eliminación de cargas/almacenamientos redundantes / Redundant load/store elimination

#### Generación de Código / Code Generation
- **Código intermedio / Intermediate code**:
  - Representación de tres direcciones / Three-address code (TAC)
  - Formato: `result = operand1 op operand2`
  - Uso de temporales para resultados intermedios / Using temporaries for intermediate results

- **Selección de instrucciones / Instruction selection**:
  - Mapeo a ensamblador x86 / Mapping to x86 assembly
  - Soporte para diferentes conjuntos de instrucciones / Support for different instruction sets
  - Optimización de instrucciones / Instruction optimization

- **Asignación de registros / Register allocation**:
  - Algoritmo de grafos de interferencia / Graph coloring register allocation
  - Uso de registros callee-saved y caller-saved / Using callee-saved and caller-saved registers
  - Derrame a memoria cuando es necesario / Spilling to memory when necessary

- **Estrategias de llamadas / Calling conventions**:
  - Convenciones de llamada estándar / Standard calling conventions
  - Paso de parámetros / Parameter passing
  - Manejo del marco de pila / Stack frame management
  - Convención de nombres para enlazado / Name mangling for linking

- **Optimizaciones específicas / Target-specific optimizations**:
  - Uso de instrucciones SIMD / Using SIMD instructions
  - Alineación de datos / Data alignment
  - Predicción de saltos / Branch prediction hints
  - Prefetching de datos / Data prefetching

## 🚨 Manejo de Errores / Error Handling

El compilador detecta y reporta diversos tipos de errores:  
The compiler detects and reports various types of errors:

### Errores Léxicos / Lexical Errors
- Símbolos no reconocidos / Unrecognized symbols
- Caracteres inválidos / Invalid characters
- Comentarios no cerrados / Unclosed comments
- Identificadores inválidos / Invalid identifiers
- Literales numéricos mal formados / Malformed numeric literals

### Errores Sintácticos / Syntax Errors
- Estructuras mal formadas / Malformed structures
- Puntos y coma faltantes / Missing semicolons
- Paréntesis/llaves no balanceados / Unbalanced parentheses/braces
- Expresiones mal formadas / Malformed expressions
- Palabras clave faltantes / Missing keywords
- Orden de tokens incorrecto / Incorrect token order

### Errores Semánticos / Semantic Errors
- Variables no declaradas / Undeclared variables
- Tipos incompatibles / Incompatible types
- Uso incorrecto de operadores / Incorrect operator usage
- Redefinición de variables / Variable redefinition
- Argumentos de función incorrectos / Incorrect function arguments
- Tipos de retorno no coincidentes / Mismatched return types
- Uso de variables no inicializadas / Use of uninitialized variables

## 🎓 Ejemplos Avanzados / Advanced Examples

### Expresiones Complejas / Complex Expressions
```c
// Expresiones aritméticas complejas / Complex arithmetic expressions
long int resultado = (a + b) * (c - d) / 2;

// Expresiones booleanas complejas / Complex boolean expressions
int es_valido = (edad >= 18) && (tiene_licencia != 0);
```

### Estructuras Anidadas / Nested Structures
```c
// Anidamiento de estructuras de control / Nested control structures
if (x > 0) {
    while (y < 10) {
        if (z == 0) {
            // Código anidado / Nested code
            // Aquí puede ir más lógica / More logic can go here
        }
    }
}
```

### Operaciones con Tipos Mixtos / Mixed Type Operations
```c
// Conversión implícita de tipos / Implicit type conversion
int entero = 10;           // Entero / Integer
double decimal = 3.14;     // Punto flotante / Floating point

// La conversión se realiza automáticamente / Conversion happens automatically
double resultado = entero * decimal;  // entero se convierte a double / integer is converted to double

// Conversión explícita / Explicit casting
int truncado = (int)decimal;  // resultado: 3 / result: 3
```

### Manejo de Cadenas / String Handling
```c
// Concatenación de cadenas / String concatenation
char saludo[] = "Hola, ";
char nombre[] = "Mundo";
// Se requiere una función de biblioteca para concatenar / Library function needed for concatenation
// strcat(saludo, nombre);  // Resultado: "Hola, Mundo"

// Longitud de cadena / String length
int longitud = strlen(saludo);  // Devuelve la longitud sin el nulo final / Returns length without null terminator
```

## 🔄 Flujo de Compilación Detallado / Detailed Compilation Flow

### 1. Análisis Léxico (Lexer) / Lexical Analysis
- **Entrada / Input**: Cadena de caracteres del código fuente / Source code character stream
- **Proceso / Process**:
  1. Escaneo del texto de entrada / Scanning input text
  2. Identificación de lexemas / Identifying lexemes
  3. Clasificación en tokens / Token classification
  4. Eliminación de espacios en blanco y comentarios / Removing whitespace and comments
- **Salida / Output**: Secuencia de tokens con información de ubicación / Token sequence with location information

### 2. Análisis Sintáctico (Parser) / Syntax Analysis
- **Entrada / Input**: Secuencia de tokens del lexer / Token sequence from lexer
- **Proceso / Process**:
  1. Verificación de la estructura gramatical / Verifying grammatical structure
  2. Construcción del árbol de sintaxis abstracta (AST) / Building abstract syntax tree (AST)
  3. Validación de reglas de producción / Validating production rules
  4. Manejo de errores sintácticos / Handling syntax errors
- **Salida / Output**: Árbol de sintaxis abstracta (AST) / Abstract syntax tree (AST)

### 3. Análisis Semántico / Semantic Analysis
- **Entrada / Input**: AST del analizador sintáctico / AST from syntax analyzer
- **Proceso / Process**:
  1. Comprobación de tipos / Type checking
  2. Validación de declaraciones / Declaration validation
  3. Resolución de nombres / Name resolution
  4. Comprobación de alcance / Scope checking
  5. Conversiones de tipo implícitas / Implicit type conversions
- **Salida / Output**: AST anotado con información semántica / AST annotated with semantic information

### 4. Generación de Código Intermedio / Intermediate Code Generation
- **Entrada / Input**: AST anotado / Annotated AST
- **Proceso / Process**:
  1. Recorrido del AST / AST traversal
  2. Generación de código de tres direcciones / Three-address code generation
  3. Gestión de la tabla de símbolos / Symbol table management
  4. Asignación de direcciones de memoria / Memory address allocation
- **Salida / Output**: Código de tres direcciones optimizado / Optimized three-address code

### 5. Optimización / Optimization
- **Técnicas aplicadas / Applied techniques**:
  - Eliminación de código muerto / Dead code elimination
  - Propagación de constantes / Constant propagation
  - Simplificación algebraica / Algebraic simplification
  - Optimización de bucles / Loop optimization
  - Asignación de registros / Register allocation
  - Inline de funciones / Function inlining
  - Eliminación de subexpresiones comunes / Common subexpression elimination

### 6. Generación de Código Final / Final Code Generation
- **Entrada / Input**: Código intermedio optimizado / Optimized intermediate code
- **Proceso / Process**:
  1. Selección de instrucciones / Instruction selection
  2. Asignación de registros / Register allocation
  3. Planificación de instrucciones / Instruction scheduling
  4. Generación de código objeto / Object code generation
  
  5. Manejo de llamadas al sistema / System call handling
  6. Gestión de la pila de llamadas / Call stack management
  7. Optimizaciones específicas de la arquitectura / Architecture-specific optimizations

- **Salida / Output**: Código ensamblador x86 / x86 assembly code

## 📊 Estadísticas del Proyecto / Project Statistics

| Categoría / Category | Detalles / Details |
|----------------------|-------------------|
| **Líneas de código / Lines of code** | ~500 |
| **Archivos fuente / Source files** | 6 |
| **Tipos de tokens soportados / Supported token types** | 20+ |
| **Estructuras de control / Control structures** | 2+ |
| **Operadores soportados / Supported operators** | 15+ |
| **Generación de Código / Code Generation** | Salida en ensamblador legible / Human-readable assembly output |
| **Lenguaje objetivo / Target language** | x86 Assembly |
| **Lenguaje fuente / Source language** | C-like language |

### 🎓 Propósitos Educativos / Educational Purposes
- **Aprendizaje / Learning**: Ideal para aprender sobre compiladores / Perfect for learning about compilers
- **Código abierto / Open Source**: Código abierto y bien documentado / Open source and well-documented
- **Extensible / Extensible**: Fácil de extender con nuevas características / Easy to extend with new features
- **Módulos / Modules**: Estructura modular para mejor comprensión / Modular structure for better understanding
- **Comentarios / Comments**: Código ampliamente comentado / Extensively commented code
- **Ejemplos / Examples**: Incluye ejemplos de entrada/salida / Includes input/output examples

## 🏗️ Estructura del Proyecto / Project Structure

### 🔍 Componentes Principales / Main Components

#### `main.py` - Punto de Entrada / Entry Point
- Inicializa todos los componentes del compilador / Initializes all compiler components
- Gestiona el flujo de ejecución / Manages execution flow
- Coordina las fases de análisis y generación de código / Coordinates analysis and code generation phases
- Maneja la entrada/salida de archivos / Handles file I/O operations

#### `lexer.py` - Analizador Léxico / Lexical Analyzer
- **Patrones de tokens / Token Patterns**: Expresiones regulares para identificar elementos léxicos / Regular expressions to identify lexical elements
- **Palabras reservadas / Reserved Words**: Manejo de palabras clave del lenguaje / Handling language keywords
- **Gestión de posición / Position Tracking**: Seguimiento de línea y columna para mensajes de error / Line and column tracking for error messages
- **Tokens soportados / Supported Tokens**:
  - Identificadores y palabras clave / Identifiers and keywords
  - Literales numéricos y de caracteres / Numeric and character literals
  - Operadores y símbolos especiales / Operators and special symbols
  - Comentarios de una línea / Single-line comments

#### `parser.py` - Analizador Sintáctico/Semántico / Parser/Semantic Analyzer
- **Gramática / Grammar**: Implementación de la gramática del lenguaje / Implementation of the language grammar
- **Árbol de sintaxis / Syntax Tree**: Construcción de la representación jerárquica / Building the hierarchical representation
- **Reglas semánticas / Semantic Rules**: Verificación de tipos y contexto / Type and context verification
- **Estructuras soportadas / Supported Structures**:
  - Declaraciones de variables / Variable declarations
  - Expresiones aritméticas y lógicas / Arithmetic and logical expressions
  - Estructuras de control de flujo / Control flow structures
  - Bloques de código anidados / Nested code blocks

#### `symbol_table.py` - Tabla de Símbolos / Symbol Table
- **Gestión de ámbitos / Scope Management**: Manejo de bloques anidados / Handling nested blocks
- **Tipado fuerte / Strong Typing**: Almacenamiento de tipos de variables / Variable type storage
- **Resolución de nombres / Name Resolution**: Búsqueda en múltiples ámbitos / Search across multiple scopes
- **Métodos principales / Main Methods**:
  - `insert()`: Añade un nuevo símbolo / Adds a new symbol
  - `lookup()`: Busca un símbolo / Looks up a symbol
  - `enter_scope()`/`exit_scope()`: Gestión de ámbitos / Scope management

#### `codegen.py` - Generador de Código / Code Generator
- **Generación de código intermedio / Intermediate Code Generation**: Código ensamblador legible / Human-readable assembly code
- **Gestión de registros / Register Management**: Asignación eficiente de registros / Efficient register allocation
- **Optimizaciones básicas / Basic Optimizations**: Constante folding, eliminación de código muerto / Constant folding, dead code elimination
- **Secciones generadas / Generated Sections**:
  - Segmento de datos (`.data`) / Data segment
  - Segmento de código (`.text`) / Code segment
  - Constantes y variables globales / Constants and global variables

#### `errors.py` - Manejo de Errores / Error Handling
- **Clasificación de errores / Error Classification**: Léxicos, sintácticos, semánticos / Lexical, syntax, semantic
- **Mensajes descriptivos / Descriptive Messages**: Explicaciones claras de los errores / Clear error explanations
- **Ubicación precisa / Precise Location**: Línea y columna del error / Line and column of the error
- **Recuperación / Recovery**: Capacidad de continuar el análisis tras errores / Ability to continue analysis after errors

### 📁 Archivos de Entrada/Salida / Input/Output Files

| Archivo / File | Propósito / Purpose | Formato / Format |
|----------------|---------------------|------------------|
| `input.txt` | Código fuente a compilar / Source code to compile | Texto plano con sintaxis del lenguaje / Plain text with language syntax |
| `output.asm` | Código ensamblador generado / Generated assembly code | Ensamblador x86 / x86 Assembly |
| `errors.err` | Registro de errores / Error log | Texto con mensajes de error / Text with error messages |

## 🛠️ Manejo de Errores / Error Handling

El compilador incluye un sistema robusto de manejo de errores que:  
The compiler includes a robust error handling system that:

- Detecta y reporta múltiples errores por compilación / Detects and reports multiple errors per compilation
- Incluye información detallada sobre la ubicación del error / Includes detailed information about error location
- Genera un archivo `errors.err` con todos los errores encontrados / Generates an `errors.err` file with all found errors
- Maneja errores de diferentes tipos: léxicos, sintácticos y semánticos / Handles different error types: lexical, syntactic, and semantic
- Permite la recuperación de errores para continuar el análisis / Provides error recovery to continue analysis
- Incluye códigos de error únicos para cada tipo de problema / Includes unique error codes for each issue type
- Proporciona mensajes de error claros y sugerencias de solución / Provides clear error messages and solution suggestions

## 🚀 Ejecución / Execution

1. Coloca tu código en `input.txt` / Place your code in `input.txt`
   ```c
   // Ejemplo / Example
   int main() {
       int x = 10;
       return x * 2;
   }
   ```

2. Ejecuta el compilador: / Run the compiler:
   ```bash
   python3 main.py
   ```

3. Revisa la salida: / Check the output:
   - `output.asm`: Código ensamblador generado / Generated assembly code
   - `errors.err`: Errores encontrados (si los hay) / Errors found (if any)

### Opciones de Línea de Comandos / Command Line Options

| Opción / Option | Descripción / Description |
|-----------------|---------------------------|
| `-i <archivo>` | Especifica archivo de entrada / Specify input file |
| `-o <archivo>` | Especifica archivo de salida / Specify output file |
| `-v` | Modo verboso / Verbose mode |
| `-h` | Muestra ayuda / Show help |

### Ejemplo de Uso / Usage Example

```bash
# Compilar con archivos personalizados / Compile with custom files
python3 main.py -i mi_codigo.txt -o salida.asm

# Habilitar modo verboso / Enable verbose mode
python3 main.py -v
```

## 🤝 Contribución / Contributing

¡Las contribuciones son bienvenidas! Por favor:  
Contributions are welcome! Please follow these steps:

### Guía de Contribución / Contribution Guide

1. **Haz un fork del repositorio** / **Fork the repository**
   - Crea tu copia del proyecto / Create your copy of the project
   - Clónala localmente / Clone it locally
   ```bash
   git clone https://github.com/tu-usuario/syntactic-analyzer.git
   cd syntactic-analyzer
   ```

2. **Configura el entorno** / **Set up the environment**
   - Crea un entorno virtual / Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
   - Instala dependencias / Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. **Crea una rama** / **Create a branch**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   # o / or
   git checkout -b fix/corrige-error
   ```

4. **Haz tus cambios** / **Make your changes**
   - Sigue las guías de estilo / Follow style guides
   - Añade pruebas cuando sea necesario / Add tests when applicable
   - Actualiza la documentación / Update documentation

5. **Haz commit de tus cambios** / **Commit your changes**
   ```bash
   git add .
   git commit -m 'Añade nueva funcionalidad / Add new feature'
   ```

6. **Haz push a la rama** / **Push to the branch**
   ```bash
   git push origin feature/nueva-funcionalidad
   ```

7. **Abre un Pull Request** / **Open a Pull Request**
   - Describe tus cambios / Describe your changes
   - Menciona problemas relacionados / Mention related issues
   - Espera la revisión / Wait for review

### Estilo de Código / Code Style
- Sigue PEP 8 para Python / Follow PEP 8 for Python
- Usa nombres descriptivos / Use descriptive names
- Comenta tu código / Comment your code
- Mantén las líneas bajo 80 caracteres / Keep lines under 80 characters

### Reporte de Errores / Bug Reports
Por favor incluye / Please include:
1. Pasos para reproducir / Steps to reproduce
2. Comportamiento esperado / Expected behavior
3. Comportamiento actual / Actual behavior
4. Versión del compilador / Compiler version
5. Sistema operativo / Operating system

## 📝 Licencia / License

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Términos de Uso / Terms of Use

#### Uso Aceptable / Acceptable Use
- **Permitido / Allowed**:
  - Uso personal y educativo / Personal and educational use
  - Modificación del código / Code modification
  - Distribución de copias / Distribution of copies
  - Uso comercial / Commercial use

- **Requisitos / Requirements**:
  - Incluir aviso de derechos de autor / Include copyright notice
  - Incluir copia de la licencia / Include copy of the license
  - No responsabilidad del autor / No author liability

#### Limitaciones / Limitations
- Sin garantía de ningún tipo / No warranty of any kind
- El autor no es responsable por daños / Author not liable for damages
- Sin garantía de idoneidad / No fitness for a particular purpose

#### Atribución / Attribution
```
Syntactic Analyzer
Copyright (c) 2023 [Tu Nombre]

Licencia MIT: https://opensource.org/licenses/MIT
```

### Política de Privacidad / Privacy Policy
Este proyecto no recopila ni almacena información personal. / This project does not collect or store personal information.

---

Desarrollado con ❤️ para la materia de Autómatas y Compiladores - UDB  
Developed with ❤️ for the Automata and Compilers course - UDB

## Requisitos / Requirements

### Requisitos del Sistema / System Requirements

#### Mínimos / Minimum
- **Sistema Operativo / Operating System**:
  - Windows 10/11, macOS 10.15+, o Linux moderno / Windows 10/11, macOS 10.15+, or modern Linux
- **Procesador / CPU**: 1.8 GHz o más rápido / 1.8 GHz or faster
- **Memoria RAM / Memory**: 4 GB (8 GB recomendado) / 4 GB (8 GB recommended)
- **Espacio en Disco / Disk Space**: 200 MB de espacio disponible / 200 MB available space

### Dependencias de Software / Software Dependencies

#### Principales / Core
- **Python 3.8+**
  - [Descargar Python](https://www.python.org/downloads/) / [Download Python](https://www.python.org/downloads/)
  - Verificar instalación: `python --version` / Check installation: `python --version`

#### Bibliotecas / Libraries
- **PLY (Python Lex-Yacc) 3.11+**
  - Instalación: `pip install ply` / Installation: `pip install ply`
  - Verificar versión: `python -c "import ply; print(ply.__version__)"`

#### Herramientas Recomendadas / Recommended Tools
- **Git** - Control de versiones / Version control
- **Visual Studio Code** - Editor de código recomendado / Recommended code editor
  - Extensiones útiles / Useful extensions:
    - Python
    - Pylance
    - GitLens

### Configuración del Entorno / Environment Setup

1. **Clonar el repositorio** / **Clone the repository**
   ```bash
   git clone https://github.com/mariobeltran06/syntactic-analyzer.git
   cd syntactic-analyzer
   ```

2. **Crear y activar entorno virtual** / **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias** / **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar la instalación** / **Verify installation**
   ```bash
   python -m pytest tests/
   ```

### Solución de Problemas / Troubleshooting

#### Error: Módulo no encontrado / Module not found
```bash
# Si falta alguna dependencia / If any dependency is missing
pip install -r requirements.txt
```

#### Error: Versión de Python incompatible / Incompatible Python version
```bash
# Verificar versión / Check version
python --version

# Instalar versión compatible / Install compatible version
# Visitar / Visit: https://www.python.org/downloads/
```

### Notas Adicionales / Additional Notes

1. **Comentarios / Comments**:
   - Usa `//` para comentarios de una línea / Use `//` for single-line comments
   - Usa `/* */` para comentarios de múltiples líneas / Use `/* */` for multi-line comments

2. **Convenciones de Nombrado / Naming Conventions**:
   - Variables: `nombre_variable` (snake_case)
   - Constantes: `NOMBRE_CONSTANTE` (UPPER_SNAKE_CASE)
   - Funciones: `nombre_funcion()` (snake_case)
   - Tipos: `TipoDato` (PascalCase)

3. **Buenas Prácticas / Best Practices**:
   - Siempre inicializa las variables / Always initialize variables
   - Usa nombres descriptivos / Use descriptive names
   - Comenta el código complejo / Comment complex code
   - Mantén las líneas cortas (máx 80 caracteres) / Keep lines short (max 80 chars)
   - Usa sangría consistente / Use consistent indentation

## 👥 Equipo de Desarrollo / Development Team

### Líder del Proyecto / Project Leader
- **Josseline Esmeralda Martínez Hernández** (MH180422)  
  *Arquitectura del Compilador y Gestión del Proyecto*  
  *Compiler Architecture and Project Management*

### Desarrolladores Principales / Core Developers
- **Mario Josue Beltrán Garcia** (BG171969)  
  *Analizador Léxico y Sistema de Manejo de Errores*  
  *Lexical Analyzer and Error Handling System*

- **Sergio Andres Argueta Motto** (AM180450)  
  *Analizador Sintáctico y Generación de Código*  
  *Syntactic Analyzer and Code Generation*

- **Nestor Javier Artiga Larin** (AL160682)  
  *Optimizaciones y Pruebas*  
  *Optimizations and Testing*

- **José Manuel Figueroa Aguilar** (FA200209)  
  *Documentación y Soporte*  
  *Documentation and Support*

### 📋 Términos de Uso / Terms of Use

1. **Uso Educativo / Educational Use**  
   Este software está diseñado principalmente con fines educativos.  
   This software is primarily designed for educational purposes.

2. **Atribución / Attribution**  
   Se debe dar crédito a los autores originales en cualquier uso o derivación.  
   Original authors must be credited in any use or derivative work.

3. **Sin Garantía / No Warranty**  
   El software se proporciona "tal cual", sin garantías de ningún tipo.  
   The software is provided "as is", without warranty of any kind.

4. **Responsabilidad / Liability**  
   Los autores no son responsables de ningún daño derivado del uso del software.  
   The authors are not liable for any damages arising from the use of the software.

### 📄 Política de Contribución / Contribution Policy

1. **Proceso / Process**  
   Las contribuciones son bienvenidas a través de Pull Requests.  
   Contributions are welcome through Pull Requests.

2. **Estilo de Código / Code Style**  
   Todo el código debe seguir las guías de estilo establecidas.  
   All code must follow the established style guides.
   - Usar 4 espacios para indentación / Use 4 spaces for indentation
   - Seguir PEP 8 para Python / Follow PEP 8 for Python
   - Documentar funciones y clases / Document functions and classes

3. **Revisión / Code Review**  
   Se requiere revisión de al menos dos mantenedores para fusionar cambios.  
   At least two maintainers must review before merging changes.

4. **Reporte de Problemas / Issue Reporting**  
   Los issues deben seguir la plantilla proporcionada.  
   Issues must follow the provided template.
   - Describir el problema claramente / Describe the issue clearly
   - Incluir pasos para reproducir / Include steps to reproduce
   - Especificar versión del software / Specify software version

5. **Código de Conducta / Code of Conduct**  
   Todos los contribuyentes deben adherirse a nuestro [Código de Conducta](CODE_OF_CONDUCT.md).  
   All contributors must adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

## 📚 Documentación Adicional

### Documentación Técnica
🔗 [Documentación Técnica en DeepWiki](https://deepwiki.com/mariobeltran06/syntactic-analyzer/6.2-system-integration)  
Documentación detallada sobre la arquitectura, diseño y decisiones técnicas del compilador.

### Guías de Referencia Rápida
- [Guía de Instalación Rápida](#-instalación--installation)
- [Referencia de la Sintaxis](#-características-principales--key-features)
- [Códigos de Error Comunes](#-manejo-de-errores--error-handling)
- [Ejemplos de Uso](#-ejemplos-avanzados--advanced-examples)

### 🔧 Instalación / Installation

#### 📥 Método 1: Usando pip (Recomendado) / Using pip (Recommended)
```bash
# Instalar desde el repositorio / Install from repository
pip install git+https://github.com/mariobeltran06/syntactic-analyzer.git

# O descargar y luego instalar / Or download and then install
git clone https://github.com/mariobeltran06/syntactic-analyzer.git
cd syntactic-analyzer
pip install .
```

#### 🛠️ Método 2: Modo Desarrollo / Development Mode
```bash
# Clonar el repositorio / Clone the repository
git clone https://github.com/mariobeltran06/syntactic-analyzer.git
cd syntactic-analyzer

# Crear y activar entorno virtual / Create and activate virtual environment
python -m venv venv
# Windows / .\venv\Scripts\activate
# Unix/macOS / source venv/bin/activate

# Instalar dependencias / Install dependencies
pip install -r requirements-dev.txt  # Incluye dependencias de desarrollo / Includes dev dependencies

# Instalar en modo desarrollo / Install in development mode
pip install -e .
```

#### 📦 Dependencias / Dependencies
El archivo `requirements.txt` incluye: / The `requirements.txt` file includes:
```
# Análisis / Analysis
ply==3.11           # Herramienta de análisis léxico y sintáctico / Lex and yacc parsing tools

# Desarrollo / Development
black==22.3.0       # Formateador de código / Code formatter
isort==5.10.1       # Ordenamiento de imports / Import sorter
mypy==0.961         # Chequeo estático de tipos / Static type checking
```

#### 📌 Notas de Instalación / Installation Notes
- En sistemas Unix, puede ser necesario instalar `python3-tk`
  ```bash
  # Debian/Ubuntu
  sudo apt-get install python3-tk
  
  # RedHat/CentOS
  sudo yum install python3-tkinter
  
  # macOS (usando Homebrew)
  brew install python-tk
  ```

### Recursos de Aprendizaje / Learning Resources
- 📖 [Teoría de Compiladores / Compiler Theory](https://es.wikipedia.org/wiki/Compilador)
- 📚 [Libro: Compiladores: Principios, Técnicas y Herramientas](https://www.amazon.com/Compilers-Principles-Techniques-Tools-2nd/dp/0321486811) (Dragon Book)

### Herramientas Relacionadas / Related Tools
- [Generador de Analizadores Léxicos / Lexical Analyzer Generator](https://www.gnu.org/software/flex/)
- [Generador de Analizadores Sintácticos / Parser Generator](https://www.gnu.org/software/bison/)
- [Entorno de Desarrollo Recomendado / Recommended IDE](https://code.visualstudio.com/)
- [Extensiones Útiles para VS Code / Useful VS Code Extensions](#)
  - [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack)
  - [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
  - [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

### Contribuir al Proyecto / Contributing to the Project
1. Revisa los [issues abiertos](https://github.com/mariobeltran06/syntactic-analyzer/issues) / Check [open issues](https://github.com/mariobeltran06/syntactic-analyzer/issues)
2. Sigue las [guías de estilo](#-política-de-contribución--contribution-policy) / Follow the [style guides](#-política-de-contribución--contribution-policy)
3. Envía un Pull Request con una descripción clara / Submit a Pull Request with a clear description

### Soporte y Contacto / Support and Contact
¿Necesitas ayuda o tienes preguntas? / Need help or have questions?

#### 📧 Soporte Técnico / Technical Support
- Correo electrónico / Email: [mariobeltran06@gmail.com](mailto:mariobeltran06@gmail.com)
- Horario de atención / Support hours: Lunes a Viernes, 9AM - 5PM (CST)

#### 🐛 Reportar Problemas / Report Issues
- [Abrir un nuevo issue](https://github.com/mariobeltran06/syntactic-analyzer/issues/new/choose)
- Proporciona la siguiente información / Please provide the following information:
  - Descripción del problema / Problem description
  - Pasos para reproducir / Steps to reproduce
  - Versión del compilador / Compiler version
  - Sistema operativo / Operating System

### 📚 Sobre el Proyecto / About the Project

Este proyecto fue desarrollado como parte del curso de Autómatas y Compiladores en la Universidad Don Bosco, modalidad Educación a Distancia.  
This project was developed as part of the Automata and Compilers course at Don Bosco University, Distance Education program.

### 📊 Estadísticas / Statistics

[![Visitas / Visits](https://visitor-badge.laobi.icu/badge?page_id=mariobeltran06.syntactic-analyzer)](https://github.com/mariobeltran06/syntactic-analyzer)
[![Licencia / License](https://img.shields.io/badge/Licencia-MIT-blue.svg)](LICENSE)
[![Última versión / Latest Release](https://img.shields.io/github/v/release/mariobeltran06/syntactic-analyzer?style=flat-square)](https://github.com/mariobeltran06/syntactic-analyzer/releases)
[![Estado del Código / Code Status](https://img.shields.io/github/actions/workflow/status/mariobeltran06/syntactic-analyzer/python-package.yml?branch=main)](https://github.com/mariobeltran06/syntactic-analyzer/actions)

### 🌟 Agradecimientos / Acknowledgments

- A nuestros profesores por su guía y apoyo / To our professors for their guidance and support
- A la comunidad de código abierto / To the open-source community
- A todos los contribuyentes / To all contributors