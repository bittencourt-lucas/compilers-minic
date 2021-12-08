import re

from token import TokenType

keyword = (TokenType.KEYWORD, '(^int$|^printf$|^printint$|^return$)')
identifier = (TokenType.IDENTIFIER, '^[a-zA-Z_$][a-zA-Z_$0-9]*$')
integer = (TokenType.INTEGER, '^([-]?[1-9]\d*|0)$')
string = (TokenType.STRING, '^\".*\"$')
operator = (TokenType.OPERATOR, '^(\+|\-|\/|\*|<|&&|=)$')
comment = (TokenType.COMMENT, '^\/\/.*$')

buffer = [
          '// This is a comment',
          'printf',
          '"This is a string"',
          'int',
          'year1994',
          '1994',
          'int',
          '_another_year',
          '2021',
          'printint',
          '42',
          '*',
          '42',
          'return',
          '0'
        ]

for word in buffer:
  if (re.search(keyword[1], word)):
    print(keyword[0])
  elif (re.search(identifier[1], word)):
    print(identifier[0])
  elif (re.search(integer[1], word)):
    print(integer[0])
  elif (re.search(string[1], word)):
    print(string[0])
  elif (re.search(operator[1], word)):
    print(operator[0])
  elif (re.search(comment[1], word)):
    print(comment[0])
  else:
    print(TokenType.INVALID)