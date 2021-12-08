from enum import Enum, auto

class TokenType(Enum):
  COMMENT = auto()
  KEYWORD = auto()
  INTEGER = auto()
  IDENTIFIER = auto()
  STRING = auto()
  OPERATOR = auto()
  INVALID = auto()
  EOF = auto()

class Token:
  def __init__(self, type: TokenType = None, value: int = 0, name: str = None):
    self.type = type
    self.value = value
    self.name = name

  def __str__(self):
    return "{type}: (value='{value}', name='{name}')".format(type=self.type, value=self.value, name=self.name)
