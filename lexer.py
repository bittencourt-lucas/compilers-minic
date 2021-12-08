import re

from token import Token, TokenType
from utils import load_MiniC_file

class Lexer:
  def __init__(self, file: str):
    self.buffer: str = load_MiniC_file(file)
    self.token: Token = Token(type=TokenType.EOF, value=0)

  def evaluate_expression(self, buffer: list) -> list:
    keyword = (TokenType.KEYWORD, '(^int$|^printf$|^printint$|^return$)')
    identifier = (TokenType.IDENTIFIER, '^[a-zA-Z_$][a-zA-Z_$0-9]*$')
    integer = (TokenType.INTEGER, '^([-]?[1-9]\d*|0)$')
    string = (TokenType.STRING, '^\".*\"$')
    operator = (TokenType.OPERATOR, '^(\+|\-|\/|\*|<|&&|=)$')
    comment = (TokenType.COMMENT, '^\/\/.*$')
    token_types = []
    for word in buffer:
      if (re.search(keyword[1], word)):
        token_types.append((keyword[0], word))
      elif (re.search(identifier[1], word)):
        token_types.append((identifier[0], word))
      elif (re.search(integer[1], word)):
        token_types.append((integer[0], word))
      elif (re.search(string[1], word)):
        token_types.append((string[0], word))
      elif (re.search(operator[1], word)):
        token_types.append((operator[0], word))
      elif (re.search(comment[1], word)):
        token_types.append((comment[0], word))
      else:
        token_types.append((TokenType.INVALID))
    return token_types

  def create_tokens(self, token_types: list) -> list:
    tokens = []
    for token in token_types:
      if token[0] == TokenType.INVALID:
        pass
      elif token[0] == TokenType.INTEGER:
        tokens.append(Token(token[0], int(token[1]), None))
      elif token[0] == TokenType.IDENTIFIER or token[0] == TokenType.OPERATOR or token[0] == TokenType.KEYWORD:
        tokens.append(Token(token[0], 0, token[1]))
      else:
        tokens.append(Token(token[0], 0, None))
    return tokens

  def get_next_token(self) -> None:
    expressions = list(filter(None, self.buffer.split('\n')))
    buffer = []
    for expression in expressions:
      if '//' in expression:
        expression = expression
        buffer.append(expression)
      elif '"' in expression:
        expression = expression.strip().replace("(", "\n").replace(")", "").replace(";", "").split("\n")
        buffer.extend(expression)
      else:
        expression = expression.replace(";", "").replace("(", " ").replace(")", "").replace("{", "").replace("}", "").split(" ")
        buffer.extend(expression)
    token_types = self.evaluate_expression(list(filter(None, buffer)))
    tokens = self.create_tokens(token_types)
    for token in tokens:
      print(token)