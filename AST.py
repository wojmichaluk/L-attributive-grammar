class Node(object):
    def __init__(self):
        # attributes
        self.P = None
        self.T = None

class Expr(Node):
    def __init__(self, expression):
        super().__init__()
        self.expr = expression

class AddSub(Node):
    def __init__(self, op, left, right):
        super().__init__()
        self.op = op
        self.left = left
        self.right = right

class Mul(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

class Div(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

class Par(Node):
    def __init__(self, expression):
        super().__init__()
        self.expr = expression

class Exp(Node):
    def __init__(self, expression):
        super().__init__()
        self.expr = expression

class Var(Node):
    def __init__(self, variable):
        super().__init__()
        self.var = variable

class Const(Node):
    def __init__(self, const):
        super().__init__()
        self.const = const
