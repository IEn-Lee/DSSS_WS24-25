import random


def random_integer(min, max):
    """
    Generate a random integer between two given numbers.

    Args:
        min (int): The minimum value (inclusive).
        max (int): The maximum value (inclusive).

    Returns:
        int: A random integer between min and max.
    """
    return random.randint(min, max)


def random_operator():
    """
    Choice a random mathematical operator within +, -, *.

    Returns:
        str: A random mathematical operator within +, -, *.
    """
    return random.choice(['+', '-', '*'])


def math_operation(num1, num2, operator):
    """
    Give the problem and calculate the expected answer based on the operator.

    Args:
        num1 (int): The first given number.
        num2 (int): The second given number.
        operator (str): The given operator.

    Returns:
        tuple: the tuple containing the problem as the string and the answer as int.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 - num2
    elif operator == '-':
        answer = num1 + num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    Generate random math problems, the user give the answer, and will receive the feedback.
    """
    score = 0
    total_question = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question):
        num1 = random_integer(1, 10)
        num2 = random_integer(1, 5)
        operator = random_operator()

        PROBLEM, ANSWER = math_operation(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")

        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_question}")


if __name__ == "__main__":
    math_quiz()
