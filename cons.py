def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(g):
  def carHelper(i, j):
    return i
  return g(carHelper)

def cdr(g):
  def cdrHelper(i, j):
    return j
  return g(cdrHelper)

print("Car:", car(cons(3 ,4)))
print("Cons:", cdr(cons(3, 4)))