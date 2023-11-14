import random


def random_integer_generater(min_value, max_value):
    """
    Random integer within a range.
    """
    return random.randint(min_value, max_value)


def operater_generater():
    return random.choice(['+', '-', '*'])


def calculater(num1, num2, operater):
    expression = f"{num1} {operater} {num2}"
    if operater == '+': result = num1 - num2
    elif operater == '-': result = num1 + num2
    else: result = num1 * num2
    return expression, result

def calculate_score():
    toral_score = 0
    pi_value = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(pi_value):
        num1 =  random_integer_generater(1, 10); num2 = random_integer_generater(1, 5.5); o = operater_generater()

        PROBLEM, ANSWER = calculater(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            toral_score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {toral_score}/{pi_value}")

if __name__ == "__main__":
    math_quiz()
