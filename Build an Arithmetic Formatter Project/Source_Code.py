def arithmetic_arranger(problems, display_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_operands = []
    second_operands = []
    operators = []
    results = []
    
    for problem in problems:
        parts = problem.split()
        
        if len(parts) != 3:
            return "Error: Incorrect format."
        
        first_operand, operator, second_operand = parts
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)
        
        if display_answers:
            if operator == '+':
                results.append(str(int(first_operand) + int(second_operand)))
            else:
                results.append(str(int(first_operand) - int(second_operand)))

    arranged_problems = []
    
    # ------------- Width Calculations ---------------------

    widths = [max(len(f), len(s)) + 2 for f, s in zip(first_operands, second_operands)]
    
    # -------------- Problem Arrangement --------------------
    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""
    
    for i in range(len(problems)):
        width = widths[i]
        first_line += first_operands[i].rjust(width)
        second_line += operators[i] + second_operands[i].rjust(width - 1)
        dashes += '-' * width
        if display_answers:
            answers += results[i].rjust(width)
        
        if i < len(problems) - 1:
            first_line += "    "
            second_line += "    "
            dashes += "    "
            if display_answers:
                answers += "    "
    
    arranged_problems.append(first_line)
    arranged_problems.append(second_line)
    arranged_problems.append(dashes)

    if display_answers:
        arranged_problems.append(answers)
    
    return "\n".join(arranged_problems)


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
