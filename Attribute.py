import AST

def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    
    return decorator

class Attribute:
    @addToClass(AST.Node)
    def calcAttr(self):
        raise Exception("calcAttr not defined in class " + self.__class__.__name__)

    @addToClass(AST.Expr)
    def calcAttr(self):
        self.P, _ = self.expr.calcAttr()

        return self.P

    @addToClass(AST.AddSub)
    def calcAttr(self):
        leftP, leftT = self.left.calcAttr()
        rightP, rightT = self.right.calcAttr()

        self.P = leftP + self.op + rightP
        self.T = leftT + self.op + rightT

        return self.P, self.T
    
    @addToClass(AST.Mul)
    def calcAttr(self):
        leftP, leftT = self.left.calcAttr()
        rightP, rightT = self.right.calcAttr()

        self.P = "(" + leftP + "*" + rightT + "+" + leftT + "*" + rightP + ")"
        self.T = leftT + "*" + rightT

        return self.P, self.T
    
    @addToClass(AST.Div)
    def calcAttr(self):
        leftP, leftT = self.left.calcAttr()
        rightP, rightT = self.right.calcAttr()

        self.P = "(" + leftP + "*" + rightT + "-" + leftT + "*" + rightP +\
            ")/(" + rightT + "*" + rightT + ")"
        self.T = leftT + "/" + rightT

        return self.P, self.T
    
    @addToClass(AST.Par)
    def calcAttr(self):
        P, T = self.expr.calcAttr()

        self.P = "(" + P + ")"
        self.T = "(" + T + ")"

        return self.P, self.T
    
    @addToClass(AST.Exp)
    def calcAttr(self):
        P, T = self.expr.calcAttr()

        self.P = "(" + P + ")*exp(" + T + ")"
        self.T = "exp(" + T + ")"

        return self.P, self.T
    
    @addToClass(AST.Var)
    def calcAttr(self):
        self.P = "1"
        self.T = "x"

        return self.P, self.T
    
    @addToClass(AST.Const)
    def calcAttr(self):
        self.P = "0"
        self.T = "1"

        return self.P, self.T
