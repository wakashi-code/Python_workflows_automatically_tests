
class Calculator:

    def sum(self, a: int, b: int) -> int:
        return a + b

    def subtruct(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def division(self, a: int, b: int) -> float:
        try:
            result = a / b
            return result
        except ZeroDivisionError as e:
            print(f"Произошло исключение: {e}")
            print("Деление на ноль запрещено")
            return None







