class Converter:
    priority = {
        '(': 0,
        '+': 1,
        '−': 1,
        ')': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3
    }

    def convert(self, expression):
        stack = []
        out = []

        for item in expression:
            if item not in self.priority:
                out.append(item)
            elif item == '(':
                stack.append(item)
            elif item == ')' and '(' in stack:
                while stack[len(stack) - 1] != '(':
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

        return list(filter(lambda elem: elem != '(' and elem != ')', out))