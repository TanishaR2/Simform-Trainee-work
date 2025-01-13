class Calculator:
    def add(self, a, b=None):
        if b is not None:
            return a + b
        return a + a
    
calc = Calculator()
print(calc.add(8, 6))    # 8 + 6 = 14
print(calc.add(8))       # 8 + 8 = 16


