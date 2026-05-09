import re

def interpreter(exp: str) -> float:
    exp = exp.strip().lower().replace(' ', '')
    if re.match(r"[a-z]", exp):
        raise ValueError("interpreter: operands should only be numbers")
    
    exp_operands = re.match(r"^(\d{1,})([\+,\-,\*,\/])(\d{1,})$", exp)
    if not exp_operands:
        raise ValueError("interpreter: invalid expression")

    x = float(exp_operands.group(1))
    op = exp_operands.group(2)
    y = float(exp_operands.group(3))

    if op == '/':
        if y == 0:
            raise ZeroDivisionError()
        return x // y
    elif op == '*':
        return x * y
    elif op == '-':
        return x - y
    elif op == '+':
        return x + y
    else:
        raise ValueError("interpreter: unknown operand")