from sly import Parser
from Scanner import Scanner
import AST

class Mparser(Parser):
    tokens = Scanner.tokens
    debugfile = 'parser.out'

    precedence = (
        ("left", '+', '-'),
        ("left", '*', '/'),
        ("left", EXP)
    )

    @_('E')
    def S(self, p):
        return AST.Expr(p[0])

    @_('E "+" E',
       'E "-" E')
    def E(self, p):
        return AST.AddSub(p[1], p[0], p[2])
    
    @_('E "*" E')
    def E(self, p):
        return AST.Mul(p[0], p[2])
    
    @_('E "/" E')
    def E(self, p):
        return AST.Div(p[0], p[2])
    
    @_('"(" E ")"')
    def E(self, p):
        return AST.Par(p[1])

    @_('EXP "(" E ")"')
    def E(self, p):
        return AST.Exp(p[2])

    @_('"x"')
    def E(self, p):
        return AST.Var(p[0])
    
    @_('"1"')
    def E(self, p):
        return AST.Const(p[0])
