def arithmetic_arranger(problems, show_answers=False):
    if(len(problems) > 5):
        return 'Error: Too many problems.'
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for prob in problems:
        parts = prob.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        left, operator, right = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(left), len(right)) + 2

        first_line.append(left.rjust(width))
        second_line.append(operator + ' ' + right.rjust(width - 2))
        dashes_line.append('-' * width)

        if show_answers:
            answer = str(eval(prob))
            answers_line.append(answer.rjust(width))

    arranged = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes_line)
    )

    if show_answers:
        arranged += '\n' + '    '.join(answers_line)

    return arranged
    

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
