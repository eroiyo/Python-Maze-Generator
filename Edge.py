from functools import total_ordering
@total_ordering
class Edge:
    def __init__(self, vertex_A, vertex_B, weight, row, column, direction):
        self.vertex_A =vertex_A
        self.vertex_B=vertex_B
        self.weight=weight
        self.row=row
        self.column=column
        self.direction=direction

    def __eq__(self, other):
        return self.weight == other.weight
  
    def __le__(self, other):
        return self.weight<= other.weight
      
    def __ge__(self, other):
        return self.weight>= other.weight
          
    def __ne__(self, other):
        return self.weight != other.weight
    
    def myWeight(self):
        return self.weight

    def myVertex_A(self):
        return self.vertex_A

    def myVertex_B(self):
        return self.vertex_B

    def myRow(self):
        return self.row

    def myColumn(self):
        return self.column

    def myColumn(self):
        return self.direction

    def present(self):
        print("Hello, this is my vertex_a:",self.vertex_A," this is my vertex_B:",self.vertex_B," this is my direction:",self.direction)