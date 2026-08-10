import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Map string operators to their corresponding functions
        operator_mapping = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "//": operator.floordiv,
            "**": operator.pow,
            "%": operator.mod,
        }

        stack = []
        for t in tokens:
            if t not in operator_mapping:
                stack.append(int(t))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                operation = operator_mapping[t]
                res = int(operation(first_operand, second_operand))
                stack.append(res)
        return stack[-1]