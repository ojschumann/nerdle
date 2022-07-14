class Operator:
  def __init__(self, op):
    self.op = op

  def __call__(self, a, b):
    if a is None or b is None:
      return None
    return self.calc(a, b)


class Plus(Operator):
  def __init__(self):
    super().__init__('+')

  def calc(self, a, b):
    return a+b

class Minus(Operator):
  def __init__(self):
    super().__init__('-')

  def calc(self, a, b):
    return a-b

class Product(Operator):
  def __init__(self):
    super().__init__('*')

  def calc(self, a, b):
    return a*b

class Divide(Operator):
  def __init__(self):
    super().__init__('/')

  def calc(self, a, b):
    if b == 0:
      return None
    u,v = divmod(a, b)
    if v == 0:
      return u
    return None


OP = (Plus(), Minus(), Product(), Divide())

for a in range(1, 1000):
  for b in range(1, 1000):
    for op in OP:
      c = op(a, b)
      if c is not None and c >= 0:
        s = f"{a}{op.op}{b}={c}"
        if len(s) == 8:
          print(s)


for a in range(1, 100):
  for b in range(1, 100):
    for c in range(1, 100):
      for op1 in OP:
        for op2 in OP:
          if op2.op in "*/" and op1.op in "+-":
            d = op1(a, op2(b,c))
          elif op2.op == "*"  and op1.op == "/":
            d = op1(op2(a,c), b)
          else:
            d = op2(op1(a,b), c)
          if d is not None and d >= 0:
            s = f"{a}{op1.op}{b}{op2.op}{c}={d}"
            if len(s) == 8:
              print(s)
