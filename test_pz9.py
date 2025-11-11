import pytest
from pz9 import Calculator


class TestIntegration:
    def setup_method(self):
        self.calculator = Calculator()


    def test_addition_positive_numbers(self):

        assert self.calculator.sum(2, 3) == 5
        assert self.calculator.sum(10, 15) == 25

    def test_addition_negative_numbers(self):
        assert self.calculator.sum(-2, -3) == -5
        assert self.calculator.sum(-10, -5) == -15

    def test_addition_mixed_signs(self):
        assert self.calculator.sum(5, -3) == 2
        assert self.calculator.sum(-10, 15) == 5

    def test_addition_with_zero(self):
        assert self.calculator.sum(0, 5) == 5
        assert self.calculator.sum(5, 0) == 5
        assert self.calculator.sum(0, 0) == 0

    def test_addition_large_numbers(self):
        assert self.calculator.sum(1000000, 2000000) == 3000000
        assert self.calculator.sum(-1000000, -2000000) == -3000000



    def test_subtraction_positive_numbers(self):
        assert self.calculator.subtruct(5, 3) == 2
        assert self.calculator.subtruct(10, 2) == 8

    def test_subtraction_negative_numbers(self):
        assert self.calculator.subtruct(-2, -3) == 1
        assert self.calculator.subtruct(-5, -2) == -3

    def test_subtraction_mixed_signs(self):
        assert self.calculator.subtruct(5, -3) == 8
        assert self.calculator.subtruct(-5, 3) == -8

    def test_subtraction_with_zero(self):
        assert self.calculator.subtruct(5, 0) == 5
        assert self.calculator.subtruct(0, 5) == -5
        assert self.calculator.subtruct(0, 0) == 0

    def test_subtraction_large_numbers(self):
        assert self.calculator.subtruct(5000000, 2000000) == 3000000
        assert self.calculator.subtruct(-5000000, -2000000) == -3000000


    # ТЕСТЫ УМНОЖЕНИЯ
    def test_multiplication_positive_numbers(self):
        assert self.calculator.multiply(2, 3) == 6
        assert self.calculator.multiply(5, 4) == 20

    def test_multiplication_negative_numbers(self):
        assert self.calculator.multiply(-2, -3) == 6
        assert self.calculator.multiply(-2, 3) == -6

    def test_multiplication_with_zero(self):
        assert self.calculator.multiply(5, 0) == 0
        assert self.calculator.multiply(0, 5) == 0
        assert self.calculator.multiply(0, 0) == 0

    def test_multiplication_with_one(self):
        assert self.calculator.multiply(5, 1) == 5
        assert self.calculator.multiply(1, 5) == 5
        assert self.calculator.multiply(-5, 1) == -5

    def test_multiplication_large_numbers(self):
        assert self.calculator.multiply(1000, 2000) == 2000000
        assert self.calculator.multiply(-1000, 2000) == -2000000


    # ТЕСТЫ ДЕЛЕНИЯ
    def test_division_positive_numbers(self):
        assert self.calculator.division(6, 3) == 2
        assert self.calculator.division(10, 2) == 5

    def test_division_negative_numbers(self):
        assert self.calculator.division(-6, -3) == 2
        assert self.calculator.division(-6, 3) == -2

    def test_division_with_one(self):
        assert self.calculator.division(5, 1) == 5
        assert self.calculator.division(1, 2) == 0.5


    def test_division_zero_by_number(self):
        assert self.calculator.division(0, 5) == 0
        assert self.calculator.division(0, -5) == 0


    def test_boundary_values(self):
        assert self.calculator.sum(999999, 1) == 1000000
        assert self.calculator.sum(-999999, -1) == -1000000



    def test_sequence_of_operations(self):
        result = self.calculator.sum(10, 5)
        result = self.calculator.subtruct(result, 3)
        result = self.calculator.multiply(result, 2)
        result = self.calculator.division(result, 4)
        assert result == 6


    def test_error_handling_preserves_state(self):
        self.calculator.sum(5, 3)
        self.calculator.multiply(2, 2)


        try:
            self.calculator.division(10, 0)
        except ValueError:
            pass


        assert self.calculator.sum(1, 1) == 2
        assert self.calculator.multiply(3, 3) == 9



if __name__ == "__main__":
    pytest.main([__file__, "-v"])