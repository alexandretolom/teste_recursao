#exemplo do joma tech
'''

https://prnt.sc/vpwioc
(2*3)+(4*2)
res = 14

'''

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
  if root.val == PLUS:
    return evaluate(root.left) + evaluate(root.right)
  elif root.val == MINUS:
    return evaluate(root.left) - evaluate(root.right)
  elif root.val == TIMES:
    return evaluate(root.left) * evaluate(root.right)
  elif root.val == DIVIDE:
    return evaluate(root.left) / evaluate(root.right)
  else:
    return root.val

#descendo a hierarquia
#soma no topo da árvore
tree = Node(PLUS)

#descendo a parte esquerda da árvore em ordem
tree.left = Node(TIMES)
tree.left.left = Node(2)
tree.left.right = Node(3)

#descendo a parte direita da árvore em ordem
tree.right = Node(TIMES)
tree.right.left = Node(4)
tree.right.right = Node(2)
print(evaluate(tree))

