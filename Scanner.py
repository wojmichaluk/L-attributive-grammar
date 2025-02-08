import sys
from sly import Lexer

class Scanner(Lexer):
    # Set of nonliteral token names
    tokens = { EXP }

    literals = {'+', '-', '*', '/', '(', ')', 'x', '1'}

    # Strings containing ignored characters and comments
    ignore = ' \t'
    ignore_comment = r'\#.*'

    # Regular expression rules for tokens
    EXP = r'exp'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Reporting errors
    def error(self, t):
        print('Wrong input! Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "examples/example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = Scanner()

    for tok in lexer.tokenize(text):
        print(f'({tok.lineno}): {tok.type}({tok.value})')
