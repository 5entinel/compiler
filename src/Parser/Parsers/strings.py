from src.Parser.Parsers.basic import *

from src.Parser.AST.strings import *

string_predefined_functions = {
    'strlen': StrLen,
    'strget': StrGet,
    'strsub': StrSub,
    'strdup': StrDup,
    'strset': StrSet,
    'strcat': StrCat,
    'strcmp': StrCmp,
    'strmake': StrMake
}

def str_exp():
    return Tag(STRING) ^ String

def char_exp():
    return Tag(CHAR) ^ Char
