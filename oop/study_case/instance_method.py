class Rectangle:
    def __init__(self, s, d):
        self.s = s
        self.d = d
        
    def area_formula(self):
        return self.s ** 2
    
    def circumference_formula(self):
        return 4 * self.s
    
    def formula_area_of_a_diagonal(self):
        return (self.d ** 2) / 2
    
task1 = Rectangle(2, 2)
print(task1.area_formula())
print(task1.circumference_formula())
print(task1.formula_area_of_a_diagonal())