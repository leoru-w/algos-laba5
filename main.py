class Nice_calc_tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        if not self.left and not self.right:
            return True
        else:
            return False


def make_tree(tokens):
    stack = []

    for t in tokens:
        if t in "+-*/^":
            n_right = stack.pop()
            n_left = stack.pop()
            res = Nice_calc_tree(t, n_left, n_right)
            stack.append(res)
        else:
            versh= Nice_calc_tree(int(t))
            stack.append(versh)

    if len(stack) > 0:
        return stack[0]
    else:
        return None


def calculate(versh):
    if versh is None:
        return 0

    if versh.is_leaf():
        return versh.val

    v1 = calculate(versh.left)
    v2 = calculate(versh.right)

    if versh.val == '+':
        return v1 + v2
    elif versh.val == '-':
        return v1 - v2
    elif versh.val == '*':
        return v1 * v2
    elif versh.val == '/':
        return v1 / v2
    elif versh.val == '^':
        return v1 ** v2

print(calculate(make_tree(["2", "5", "*", "3", "+"])))
print(calculate(make_tree(["2", "3", "^"])))
