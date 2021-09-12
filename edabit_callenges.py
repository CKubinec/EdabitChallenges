def hello():
    return "hello edabit.com"


def addition(a, b):
    """Adds two numbers together"""
    return a + b


def addition(num):
    """Adds one to the number"""
    return num + 1


def tri_area(base, height):
    """Calculates the area of a triangle"""
    return (base * height) / 2


def next_edge(side1, side2):
    """Function that finds the maximum range of a triangle's third edge"""
    return (side1 + side2) - 1


def remainder(x, y):
    """Uses modulo to return the remainder of x and y"""
    return x % y


def string_int(txt):
    """Takes a string and converts it to an integer"""
    return int(txt)


def find_perimeter(length, width):
    """Finds the perimeter of a square"""
    return (length * 2) + (width * 2)


def circuit_power(voltage, current):
    """Calculates the circuit power"""
    return voltage * current


def stutter(word: str):
    """Returns a string as if someone was stuttering"""
    first_two = word[0:2] + "... "
    return first_two * 2 + word + "?"


def how_many_seconds(hours):
    """Converting hours into seconds"""
    return hours * 3600


def convert(minutes):
    """Converting minutes into seconds"""
    return minutes * 60


def calc_age(age):
    """Calculated age in days"""
    return age * 365


def calculator(num1, operator, num2):
    """Allows a user to enter two numbers and an operator for basic math"""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num1 == 0 or num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1 / num2


def dis(price, discount):
    """Calculates a price after discount rounded to nearest 2nd decimal place"""
    discount_amount = discount/100 * price
    return (price - discount_amount).__round__(2)


if __name__ == '__main__':
    print(dis(100, 75))
