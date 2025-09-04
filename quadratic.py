import math

def solve_quadratic_equation(coefficients: list[float]):
    a, b, c = coefficients

    # We'll check if none of the coefficients are 0, and if one of them is, jump to elif statements and change the result
    if all(a, b, c) != 0:

        # Basicly, discriminant is the number inside of the square root, we will calculate it separately
        discriminant = (b ** 2.0) - (4.0 * (a * c))

        # It cannot be less than 0
        if discriminant < 0:
            result = [0, None]

        # And if it's equal to 0, two of the solutions are the same, and we return just one
        elif discriminant == 0:
            x = (b * -1.0) / (2.0 * a)
            result = [1 , x]

        # At last, if discriminant's value is positive, we use the formula
        elif discriminant > 0:
            x1 = ((b * -1.0) + math.sqrt(discriminant)) / (2.0 * a)
            x2 = ((b * -1.0) - math.sqrt(discriminant)) / (2.0 * a)

            # We return a list which contains an integer and (in this case) a tuple of two solutions
            # For why I do it exactly like that, check main function's comment on match-case statement
            result = [2, (x1, x2)]

    # If the first coefficient is 0, it wouldn't be a quadratic equation anymore, so we calculate the only solution
    elif a == 0: result = [3, ((c * -1) / b)]

    # If the second one is 0, we'll just solve incomplete quadratic equation (ax² + c = 0)
    elif b == 0: 
        if c * -1 > 0: result = [4, (math.sqrt((c * -1) / a), math.sqrt((c * -1) / a) * -1)]

        # And if c negative is less than 0, we don't have any real solutions
        else: result = [5, None]

    # And at last, if c equals 0, we'll have incomplete quadratic equation of type ax² + bx = 0, which we factor down to x(ax + b) = 0 and solve
    elif c == 0: result = [6, (0, (b * -1) / a)]
    return result

def display_quadratic_equation(coefficients: list[float]):
    a, b, c = coefficients

    # By default, we set operators to be addition, and change them later
    first_operator, second_operator = '+', '+'

    # Here is a boolean that gets set to 0 if we have a valid equation, otherwise, a funny message will be shown
    special_message = 1

    # Check if a is an integer
    if a % 1 == 0: 
        a = int(a)

        # Then, if it's equal to 1 or 0, we don't display the 1 at the start
        if a == 1: a = ''
        elif a == -1: a = '-'

    # We do pretty much the exact thing to b
    if b % 1 == 0: 
        b = int(b)
    if b == 1: b = ''

    # But we also check if it's negative, and if so, we change the "first operator" and set b to its positive value
    elif b < 0:
        first_operator = '-'
        b = abs(b)

    # And, finally, check c just like the previous one
    if c % 1 == 0: 
        c = int(c)
    if c < 0:
        second_operator = '-'
        c = abs(c)
    
    # When we succesfully asign new values to stuff (if needed), we start to change the output based on which coefficients are equal to 0
    # If a is, then we get just a linear equation
    if a == 0: output = f'{b}x {second_operator} {c} = 0'

    # If b is, it's an incomplete quadratic equation of type ax² + c = 0
    elif b == 0: output = f'{a}x² {second_operator} {c} = 0'

    # The same with c, but it looks like that: ax² + bx = 0
    elif c == 0: output = f'{a}x² {first_operator} {b}x = 0'

    # And if none of the coefficients are 0, it's completly normal equation
    else: output = f'{a}x² {first_operator} {b}x {second_operator} {c} = 0'
    
    # Then, the funny part. It displays error messages if the answer is just 0 or it has no solutions
    if a == 0 and b == 0 and c == 0: output = 'Dude, you just entered a bunch of zeros. I wonder what the result would be...'
    elif a == 0 and b == 0: output = 'Nah, your c isn\'t zero. That ain\'t a valid equation.'
    elif a == 0 and c == 0: output = 'Yeah, x is zero whatever the value of b is. Great job.'
    elif b == 0 and c == 0: output = 'Is it just me or... The x is zero..?'
    else: special_message = 0

    # And we yet again return a list, so then we can check if the equation is actually valid
    return [special_message, output]

def main():
    print('This script solves a simple quadratic equation of general form ax² + bx + c = 0.')
    user_input = input('Write down the coefficients a, b and c, separeted by commas: ')

    # We read the user input and split it by commas, therefore, we get list of 3 numbers (in a good case)
    user_coefficients = user_input.split(',', 3)

    # If we don't get 3 separate elements, we skip all of it and output an error
    if len(user_coefficients) == 3:

        # We try to convert user coefficients to float type
        try: a, b, c = float(user_coefficients[0]), float(user_coefficients[1]), float(user_coefficients[2])

        # And if we fail, then user may have wrote something other than numbers
        except ValueError: print('All of the coefficients must be valid numbers). Please try again.')

        # We execute the "display" function, and assing the output to 2 variables
        show_error, equation = display_quadratic_equation([a, b, c])

        # If we got 1 (True), we show our funny message from earlier and quit program
        if show_error:
            print(equation)
            return
        
        # Else, we show user the equation and its solution(s)
        else:

            # Call "solve" and store two variables: one for the "type check", and the other one is the answer
            response, answer = solve_quadratic_equation([a, b, c])

            # Now, we have quite a long match-case statement to check the type of the result we got from "solve" function
            match response:

                # So 0 means the discriminant is negative
                case 0: print(f'{equation} has no real solutions (D < 0).')

                # 1 means discriminant equals to 0, therefore two of the solutions are the same, and we only output one
                case 1: 
                    if answer % 1 == 0: answer = int(answer)
                    print(f'{equation} has only one solution (D = 0): {round(answer, 2)}.')

                # And so with the other ones, I hope you get this (I kinda got bored explaining all this)
                case 2:
                    x1, x2 = answer
                    if x1 % 1 == 0: x1 = int(x1)
                    if x2 % 1 == 0: x2 = int(x2)
                    print(f'{equation} has two solutions (D > 0): {round(x1, 3)} and {round(x2, 3)}.')

                case 3: 
                    if answer % 1 == 0: answer = int(answer)
                    print(f'{equation} has one solution (it is a linear equstion): {round(answer, 3)}.')

                case 4: 
                    x1, x2 = answer
                    if x1 % 1 == 0: x1 = int(x1)
                    if x2 % 1 == 0: x2 = int(x2)
                    print(f'{equation} has two real solutions (it is an incomplete quadratic equation): {round(x1, 3)} and {round(x2, 3)}.')

                case 5: print(f'{equation} has no real solutions.')

                case 6: 
                    x1, x2 = answer
                    if x1 % 1 == 0: x1 = int(x1)
                    if x2 % 1 == 0: x2 = int(x2)
                    print(f'{equation} has two real solutions (it is an incomplete quadratic equation): {round(x1, 3)} and {round(x2, 3)}.')

    else: print('Wrong format of input. Please, try again.')

main()

# And that's all. 88 lines of code, 38 comments to explain all this mess, and 45 empty lines for no reason :D. To be expanded, upgraded, remade and continued. 04/09/2025, - KJL
