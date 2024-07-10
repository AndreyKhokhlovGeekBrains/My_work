from typing import List

class Matrix:  
    
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for col in range(self.cols)] for row in range(self.rows)]
                
    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, item)) for item in self.data])
    
    def __repr__(self) -> str:
        return f'Matrix({self.rows}, {self.cols})'
    
    def __eq__(self, other) -> bool:
        if self.rows != other.rows or self.cols != other.cols:
            return False
        else:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.data[row][col] != other.data[row][col]:
                        return False
            return True
        
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        else:
            new_matrix = Matrix(self.rows, self.cols)
            for row in range(self.rows):
                for col in range(self.cols):
                    new_matrix.data[row][col] = self.data[row][col] + other.data[row][col]
            return new_matrix
        
    def __mul__(self, other):
        if self.cols == other.rows:
            new_matrix = Matrix(self.rows, other.cols)
            for row in range(self.rows):
                for col in range(other.cols):
                    for item in range(self.cols):
                        new_matrix.data[row][col] += self.data[row][item] * other.data[item][col]      
            return new_matrix
        return None
        
        
if __name__ == '__main__':
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)
        
