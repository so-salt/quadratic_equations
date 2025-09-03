import math

def solve_quadratic_equation(coefficients: list[float]):
    a, b, c = coefficients
    discriminant = (b ** 2.0) - (4.0 * (a * c))
    if discriminant > 0:
        x1 = ((b * -1.0) + math.sqrt(discriminant)) / (2.0 * a)
        x2 = ((b * -1.0) - math.sqrt(discriminant)) / (2.0 * a)
        result = [2, (x1, x2)]
    elif discriminant == 0:
        x = (b * -1.0) / (2.0 * a)
        result = [1 ,x]
    elif discriminant < 0:
        result = [0, None]
    return result

def io_system():
    print('This script solves a simple quadratic equation of general form ax² + bx + c = 0.')
    user_input = input('Write down the coefficients a, b and c, separeted by commas: ')
    user_coefficients = user_input.split(',', 3)
    if len(user_coefficients) == 3:
        a, b, c = float(user_coefficients[0]), float(user_coefficients[1]), float(user_coefficients[2])
        response, answer = solve_quadratic_equation([a, b, c])
        if a == 1: a = ''
        elif a == -1: a = '-'
        elif a % 1 == 0: a = int(a)
        if b < 0: 
            b = abs(b)
            first_operation = '-'
        else: first_operation = '+'
        if b % 1 == 0: b = int(b)
        if c < 0: 
            c = abs(c)
            second_operation = '-'
        else: second_operation = '+'
        if c % 1 == 0: c = int(c)
        match response:
            case 2:
                x1 = answer[0]
                x2 = answer[1]
                if x1 % 1 == 0: x1 = int(x1)
                if x2 % 1 == 0: x2 = int(x2)
                print(f'{a}x² {first_operation} {b}x {second_operation} {c} = 0 has two solutions (D > 0): {round(x1, 2)} and {round(x2, 2)}.')
            case 1: 
                if answer % 1 == 0: answer = int(answer)
                print(f'{a}x² {first_operation} {b}x {second_operation} {c} = 0 has only one solution (D = 0): {round(answer, 2)}.')
            case 0: print(f'{a}x² {first_operation} {b}x {second_operation} {c} = 0 has no real solutions (D < 0).')
            case _: print('wtf')
    else: print('Wrong format of input. Please, try again.')

io_system()