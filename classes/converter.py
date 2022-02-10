from classes.constants.operator import OperatorEnum
from classes.helpers.helper import is_numeric


class Converter:
    priority = {
        OperatorEnum.LBR: 0,
        OperatorEnum.ADD: 1,
        OperatorEnum.SUB: 1,
        OperatorEnum.RBR: 1,
        OperatorEnum.MUL: 2,
        OperatorEnum.DIV: 2,
        OperatorEnum.MOD: 2,
        OperatorEnum.POW: 3
    }

    def convert(self, expression):
        expression = self.fix_expression(expression)

        stack = []
        out = []

        for item in expression:
            if item not in self.priority:
                out.append(item)
            elif item == OperatorEnum.LBR:
                stack.append(item)
            elif item == OperatorEnum.RBR and OperatorEnum.LBR in stack:
                while stack[len(stack) - 1] != OperatorEnum.LBR:
                    out.append(stack.pop())
                stack.pop()
            elif not stack or self.priority.get(item) > self.priority.get(stack[len(stack) - 1]):
                stack.append(item)
            else:
                while len(stack) > 0 and (self.priority.get(stack[len(stack) - 1]) >= self.priority.get(item)):
                    out.append(stack.pop())
                stack.append(item)

        while stack:
            out.append(stack.pop())

        return list(filter(lambda elem: elem != OperatorEnum.LBR and elem != OperatorEnum.RBR, out))

    def fix_expression(self, expression):
        if not expression:
            return []

        if not is_numeric(expression[-1]):
            expression = expression[:-1]

        return expression
