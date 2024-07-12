# calculator.py

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.result /= num

    def get_result(self):
        return self.result
