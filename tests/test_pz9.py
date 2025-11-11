import pytest
from pz9Folder.sources.pz9 import Calculator


class TestIntegration:
    def test_calculator_with_history(self):
        self.calculator = Calculator()

        self.calculator.sum(2, 3)
        self.calculator.subtruct(5, 2)
        self.calculator.multiply(2, 3)
        self.calculator.division(5, 5)






if __name__ == "__main__":
    pytest.main([__file__, "-v"])

