# -*- coding: utf-8 -*-

from src.VM.commands import *

# Мапа соответствий: строковое представление команды VM - класс команды VM
commands_map = {
    'PUSH': Push,
    'POP': Pop,
    'NOP': Nop,
    'DUP': Dup,
    'LOAD': Load,
    'BLOAD': BLoad,
    'DLOAD': DLoad,
    'DBLOAD': DBLoad,
    'STORE': Store,
    'BSTORE': BStore,
    'DSTORE': DStore,
    'DBSTORE': DBStore,
    'ADD': Add,
    'MUL': Mul,
    'SUB': Sub,
    'DIV': Div,
    'MOD': Mod,
    'INVERT': Invert,
    'COMPARE': Compare,
    'LABEL': Label,
    'JUMP': Jump,
    'JZ': Jz,
    'JNZ': Jnz,
    'READ': Read,
    'WRITE': Write,
    'ENTER': Enter,
    'CALL': Call,
    'FUNCTION': Function,
    'RETURN': Return,
    'MALLOC': Malloc,
    'DMALLOC': DMalloc,
    'LOG': Log
}

# Разделитель команд VM
COMMAND_SEPARATOR = '\n'

# Разделитель аргументов команд VM
ARGS_SEPARATOR = ' '
