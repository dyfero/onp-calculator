import operator

from helper import is_numeric


class Onp:
    operators = {
        '+': operator.add,
        '−': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '^': operator.pow,
    }

    def calc(self, onp):
        stack = []
        while onp:
            item = onp.pop(0)
            if is_numeric(item):
                stack.append(item)
            else:
                a = float(stack.pop())
                b = float(stack.pop())
                res = self.operators[item](b, a)
                stack.append(res)

        return stack.pop()

    # def check(self, onp):
    #     size = 0
    #     for elem in onp:
    #         if is_numeric(elem):
    #             size += 1
    #         elif elem in self.operators:
    #             size -= 1
    #         else:
    #             return False
    #     return size == 1
